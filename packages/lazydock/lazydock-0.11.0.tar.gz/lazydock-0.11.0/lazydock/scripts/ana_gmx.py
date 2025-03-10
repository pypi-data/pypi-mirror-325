import argparse
import os
from pathlib import Path
from typing import Dict, List, Tuple, Union

from tqdm import tqdm
from MDAnalysis import Universe
from mbapy_lite.base import put_err, put_log
from mbapy_lite.file import get_paths_with_extension, opts_file
from mbapy_lite.web import TaskPool
from lazydock.gmx.run import Gromacs
from lazydock.gmx.mda.convert import PDBConverter
from lazydock.scripts.ana_interaction import simple_analysis, pml_mode, plip_mode
from lazydock.scripts._script_utils_ import Command, clean_path, excute_command


class simple(Command):
    HELP = """
    simple analysis for GROMACS simulation
    0. gmx_mpi trjconv -s md.tpr -f md.xtc -o md_center.xtc -pbc mol -center
    
    1. gmx_mpi rms -s md.tpr -f md_center.xtc -o rmsd.xvg -tu ns 
    2. gmx_mpi rmsf -s md.tpr -f md_center.xtc -o rmsf.xvg
    3. gmx_mpi gyrate -s md.tpr -f md_center.xtc -o gyrate.xvg
    4. gmx_mpi hbond -s md.tpr -f md_center.xtc -num -dt 10
    
    5. gmx_mpi sasa -s md.tpr -f md_center.xtc -o sasa_total.xvg -or sasa_res.xvg -tu ns 
    6. gmx_mpi covar -s md.tpr -f md_center.xtc -o eigenval.xvg -tu ns 
    """
    def __init__(self, args, printf=print):
        super().__init__(args, printf)
        
    @staticmethod
    def make_args(args: argparse.ArgumentParser):
        args.add_argument('-d', '--dir', type=str,
                          help='directory to store the prepared files')
        args.add_argument('-n', '--main-name', type = str,
                          help='main name in each sub-directory, such as md.tpr.')
        args.add_argument('-cg', '--center-group', type = str, default='1',
                          help='group to center the trajectory, default is %(default)s.')
        args.add_argument('-rg', '--rms-group', type = str, default='4',
                          help='group to calculate rmsd, rmsf, and gyrate, default is %(default)s.')
        args.add_argument('-hg', '--hbond-group', type = str, default='1',
                          help='group to calculate hbond, default is %(default)s.')
        args.add_argument('-sg', '--sasa-group', type = str, default='4',
                          help='group to calculate sasa, default is %(default)s.')
        args.add_argument('-eg', '--eigenval-group', type = str, default='4',
                          help='group to calculate eigenval, default is %(default)s.')
        args.add_argument('-xmax', '--eigenval-xmax', type = int, default=15,
                          help='max value of eigenval, default is %(default)s.')
        return args

    @staticmethod
    def trjconv(gmx: Gromacs, main_name: str, center_group: str = '1', **kwargs):
        gmx.run_command_with_expect('trjconv', s=f'{main_name}.tpr', f=f'{main_name}.xtc', o=f'{main_name}_center.xtc', pbc='mol', center=True,
                                    expect_actions=[{'Select a group:': f'{center_group}\r', '\\timeout': f'{center_group}\r'},
                                                    {'Select a group:': '0\r', '\\timeout': '0\r'}],
                                    expect_settings={'timeout': 10}, **kwargs)
        
    @staticmethod
    def rms(gmx: Gromacs, main_name: str, group: str = '4', **kwargs):
        gmx.run_command_with_expect('rms', s=f'{main_name}.tpr', f=f'{main_name}_center.xtc', o=f'rmsd.xvg', tu='ns',
                                    expect_actions=[{'Select a group:': f'{group}\r', '\\timeout': f'{group}\r'},
                                                    {'Select a group:': f'{group}\r', '\\timeout': f'{group}\r'}],
                                    expect_settings={'timeout': 10}, **kwargs)
        os.system(f'cd "{gmx.working_dir}" && dit xvg_compare -c 1 -f rmsd.xvg -o rmsd.png -smv -t "RMSD of {main_name}" -csv {main_name}_rmsd.csv -ns')
        
    @staticmethod
    def rmsf(gmx: Gromacs, main_name: str, group: str = '4', res: bool = True, **kwargs):
        gmx.run_command_with_expect('rmsf', s=f'{main_name}.tpr', f=f'{main_name}_center.xtc', o=f'rmsf.xvg', res=res,
                                    expect_actions=[{'Select a group:': f'{group}\r', '\\timeout': f'{group}\r'}],
                                    expect_settings={'timeout': 10}, **kwargs)
        os.system(f'cd "{gmx.working_dir}" && dit xvg_compare -c 1 -f rmsf.xvg -o rmsf.png -t "RMSF of {main_name}" -csv {main_name}_rmsf.csv -ns')
        
    @staticmethod
    def gyrate(gmx: Gromacs, main_name: str, group: str = '4', **kwargs):
        gmx.run_command_with_expect('gyrate', s=f'{main_name}.tpr', f=f'{main_name}_center.xtc', o=f'gyrate.xvg',
                                    expect_actions=[{'Select a group:': f'{group}\r', '\\timeout': f'{group}\r'}],
                                    expect_settings={'timeout': 10}, **kwargs)
        os.system(f'cd "{gmx.working_dir}" && dit xvg_compare -c 1 -f gyrate.xvg -o gyrate.png -smv -t "Gyrate of {main_name}" -csv {main_name}_gyrate.csv -ns')
        
    @staticmethod
    def hbond(gmx: Gromacs, main_name: str, group: str = '1', dt=10, **kwargs):
        gmx.run_command_with_expect('hbond', s=f'{main_name}.tpr', f=f'{main_name}_center.xtc',
                                    num=f'{main_name}_hbond_num.xvg', dist=f'{main_name}_hbond_dist.xvg',
                                    expect_actions=[{'Select a group:': f'{group}\r', '\\timeout': f'{group}\r'},
                                                    {'Select a group:': f'{group}\r', '\\timeout': f'{group}\r'}],
                                    expect_settings={'timeout': 10}, **kwargs)
        os.system(f'cd "{gmx.working_dir}" && dit xvg_compare -c 1 -f {main_name}_hbond_num.xvg -o hbond_num.png -smv -t "H-bond num of {main_name}" -csv {main_name}_hbond_num.csv -ns')
        os.system(f'cd "{gmx.working_dir}" && dit xvg_show -f {main_name}_hbond_dist.xvg -o hbond_dist.png -ns')

    @staticmethod
    def sasa(gmx: Gromacs, main_name: str, group: str = '4', **kwargs):
        gmx.run_command_with_expect('sasa -or sasa_res.xvg', s=f'{main_name}.tpr', f=f'{main_name}_center.xtc',
                                    o=f'sasa_total.xvg', odg=f'sasa_dg.xvg', tv='sasa_tv.xvg', tu='ns',
                                    expect_actions=[{'>': f'{group}\r', '\\timeout': f'{group}\r'}],
                                    expect_settings={'timeout': 10}, **kwargs)
        for ty in ['total', 'res', 'dg', 'tv']:
            os.system(f'cd "{gmx.working_dir}" && dit xvg_compare -c 1 -f sasa_{ty}.xvg -o sasa_{ty}.png -smv -t "SASA {ty} of {main_name}" -csv {main_name}_sasa_{ty}.csv -ns')

    @staticmethod
    def covar(gmx: Gromacs, main_name: str, group: str = '4', xmax: int = 15, **kwargs):
        gmx.run_command_with_expect('covar', s=f'{main_name}.tpr', f=f'{main_name}_center.xtc', o=f'eigenval.xvg', tu='ns',
                                    expect_actions=[{'Select a group:': f'{group}\r', '\\timeout': f'{group}\r'},
                                                    {'Select a group:': f'{group}\r', '\\timeout': f'{group}\r'}],
                                    expect_settings={'timeout': 10}, **kwargs)
        os.system(f'cd "{gmx.working_dir}" && dit xvg_compare -c 1 -f eigenval.xvg -o eigenval.png -xmin 0 -xmax {xmax} -smv -t "Eigenval of {main_name}" -csv {main_name}_eigenval.csv -ns')
    
    @staticmethod
    def free_energy_landscape(gmx: Gromacs, main_name: str, **kwargs):
        os.system(f'cd "{gmx.working_dir}" && md-davis landscape_xvg -c -T 300 -x rmsd.xvg -y gyrate.xvg -o FEL.html -n FEL -l "RMSD-Rg" --axis_labels "dict(x=\'RMSD (in nm)\', y=\'Rg (in nm)\', z=\'Free Energy (kJ mol<sup>-1</sup>)<br>\')"')
    
    def process_args(self):
        self.args.dir = clean_path(self.args.dir)
        if not os.path.isdir(self.args.dir):
            put_err(f'dir argument should be a directory: {self.args.dir}, exit.', _exit=True)
        
    def main_process(self):
        # get complex paths
        complexs_path = get_paths_with_extension(self.args.dir, [], name_substr=self.args.main_name)
        put_log(f'get {len(complexs_path)} task(s)')
        # process each complex
        for complex_path in tqdm(complexs_path, total=len(complexs_path)):
            complex_path = Path(complex_path).resolve()
            gmx = Gromacs(working_dir=str(complex_path.parent))
            # perform trjconv
            self.trjconv(gmx, main_name=complex_path.stem, center_group=self.args.center_group)
            # perform analysis
            self.rms(gmx, main_name=complex_path.stem, group=self.args.rms_group)
            self.rmsf(gmx, main_name=complex_path.stem, group=self.args.rms_group)
            self.gyrate(gmx, main_name=complex_path.stem, group=self.args.rms_group)
            self.hbond(gmx, main_name=complex_path.stem, group=self.args.hbond_group)
            self.sasa(gmx, main_name=complex_path.stem, group=self.args.sasa_group)
            self.covar(gmx, main_name=complex_path.stem, group=self.args.eigenval_group, xmax=self.args.eigenval_xmax)
            # perform free energy landscape by MD-DaVis
            self.free_energy_landscape(gmx, main_name=complex_path.stem)
            
            
class mmpbsa(Command):
    HELP = """
    mmpbsa analysis for GROMACS simulation
    """
    def __init__(self, args, printf=print):
        super().__init__(args, printf)
        
    @staticmethod
    def make_args(args: argparse.ArgumentParser):
        args.add_argument('-d', '--dir', type=str,
                          help='directory to search files for tasks.')
        args.add_argument('-n', '--main-name', type = str,
                          help='main name in each sub-directory, such as md.tpr.')
        args.add_argument('-cg', '--cg', type = str, required=True,
                          help='Groups index for gmx_MMPBSA, default is %(default)s.')
        args.add_argument('-in', '--in', type = str, required=True,
                          help='gmx_MMPBSA input parameters file, such as mmpbsa.in.')
        args.add_argument('-np', '--np', type = int, default=0,
                          help='np parameter for mpirun, if 0, will call without mpirun, default is %(default)s.')
        return args


class interaction(simple_analysis):
    HELP = """
    interaction analysis for GROMACS simulation
    """
    def __init__(self, args, printf=print):
        super().__init__(args, printf)

    @staticmethod
    def make_args(args: argparse.ArgumentParser):
        args.add_argument('-bd', '--batch-dir', type = str, required=True,
                          help=f"dir which contains many sub-folders, each sub-folder contains docking result files.")
        args.add_argument('-top', '--topol-name', type = str, required=True,
                          help=f"topology file name in each sub-folder.")
        args.add_argument('-traj', '--traj-name', type = str, required=True,
                          help=f"trajectory file name in each sub-folder.")
        args.add_argument('--receptor-chain-name', type = str, required=True,
                          help='receptor chain name.')
        args.add_argument('--ligand-chain-name', type = str, required=True,
                          help='ligand chain name.')
        args.add_argument('--method', type = str, default='pymol', choices=['pymol', 'plip'],
                          help='interaction method, default is %(default)s.')
        args.add_argument('--mode', type = str, default='all',
                          help=f'interaction mode, multple modes can be separated by comma, all method support `\'all\'` model.\npymol: {",".join(pml_mode)}\nplip: {",".join(plip_mode)}')
        args.add_argument('--cutoff', type = float, default=4,
                          help='distance cutoff for interaction calculation, default is %(default)s.')
        args.add_argument('--hydrogen-atom-only', default=False, action='store_true',
                          help='only consider hydrogen bond acceptor and donor atoms, this only works when method is pymol, default is %(default)s.')
        args.add_argument('--output-style', type = str, default='receptor', choices=['receptor'],
                          help='output style\n receptor: resn resi distance')
        args.add_argument('--ref-res', type = str, default='',
                          help='reference residue name, input string shuld be like GLY300,ASP330, also support a text file contains this format string as a line.')
        args.add_argument('--n-workers', type=int, default=4,
                          help='number of workers to parallel. Default is %(default)s.')
        
    def main_process(self):
        # load origin dfs from data file
        if self.args.batch_dir:
            top_paths = get_paths_with_extension(self.args.batch_dir, name_substr=self.args.top_name)
            traj_paths = get_paths_with_extension(self.args.batch_dir, name_substr=self.args.traj_name)
            if len(top_paths) != len(traj_paths):
                r_roots = [os.path.dirname(p) for p in top_paths]
                l_roots = [os.path.dirname(p) for p in traj_paths]
                roots_count = {root: r_roots.count(root)+l_roots.count(root) for root in (set(r_roots) | set(l_roots))}
                invalid_roots = '\n'.join([root for root, count in roots_count.items() if count != 2])
                return put_err(f"The number of top and traj files is not equal, please check the input files.\ninvalid roots:{invalid_roots}")
            for r_path, l_path in zip(top_paths, traj_paths):
                self.tasks.append((r_path, l_path))
        # run tasks
        print(f'found {len(self.tasks)} tasks.')
        pool = TaskPool('process', self.args.n_workers).start()
        bar = tqdm(total=len(self.tasks), desc='Calculating interaction')
        for top_path, traj_path in self.tasks:
            bar.set_description(f"{wdir}: {os.path.basename(r_path)} and {os.path.basename(l_path)}")
            wdir = os.path.dirname(l_path)
            # load pdbstr from traj
            u = Universe(top_path, traj_path)
            self.calc_interaction_from_dlg(r_path, l_path, method, mode, self.args.cutoff,
                                           getattr(self, f'output_fromater_{self.args.output_style}'),
                                           self.args.hydrogen_atom_only, self.args.ref_res)
            bar.update(1)


_str2func = {
    'simple': simple,
    'mmpbsa': mmpbsa,
    'interaction': interaction,
}


def main(sys_args: List[str] = None):
    args_paser = argparse.ArgumentParser(description = 'tools for GROMACS analysis.')
    subparsers = args_paser.add_subparsers(title='subcommands', dest='sub_command')

    for k, v in _str2func.items():
        v.make_args(subparsers.add_parser(k, description=v.HELP))

    excute_command(args_paser, sys_args, _str2func)


if __name__ == '__main__':
    main()
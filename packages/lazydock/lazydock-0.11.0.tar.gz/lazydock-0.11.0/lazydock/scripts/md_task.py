'''
Date: 2025-02-01 11:07:08
LastEditors: BHM-Bob 2262029386@qq.com
LastEditTime: 2025-02-06 15:50:11
Description: 
'''
import argparse
import os
from pathlib import Path
from typing import Dict, List, Tuple, Union

import pandas as pd
from mbapy_lite.base import put_err, put_log
from mbapy_lite.file import get_paths_with_extension, opts_file
from mbapy.web_utils.task import TaskPool
from tqdm import tqdm

import numpy as np
import networkx as nx
import MDAnalysis as mda
from lazydock_md_task.scripts.calc_correlation import plot_map
from lazydock_md_task.scripts.contact_map_v2 import load_and_preprocess_traj, calculate_contacts, save_network_data, plot_network
from lazydock.scripts._script_utils_ import Command, clean_path, excute_command


def construct_graph(frame, atoms_inices: np.ndarray, threshold=6.7):
    # calculate distance matrix and build edges
    nodes = range(0, len(atoms_inices))
    dist = np.sqrt(np.sum((frame.positions[atoms_inices][:, None] - frame.positions[atoms_inices][None, :])**2, axis=-1))
    indices = np.where(dist < threshold)
    edges = list(filter(lambda x: x[0] < x[1], zip(indices[0], indices[1])))
    # build networkx graph
    protein_graph = nx.Graph()
    protein_graph.add_nodes_from(nodes)
    protein_graph.add_edges_from(edges)
    return protein_graph

def calcu_nextwork_from_frame(g):
    try:
        bc = nx.betweenness_centrality(g, normalized=False)
        bc = np.asarray(list(bc.values())).reshape(-1)
        path_dict = dict(nx.all_pairs_shortest_path_length(g))
        path = pd.DataFrame(path_dict).values
        return bc, path
    except Exception as ex:
        return put_err(f'Error calculating BC for frame: {ex}')


class network(Command):
    HELP = """
    network analysis for MD-TASK
    """
    def __init__(self, args, printf=print):
        super().__init__(args, printf)
        
    @staticmethod
    def make_args(args: argparse.ArgumentParser):
        args.add_argument('-d', '--dir', type=str, default='.',
                          help='directory to store the prepared files, default: %(default)s.')
        args.add_argument('-xtc', '--xtc-name', type = str, required=True,
                          help='trajectory file name in each sub-directory, such as center.xtc.')
        args.add_argument('-gro', '--gro-name', type = str, required=True,
                          help='gro file name for topology info in each sub-directory, such as md.gro.')
        args.add_argument("--ligand", type=str, default=None,
                          help="MDAnalysis atoms select expression to be included in the network, default: %(default)s")
        args.add_argument("--threshold", type=float, default=6.7,
                          help="Maximum distance threshold in Angstroms when constructing graph (default: %(default)s)")
        args.add_argument("--step", type=int, default=1,
                          help="Size of step when iterating through trajectory frames, default: %(default)s")
        args.add_argument('-mp', "--n-workers", type=int, default=4,
                          help="Number of workers to parallelize the calculation, default: %(default)s")
        return args

    def process_args(self):
        self.args.dir = clean_path(self.args.dir)
        if not os.path.isdir(self.args.dir):
            put_err(f'dir argument should be a directory: {self.args.dir}, exit.', _exit=True)
        self.paths = get_paths_with_extension(self.args.dir, [], name_substr=self.args.gro_name)
        if len(self.paths) == 0:
            put_err(f'No pdb files found in {self.args.dir}, exit.', _exit=True)
        self.pool = TaskPool('process', self.args.n_workers)
    
    def calcu_network(self, traj_path: Path, topol_path: Path):
        # prepare trajectory and topology
        u = mda.Universe(str(topol_path), str(traj_path))
        ligand = '' if self.args.ligand is None else f' or {self.args.ligand}'
        atoms = u.select_atoms("(name CB and protein) or (name CA and resname GLY)" + ligand)
        # prepare and run parallel calculation
        total_frames = len(u.trajectory) // self.args.step
        total_bc, total_dj_path = [None] * total_frames, [None] * total_frames
        for current, frame in enumerate(tqdm(u.trajectory[::self.args.step], total=total_frames)):
            pg = construct_graph(frame, atoms.indices, self.args.threshold)
            self.pool.add_task(current, calcu_nextwork_from_frame, pg)
            self.pool.wait_till(lambda: self.pool.count_waiting_tasks() == 0, 0)
        # gather results
        self.pool.wait_till(lambda: self.pool.count_done_tasks() == total_frames, 0)
        for i, (_, (bc, path), _) in self.pool.tasks.items():
            total_bc[i] = bc
            total_dj_path[i] = path
        self.pool.clear()
        total_bc = np.asarray(total_bc)
        total_dj_path = np.asarray(total_dj_path)
        # save outputs, float32 and int16 for saving space
        np.savez(f'{traj_path.stem}_network.npz', total_bc=total_bc.astype(np.float32),
                 total_dj_path=total_dj_path.astype(np.int16))
    
    def main_process(self):
        put_log(f'get {len(self.paths)} task(s)')
        self.pool.start()
        # process each complex
        for path in tqdm(self.paths, total=len(self.paths)):
            gro_path = Path(path).resolve()
            xtc_path = gro_path.parent / self.args.xtc_name
            if not xtc_path.exists():
                put_err(f'xtc file not found: {xtc_path}, skip.')
                continue
            self.calcu_network(xtc_path, gro_path)
        self.pool.close()
        
        
class correlation(network):
    HELP = """
    correlation analysis for MD-TASK
    """
    def __init__(self, args, printf=print):
        super().__init__(args, printf)
        
    def correlate(self, coords):
        # residues shape: (n_traj_frame, n_res, 3)
        n_traj, n_res, _ = coords.shape
        # centerlize coords for each residue
        mean = np.mean(coords, axis=0, keepdims=True)
        delta = coords - mean  # (n_traj, n_res, 3)
        # calculate magnitude for each residue
        dot_products = np.sum(delta ** 2, axis=2)  # (n_traj, n_res, 3) => (n_traj, n_res)
        mean_dots = np.mean(dot_products, axis=0)  # (n_traj, n_res) => (n_res,)
        magnitudes = np.sqrt(mean_dots)  # (n_res,)
        
        # 计算所有残基对的协方差矩阵
        # 使用einsum计算每个残基对在所有时间点的点积之和，再除以时间数得到平均值
        cov_matrix = np.einsum('tix,tjx->ij', delta, delta) / n_traj
        # calculate correlation matrix
        corr_matrix = cov_matrix / (magnitudes[:, None] * magnitudes[None, :])
        
        return corr_matrix
    
    def calcu_network(self, traj_path: Path, topol_path: Path):
        # prepare trajectory and topology
        u = mda.Universe(str(topol_path), str(traj_path))
        ligand = '' if self.args.ligand is None else f' or {self.args.ligand}'
        atoms = u.select_atoms("(name CA and protein)" + ligand)
        # extract coords
        total_frames = len(u.trajectory) // self.args.step
        coords = np.zeros((len(u.trajectory), len(atoms), 3), dtype=np.float64)
        for current, _ in enumerate(tqdm(u.trajectory[::self.args.step], total=total_frames)):
            coords[current] = atoms.positions
        # calculate correlation matrix and save, show
        sorted_residx = np.argsort(atoms.resids)
        corr_matrix = self.correlate(coords[:, sorted_residx, :])
        np.savez(f'{traj_path.stem}_corr_matrix.npz', corr_matrix=corr_matrix.astype(np.float32))
        plot_map(corr_matrix, traj_path.stem, traj_path.parent / f'{traj_path.stem}_corr_matrix')
     
        
class prs(network):
    HELP = """
    prs analysis for MD-TASK
    """
    def __init__(self, args, printf=print):
        super().__init__(args, printf)

    def calcu_network(self, traj_path: Path, topol_path: Path):
        raise NotImplementedError
        # prepare trajectory and topology
        u = mda.Universe(str(topol_path), str(traj_path))
        ligand = '' if self.args.ligand is None else f' or {self.args.ligand}'
        atoms = u.select_atoms("(name CA and protein)" + ligand)


class contact_map(network):
    HELP = """
    contact map analysis for MD-TASK
    """
    def __init__(self, args, printf=print):
        super().__init__(args, printf)
        
    @staticmethod
    def make_args(args: argparse.ArgumentParser):
        network.make_args(args)
        args.add_argument("--residue", type=str, required=True, help="traget residue name, such as LYS111")
        args.add_argument("--chain", type=str, default="A", help="traget residue chain, such as A, default: %(default)s.")
        args.add_argument("--nodesize", type=int, default=2900, help="node size in drawing, default: %(default)s.")
        args.add_argument("--nodefontsize", type=float, default=9.5, help="node font size in drawing, default: %(default)s.")
        args.add_argument("--edgewidthfactor", type=float, default=10.0, help="edge width factor in drawing, default: %(default)s.")
        args.add_argument("--edgelabelfontsize", type=float, default=8.0, help="edge label font size in drawing, default: %(default)s.")
        return args
    
    def process_args(self):
        super().process_args()
        self.args.residue = self.args.residue.upper()
        self.args.chain = self.args.chain.upper()
        self.prefix = self.args.residue.split(".")[0] if "." in self.args.residue else self.args.residue
        
    def calcu_network(self, traj_path: Path, topol_path: Path):
        # 1. load trajectory and topology
        traj = load_and_preprocess_traj(str(traj_path), str(topol_path), self.args.step)
        # 2. calculate contacts
        contacts, n_frames = calculate_contacts(
            traj, self.args.residue, self.args.chain, self.args.threshold/10
        )
        # 3. generate edges list
        center_node = f"{self.args.residue}.{self.args.chain}"
        edges_list = [[center_node, edge[1], count/n_frames] for edge, count in contacts.items()]
        # 4. create graph object
        contact_graph = nx.Graph()
        contact_graph.add_weighted_edges_from(edges_list)
        # 5. save output results
        output_csv = f"{self.prefix}_chain{self.args.chain}_network.csv"
        save_network_data(edges_list, output_csv)
        # 6. generate visualization graph
        output_png = f"{self.prefix}_chain{self.args.chain}_contact_map.png"
        plot_network(contact_graph, edges_list, output_png,
                     node_size=self.args.nodesize, node_fontsize=self.args.nodefontsize,
                     edgewidth_factor=self.args.edgewidthfactor, edgelabel_fontsize=self.args.edgelabelfontsize)


_str2func = {
    'network': network,
    'correlation': correlation,
    'contact-map': contact_map,
}


def main(sys_args: List[str] = None):
    args_paser = argparse.ArgumentParser(description = 'tools for GROMACS analysis.')
    subparsers = args_paser.add_subparsers(title='subcommands', dest='sub_command')

    for k, v in _str2func.items():
        v.make_args(subparsers.add_parser(k, description=v.HELP))

    excute_command(args_paser, sys_args, _str2func)


if __name__ == '__main__':
    # dev code
    
    main()
# Copyright 2022 Dechin Chen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import numpy as np
from .constants import hnames, hbond_type, RESIDUE_NAMES
from .parsers import read_pdb, gen_pdb


def rotate_by_axis(axis, theta):
    """Rotate an atom by a given axis with angle theta.
    Args:
        axis: The rotate axis.
        theta: The rotate angle.
    Returns:
        The rotate matrix.
    """
    vx, vy, vz = axis[0], axis[1], axis[2]
    return np.array([[vx * vx * (1 - np.cos(theta)) + np.cos(theta),
                      vx * vy * (1 - np.cos(theta)) - vz * np.sin(theta),
                      vx * vz * (1 - np.cos(theta)) + vy * np.sin(theta)],
                     [vx * vy * (1 - np.cos(theta)) + vz * np.sin(theta),
                      vy * vy * (1 - np.cos(theta)) + np.cos(theta),
                      vy * vz * (1 - np.cos(theta)) - vx * np.sin(theta)],
                     [vx * vz * (1 - np.cos(theta)) - vy * np.sin(theta),
                      vy * vz * (1 - np.cos(theta)) + vx * np.sin(theta),
                      vz * vz * (1 - np.cos(theta)) + np.cos(theta)]])


def add_h(crd, atype=None, i=None, j=None, k=None):
    """Add hydrogen once.
    Args:
        crd: The coordinates of all atoms.
        atype: Different types correspond to different addH algorithms.
        i: A label of input atom.
        j: A label of input atom.
        k: A label of input atom.
    Indexes:
        c6: Add one hydrogen at atom i. j and k atoms are connected to atom i.
    """
    if atype is None:
        raise ValueError('The type of AddH should not be None!')

    if atype != 'h2o' and i is None or j is None or k is None:
        raise ValueError('3 atom indexes are need.')

    if atype == 'c6':
        left_arrow = crd[j] - crd[i]
        left_arrow /= np.linalg.norm(left_arrow)
        right_arrow = crd[k] - crd[i]
        right_arrow /= np.linalg.norm(right_arrow)
        h_arrow = -1 * (left_arrow + right_arrow)
        h_arrow /= np.linalg.norm(h_arrow)
        return (h_arrow + crd[i])[None, :]

    if atype == 'dihedral':
        h_arrow = crd[j] - crd[k]
        h_arrow /= np.linalg.norm(h_arrow)
        return (h_arrow + crd[i])[None, :]

    if atype == 'c2h4':
        h_arrow_1 = crd[j] - crd[k]
        h1 = (h_arrow_1 / np.linalg.norm(h_arrow_1) + crd[i])[None, :]
        middle_arrow = (crd[i] - crd[j])
        middle_arrow /= np.linalg.norm(middle_arrow)
        middle_arrow *= np.linalg.norm(h_arrow_1)
        h_arrow_2 = -h_arrow_1 + middle_arrow
        h2 = (h_arrow_2 / np.linalg.norm(h_arrow_2) + crd[i])[None, :]
        return np.append(h1, h2, axis=0)

    if atype == 'ch3':
        upper_arrow = crd[k] - crd[j]
        upper_arrow /= np.linalg.norm(upper_arrow)
        h1 = -upper_arrow + crd[i]
        axes = crd[j] - crd[i]
        rotate_matrix = rotate_by_axis(axes, 2 * np.pi / 3)
        h2 = np.dot(rotate_matrix, h1 - crd[i])
        h2 /= np.linalg.norm(h2)
        h2 += crd[i]
        rotate_matrix = rotate_by_axis(axes, 4 * np.pi / 3)
        h3 = np.dot(rotate_matrix, h1 - crd[i])
        h3 /= np.linalg.norm(h3)
        h3 += crd[i]
        h12 = np.append(h1[None, :], h2[None, :], axis=0)
        return np.append(h12, h3[None, :], axis=0)

    if atype == 'cc3':
        h1 = crd[k]
        upper_arrow = crd[j] - crd[i]
        rotate_matrix = rotate_by_axis(upper_arrow, 2 * np.pi / 3)
        h2 = np.dot(rotate_matrix, h1 - crd[i])
        h2 /= np.linalg.norm(h2)
        return (h2 + crd[i])[None, :]

    if atype == 'c2h2':
        right_arrow = crd[k] - crd[i]
        rotate_matrix = rotate_by_axis(right_arrow, 2 * np.pi / 3)
        h1 = np.dot(rotate_matrix, crd[j] - crd[i])
        h2 = np.dot(rotate_matrix, h1)
        h1 /= np.linalg.norm(h1)
        h1 = (h1 + crd[i])[None, :]
        h2 /= np.linalg.norm(h2)
        h2 = (h2 + crd[i])[None, :]
        return np.append(h1, h2, axis=0)

    if atype == 'wat':
        h1 = np.array([0.79079641, 0.61207927, 0.0], np.float32) + crd[i]
        h2 = np.array([-0.79079641, 0.61207927, 0.0], np.float32) + crd[i]
        return np.append(h1[None, :], h2[None, :], axis=0)

    if atype == 'h2o':
        if i is None:
            raise ValueError('The index of O atom should be given.')


def AddHydrogen(pdb_in, pdb_out, lazy=False, no_resid=False):
    """ The API function for adding Hydrogen.
    Args:
        pdb_in(str): The input pdb file name, absolute file path is suggested.
        pdb_out(str): The output pdb file name, absolute file path is suggested.
    """
    # Record the time cost of Add Hydrogen.
    start_time = time.time()

    pdb_name = pdb_in
    new_pdb_name = pdb_out
    if lazy:
        pdb_obj = read_pdb(pdb_name, lazy=True, no_resid=no_resid)
    else:
        pdb_obj = read_pdb(pdb_name, ignoreh=True, lazy=False, no_resid=no_resid)
    
    chain_id = pdb_obj.chain_id
    chain_label = pdb_obj.atom_chain_label
    res_chain_label = pdb_obj.res_chain_label
    new_chain_label = []

    if lazy:
        crds = pdb_obj.flatten_crds
        atom_names = pdb_obj.flatten_atoms
        res_names = pdb_obj.init_res_names
        res_ids = pdb_obj.init_res_ids
        gen_pdb(crds, atom_names,
                res_names, res_ids, chain_id=chain_id,
                chain_label=chain_label, pdb_name=new_pdb_name, lazy=lazy)

        end_time = time.time()
        print(
            '1 lazy task with {} atoms complete in {} seconds.'.format(
                round(
                    len(crds), 3), round(
                    end_time - start_time, 3)))
        return 1

    crds = pdb_obj.crds
    atom_names = pdb_obj.atom_names
    res_names = pdb_obj.res_names
    is_amino = np.isin(res_names, RESIDUE_NAMES)

    for i, res in enumerate(res_names):
        if res == 'HIE':
            res_names[i] = 'HIS'
        if res == 'HOH':
            res_names[i] = 'WAT'
        if not is_amino[i]:
            continue
        if i == 0:
            res_names[i] = 'N' * (res != 'ACE') + res
            continue
        elif i == len(res_names) - 1:
            res_names[i] = 'C' * (res != 'NME') + res
            break
        if chain_id[i] < chain_id[i + 1]:
            res_names[i] = 'C' * (res != 'ACE') + res
        if chain_id[i] > chain_id[i - 1]:
            res_names[i] = 'N' * (res != 'ACE') + res

    for i, res in enumerate(res_names):
        h_names = []
        crds[i] = np.array(crds[i])
        if res == 'NME':
            c_index = np.where(np.array(atom_names[i - 1]) == 'C')
            atom_names[i].insert(0, 'C')
            crds[i] = np.append(crds[i - 1][c_index], crds[i], axis=-2)
        for atom in atom_names[i]:
            if atom == 'C' and len(res) == 4 and res.startswith(
                    'C') and np.isin(atom_names[i], 'OXT').sum() == 1:
                continue
            if atom in hbond_type[res].keys() and len(
                    hbond_type[res][atom].shape) == 1:
                addh_type = hbond_type[res][atom][0]
                for name in hnames[res][atom]:
                    h_names.append(name)
                try:
                    m = np.where(np.array(atom_names[i]) == [atom])[0][0]
                    n = np.where(
                        np.array(
                            atom_names[i]) == hbond_type[res][atom][1])[0][0]
                    o = np.where(
                        np.array(
                            atom_names[i]) == hbond_type[res][atom][2])[0][0]
                except IndexError:
                    raise ValueError('Some heavy atoms in residue {} are missing.'.format(res))
                new_crd = add_h(np.array(crds[i]), atype=addh_type, i=m, j=n, k=o)
                crds[i] = np.append(crds[i], new_crd, axis=0)
                new_chain_label.extend([res_chain_label[i]] * crds[i].shape[0])
            elif atom in hbond_type[res].keys():
                for j, hbond in enumerate(hbond_type[res][atom]):
                    addh_type = hbond[0]
                    h_names.append(hnames[res][atom][j])
                    try:
                        m = np.where(np.array(atom_names[i]) == [atom])[0][0]
                        n = np.where(np.array(atom_names[i]) == hbond[1])[0][0]
                        o = np.where(np.array(atom_names[i]) == hbond[2])[0][0]
                    except IndexError:
                        raise ValueError('Some heavy atoms in residue {} are missing.'.format(res))
                    new_crd = add_h(np.array(crds[i]), atype=addh_type, i=m, j=n, k=o)
                    crds[i] = np.append(crds[i], new_crd, axis=0)
                    new_chain_label.extend([res_chain_label[i]] * crds[i].shape[0])
            else:
                continue
        for name in h_names:
            atom_names[i].append(name)

        if res == 'NME':
            atom_names[i].pop(0)
            crds[i] = crds[i][1:]

    new_crds = crds[0]
    for crd in crds[1:]:
        new_crds = np.append(new_crds, crd, axis=0)

    new_atom_names = np.array(atom_names[0])
    for name in atom_names[1:]:
        new_atom_names = np.append(new_atom_names, name)

    new_res_names = []
    new_res_ids = []
    for i, crd in enumerate(crds):
        for _ in range(crd.shape[0]):
            new_res_names.append(res_names[i])
            new_res_ids.append(i + 1)
    new_res_ids = np.array(new_res_ids, np.int32)
    new_res_names = np.array(new_res_names, np.str_)
    new_chain_label = np.array(new_chain_label, np.str_)

    gen_pdb(new_crds, new_atom_names,
            new_res_names, new_res_ids, chain_id=chain_id,
            chain_label=new_chain_label, pdb_name=new_pdb_name, lazy=lazy)

    end_time = time.time()
    print(
        '1 H-Adding task with {} atoms complete in {} seconds.'.format(
            round(
                len(new_crds), 3), round(
                end_time - start_time, 3)))
    return 1

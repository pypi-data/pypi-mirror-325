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

import argparse
from hadder import AddHydrogen

parser = argparse.ArgumentParser()

parser.add_argument("-i", help="Set the input pdb file path.")
parser.add_argument("-o", help="Set the output pdb file path.")
parser.add_argument("-lazy", help="Ignore residues not recorded. Default: false", default='false')
parser.add_argument("-no_resid", help="Do not read the residue ID from input file. Default: false",
                    default='false')

args = parser.parse_args()
pdb_name = args.i
save_pdb_name = args.o
lazy_mode = args.lazy
no_resid = args.no_resid=='true'

if lazy_mode == 'false':
    AddHydrogen(pdb_name, save_pdb_name, lazy=False, no_resid=no_resid)
else:
    AddHydrogen(pdb_name, save_pdb_name, lazy=True, no_resid=no_resid)

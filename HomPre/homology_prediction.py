from modeller import *
from modeller.automodel import *

log.verbose()
envi = environ()

# Directories for input atom/pdb files
envi.io.atom_files_directory = ['.', '../atom_files']

a = automodel(envi, alnfile = 'alignment.ali', knowns = '4n9f', sequence = 'G1')

# Indices of first and last models (determines how many models to calculate)
a.starting_model = 1
a.ending_model = 1

# Compute comparative modeling
a.make()
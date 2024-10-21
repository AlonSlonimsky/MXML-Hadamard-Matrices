import numpy as np
from checkHadamardNP import *
from catalogueTradesNP import *

# Element to multiply with
c = -1

# The matrix (must be UH(n))
example = np.matrix([
    [1, 1, 1, 1],
    [1, 1j, -1, -1j],
    [1, -1, 1, -1],
    [1, -1j, -1, 1j]
])

# Copy the matrix to compare with the original
copy = example.copy()

# Output file
DEST = 'outputs/F_4_c_-1.txt'

# Clear the file
open(DEST, 'w').close()

catalogue_trades(example, c, 0, copy, DEST)
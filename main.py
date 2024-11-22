import numpy as np
from checkHadamardNP import *
from catalogueTradesNP import *

# Elements to multiply with
c: List[complex] = [EPS, EPS2, EPS3, EPS4]

c_map: dict = {}
curr_char: str = 'a'
for const in c:
    c_map[const] = curr_char
    curr_char = chr(ord(curr_char) + 1)

# The matrix (must be UH(n))
# Current example is using spectral matrix of order 6 (a BH(6,3))
# example: np.ndarray = np.array([
#     [1, 1, 1, 1, 1, 1],
#     [1, 1, GAM, GAM, GAM2, GAM2],
#     [1, GAM, 1, GAM2, GAM2, GAM],
#     [1, GAM, GAM2, 1, GAM, GAM2],
#     [1, GAM2, GAM2, GAM, 1, GAM],
#     [1, GAM2, GAM, GAM2, GAM, 1]

# ])

# example: np.ndarray = np.array([
#     [1, 1, 1, 1],
#     [1, 1j, -1, -1j],
#     [1, -1, 1, -1],
#     [1, -1j, -1, 1j]
# ])

example: np.ndarray = np.array([
    [1, 1, 1, 1, 1],
    [1, EPS, EPS2, EPS3, EPS4],
    [1, EPS2, EPS4, EPS, EPS3],
    [1, EPS3, EPS, EPS4, EPS2],
    [1, EPS4, EPS3, EPS2, EPS]
])

# Copy the matrix to compare with the original
copy: np.ndarray = example.copy()

# Output file
DEST: str = 'outputs/F_5.txt'

# Clear the file
open(DEST, 'w').close()

with open(DEST, 'a') as f:
    f.write("Cataloguing UH of size " + str(example.shape[0]) + ":\n")
    f.write("Constant appendix:\n")
    f.write("+ = 1\n")
    for const in c:
        f.write(c_map[const] + " = " + "{:.2f}".format(const) + "\n")
    f.write("\n")

catalogue_trades(example, c, DEST, c_map)
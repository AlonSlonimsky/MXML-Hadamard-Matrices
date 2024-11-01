import numpy as np
from checkHadamardNP import *
from catalogueTradesNP import *

# Elements to multiply with
c = [1j, -1, -1j]

c_map = {}
curr_char = 'a'
for const in c:
    c_map[const] = curr_char
    curr_char = chr(ord(curr_char) + 1)

# The matrix (must be UH(n))
example = np.matrix([
    [1+0j, 1+0j, 1+0j, 1+0j],
    [1+0j, 1j, -1+0j, -1j],
    [1+0j, -1+0j, 1+0j, -1+0j],
    [1+0j, -1j, -1+0j, 1j]
])

# example = np.matrix([
#     [1+0j, 1+0j, 1+0j],
#     [1+0j, GAM, GAM2],
#     [1+0j, GAM2, GAM]
# ])

# Copy the matrix to compare with the original
copy = example.copy()

# Output file
DEST = 'outputs/F_4.txt'

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
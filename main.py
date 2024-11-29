import numpy as np
from checkHadamardNP import *
from catalogueTradesNP import *

# Elements to multiply with
c: List[complex] = [ZET, GAM, -1, GAM2, ZET5]

c_map: dict = {}
curr_char: str = 'a'
for const in c:
    c_map[const] = curr_char
    curr_char = chr(ord(curr_char) + 1)

# The matrix (must be UH(n))
example = np.array([
    [1, 1, 1, 1, 1, 1, 1],
    [1, ZET, GAM2, ZET5, -1, -1, ZET],
    [1, GAM2, ZET, -1, ZET5, -1, ZET],
    [1, ZET5, -1, ZET, GAM2, ZET, -1],
    [1, -1, ZET5, GAM2, ZET, ZET, -1],
    [1, -1, -1, ZET, ZET, GAM2, ZET5],
    [1, ZET, ZET, -1, -1, ZET5, GAM2]
])

# Copy the matrix to compare with the original
copy: np.ndarray = example.copy()

# Output file
DEST: str = 'outputs/P_7.txt'

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

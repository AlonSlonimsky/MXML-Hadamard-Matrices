from checkHadamardNP import *
import numpy as np

def catalogue_trades(mat, c, index, copy, dest):
    n = mat.shape[0]
    if index == n * n:
        if is_hadamard(mat):
            comparison_mat = generate_comparison_matrix(mat, copy)
            with open(dest, 'a') as f:
                np.savetxt(f, mat, fmt='%.2f')
                f.write("\n")
                for row in comparison_mat:
                    f.write(' '.join(row) + '\n')
                f.write("\n")
        return
    
    curRow = index // n
    curCol = index % n
    
    # Try without multiplying
    catalogue_trades(mat, c, index + 1, copy, dest)
    
    # Try multiplying by c
    mat[curRow, curCol] *= c
    catalogue_trades(mat, c, index + 1, copy, dest)
    
    # Revert the change for backtracking
    mat[curRow, curCol] /= c

def generate_comparison_matrix(mat, original_mat):
    comparison_mat = np.full(mat.shape, 'o', dtype=str)
    count = 0
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            if not np.isclose(mat[r, c], original_mat[r, c]):
                comparison_mat[r, c] = 'x'
                count += 1
    if count < mat.shape[0] and count != 0:
        print("TRADE LESS THAN n DETECTED")
    return comparison_mat
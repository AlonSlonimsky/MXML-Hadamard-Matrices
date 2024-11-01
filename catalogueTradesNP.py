from checkHadamardNP import *
import numpy as np

def catalogue_trades(mat, c, dest, c_map):
    copy = mat.copy()
    hadamard_matrices = []
    catalogue_trades_helper(mat, c, 0, copy, dest, c_map, hadamard_matrices)
    hadamard_matrices.sort(key=lambda x: x[1])  # Sort based on the count value
    for hadamard_matrix in hadamard_matrices:
        write_output(hadamard_matrix[0], copy, c, c_map, hadamard_matrix[1], dest)

def catalogue_trades_helper(mat, c, index, copy, dest, c_map, hadamard_matrices, count=0):
    n = mat.shape[0]
    if index == n * n:
        if is_hadamard(mat):
            hadamard_matrices.append((mat.copy(), count))  # Store the matrix and count as a tuple
        return
    
    curRow = index // n
    curCol = index % n
    
    # Try without multiplying
    catalogue_trades_helper(mat, c, index + 1, copy, dest, c_map, hadamard_matrices, count)
    
    if (curRow > 0 and curCol > 0):
        for const in c:
            # Try multiplying by c
            mat[curRow, curCol] *= const
            catalogue_trades_helper(mat, c, index + 1, copy, dest, c_map, hadamard_matrices, count+1)
            
            # Revert the change for backtracking
            mat[curRow, curCol] /= const

def generate_comparison_matrix(mat, original_mat, constants, c_map):
    comparison_mat = np.full(mat.shape, 'o', dtype=str)
    count = 0
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            for const in constants:
                if np.isclose(mat[r, c], original_mat[r, c] * const):
                    comparison_mat[r, c] = c_map[const]
                    count += 1
                    break
    if count < mat.shape[0] and count != 0:
        print("TRADE LESS THAN n DETECTED")
    return comparison_mat

def generate_comparison_matrix_log(mat, original_mat, constants, c_map):
    comparison_mat = np.full(mat.shape, 'o', dtype=str)
    count = 0
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            for const in constants:
                if np.isclose(mat[r, c], original_mat[r, c] * const):
                    comparison_mat[r, c] = ord(c_map[const]) - ord('a') + 1
                    count += 1
                    break
    return comparison_mat

def format_matrix(mat, constants, c_map):
    formatted_mat = np.full(mat.shape, '+', dtype=str)
    count = 0
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            for const in constants:
                if np.isclose(mat[r, c], const):
                    formatted_mat[r, c] = c_map[const]
                    count += 1
                    break
    return formatted_mat

def format_matrix_log(mat, constants, c_map):
    formatted_mat = np.full(mat.shape, '0', dtype=str)
    count = 0
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            for const in constants:
                if np.isclose(mat[r, c], const):
                    formatted_mat[r, c] = ord(c_map[const]) - ord('a') + 1
                    count += 1
                    break
    return formatted_mat

def write_output(mat, copy, c, c_map, n, dest):
    formatted_mat = format_matrix(mat, c, c_map)
    formatted_mat_log = format_matrix_log(mat, c, c_map)
    comparison_mat = generate_comparison_matrix(mat, copy, c, c_map)
    comparison_mat_log = generate_comparison_matrix_log(mat, copy, c, c_map)
    with open(dest, 'a') as f:
        if (n == 0):
            f.write("Fourier matrix:\n")
        else:
            f.write("Switched matrix:\n")
        for row in formatted_mat:
            f.write(' '.join(row) + '\n')
        f.write("\n")
        f.write("Logarithmic form:\n")
        for row in formatted_mat_log:
            f.write(' '.join(row) + '\n')
        f.write("\n")
        if (n != 0):
            f.write("Switch matrix form:\n")
            for row in comparison_mat:
                f.write(' '.join(row) + '\n')
            f.write("\n")
            f.write("Switch matrix logarithmic form:\n")
            for row in comparison_mat_log:
                f.write(' '.join(row) + '\n')
            f.write("Trade size: " + str(n) + "\n")
        f.write("----------\n")
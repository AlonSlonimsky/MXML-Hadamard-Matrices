from checkHadamardNP import *
import numpy as np
from typing import List

def catalogue_trades(mat: np.ndarray, c: List[complex], dest: str, c_map: dict) -> None:
    """
    This function catalogues all possible trades in a given Hadamard matrix. 

    Args:
        mat (np.ndarray): The input Hadamard matrix.
        c (List[complex]): A list of constants to multiply by.
        dest (str): The path to the output file.
        c_map (dict): A dictionary mapping constants to their corresponding characters.

    Returns:
        None: This function does not return any value. It writes the results to the output file.

    """
    copy: np.ndarray = mat.copy()  # Create a copy of the matrix for comparison
    catalogue_trades_helper(mat, c, 0, copy, dest, c_map)  # Start the recursive helper function

def catalogue_trades_helper(mat: np.ndarray, c: List[complex], index: int, copy: np.ndarray, dest: str, c_map: dict, count: int = 0) -> None:
    """
    A recursive helper function for catalogue_trades that iterates through all possible combinations 
    of multiplying entries in the matrix by constants. 

    Args:
        mat (np.ndarray): The input Hadamard matrix.
        c (List[complex]): A list of constants to multiply by.
        index (int): The current index of the matrix being considered.
        copy (np.ndarray): A copy of the original matrix.
        dest (str): The path to the output file.
        c_map (dict): A dictionary mapping constants to their corresponding characters.
        count (int): The number of entries that have been multiplied by constants.

    Returns:
        None: This function does not return any value. It writes the results to the output file.

    """
    n: int = mat.shape[0]  # Get the size of the matrix (assuming it's a square matrix)
    if index == n * n:  # Base case: reached the end of the matrix
        if is_hadamard(mat):  # Check if the modified matrix is still a Hadamard matrix
            write_output(mat, copy, c, c_map, count, dest)  # Write the results to the output file
        return

    curRow: int = index // n  # Calculate the current row index
    curCol: int = index % n  # Calculate the current column index

    # Try without multiplying
    catalogue_trades_helper(mat, c, index + 1, copy, dest, c_map, count) 

    if (curRow > 0 and curCol > 0):  # Only try multiplying if the current entry is not the first row or column
        for const in c:
            # Try multiplying by each of the constant
            mat[curRow, curCol] *= const  # Multiply the entry by the constant
            catalogue_trades_helper(mat, c, index + 1, copy, dest, c_map, count+1)  # Recursively call the helper function
            
            mat[curRow, curCol] /= const  # Revert the multiplication for backtracking

def generate_comparison_matrix(mat: np.ndarray, original_mat: np.ndarray, constants: List[complex], c_map: dict) -> np.ndarray:
    """
    Generates a matrix that shows the differences between the original matrix and the modified matrix. 
    Entries that are the same are marked with 'o', while entries that are different are marked with the
    character corresponding to the constant used to multiply them.

    Args:
        mat (np.ndarray): The modified matrix.
        original_mat (np.ndarray): The original matrix.
        constants (List[complex]): A list of constants used for multiplication.
        c_map (dict): A dictionary mapping constants to their corresponding characters.

    Returns:
        np.ndarray: A matrix representing the comparison.
    """
    comparison_mat: np.ndarray = np.full(mat.shape, 'o', dtype=str)  # Create a matrix filled with 'o'
    count: int = 0
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

def generate_comparison_matrix_log(mat: np.ndarray, original_mat: np.ndarray, constants: List[complex], c_map: dict) -> np.ndarray:
    """
    Generates a comparison matrix in logarithmic form, representing the differences between the original 
    matrix and the modified matrix. Entries that are the same are marked with 'o', while entries that 
    are different are marked with a number corresponding to the constant used to multiply them. 

    Args:
        mat (np.ndarray): The modified matrix.
        original_mat (np.ndarray): The original matrix.
        constants (List[complex]): A list of constants used for multiplication.
        c_map (dict): A dictionary mapping constants to their corresponding characters.

    Returns:
        np.ndarray: A matrix representing the comparison in logarithmic form.
    """
    comparison_mat: np.ndarray = np.full(mat.shape, 'o', dtype=str)
    count: int = 0
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            for const in constants:
                if np.isclose(mat[r, c], original_mat[r, c] * const):
                    comparison_mat[r, c] = ord(c_map[const]) - ord('a') + 1
                    count += 1
                    break
    return comparison_mat

def format_matrix(mat: np.ndarray, constants: List[complex], c_map: dict) -> np.ndarray:
    """
    Formats the given matrix for output by replacing complex entries with their corresponding characters 
    based on the `c_map` dictionary.

    Args:
        mat (np.ndarray): The matrix to be formatted.
        constants (List[complex]): A list of constants used for multiplication.
        c_map (dict): A dictionary mapping constants to their corresponding characters.

    Returns:
        np.ndarray: A formatted matrix with characters representing complex numbers.
    """
    formatted_mat: np.ndarray = np.full(mat.shape, '+', dtype=str)
    count: int = 0
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            for const in constants:
                if np.isclose(mat[r, c], const):
                    formatted_mat[r, c] = c_map[const]
                    count += 1
                    break
    return formatted_mat

def format_matrix_log(mat: np.ndarray, constants: List[complex], c_map: dict) -> np.ndarray:
    """
    Formats the given matrix for output in logarithmic form by replacing complex entries with 
    a number corresponding to their position in the `constants` list.

    Args:
        mat (np.ndarray): The matrix to be formatted.
        constants (List[complex]): A list of constants used for multiplication.
        c_map (dict): A dictionary mapping constants to their corresponding characters.

    Returns:
        np.ndarray: A formatted matrix with numbers representing complex numbers.
    """
    formatted_mat: np.ndarray = np.full(mat.shape, '0', dtype=str)
    count: int = 0
    for r in range(mat.shape[0]):
        for c in range(mat.shape[1]):
            for const in constants:
                if np.isclose(mat[r, c], const):
                    formatted_mat[r, c] = ord(c_map[const]) - ord('a') + 1
                    count += 1
                    break
    return formatted_mat

def write_output(mat: np.ndarray, copy: np.ndarray, c: List[complex], c_map: dict, n: int, dest: str):
    """
    Writes the formatted output to a file. 

    Args:
        mat (np.ndarray): The modified matrix.
        copy (np.ndarray): The original matrix.
        c (List[complex]): A list of constants used for multiplication.
        c_map (dict): A dictionary mapping constants to their corresponding characters.
        n (int): The number of entries that have been multiplied by constants.
        dest (str): The path to the output file.

    Returns:
        None: This function does not return any value. It writes the results to the output file.

    """
    formatted_mat: np.ndarray = format_matrix(mat, c, c_map)
    formatted_mat_log: np.ndarray = format_matrix_log(mat, c, c_map)
    comparison_mat: np.ndarray = generate_comparison_matrix(mat, copy, c, c_map)
    comparison_mat_log: np.ndarray = generate_comparison_matrix_log(mat, copy, c, c_map)
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

# NOTE Sorted version, inefficient
# def catalogue_trades(mat, c, dest, c_map):
#     copy = mat.copy()
#     hadamard_matrices = []
#     catalogue_trades_helper(mat, c, 0, copy, dest, c_map, hadamard_matrices)
#     hadamard_matrices.sort(key=lambda x: x[1])  # Sort based on the count value
#     for hadamard_matrix in hadamard_matrices:
#         write_output(hadamard_matrix[0], copy, c, c_map, hadamard_matrix[1], dest)

# def catalogue_trades_helper(mat, c, index, copy, dest, c_map, hadamard_matrices, count=0):
#     n = mat.shape[0]
#     if index == n * n:
#         if is_hadamard(mat):
#             hadamard_matrices.append((mat.copy(), count))  # Store the matrix and count as a tuple
#         return
    
#     curRow = index // n
#     curCol = index % n
    
#     # Try without multiplying
#     catalogue_trades_helper(mat, c, index + 1, copy, dest, c_map, hadamard_matrices, count)
    
#     if (curRow > 0 and curCol > 0 and count < n):
#         for const in c:
#             # Try multiplying by c
#             mat[curRow, curCol] *= const
#             catalogue_trades_helper(mat, c, index + 1, copy, dest, c_map, hadamard_matrices, count+1)
            
#             # Revert the change for backtracking
#             mat[curRow, curCol] /= const
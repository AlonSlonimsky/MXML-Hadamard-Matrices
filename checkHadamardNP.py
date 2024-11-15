import numpy as np

GAM = np.exp(2j * np.pi / 3)
GAM2 = np.exp(4j * np.pi / 3)

EPS = np.exp(2j * np.pi / 5)
EPS2 = np.exp(4j * np.pi / 5)
EPS3 = np.exp(6j * np.pi / 5)
EPS4 = np.exp(8j * np.pi / 5)

def is_unit_modulus(matrix):
    """Check if all entries in the matrix have unit modulus (absolute value of 1)."""
    return np.allclose(np.abs(matrix), 1)

def is_pairwise_orthogonal(matrix):
    """Check if the columns of the matrix are pairwise orthogonal."""
    matrix_product = matrix @ matrix.T.conjugate()
    correct_diagonal = np.allclose(np.diag(matrix_product), matrix.shape[0])
    correct_off_diagonal = np.allclose(matrix_product - np.diag(np.diag(matrix_product)), 0)
    return correct_diagonal and correct_off_diagonal

def is_hadamard(matrix):
    return is_unit_modulus(matrix) and is_pairwise_orthogonal(matrix)
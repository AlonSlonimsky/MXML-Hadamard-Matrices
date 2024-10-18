import numpy as np

GAM = np.exp(2j * np.pi / 3)
GAM2 = np.exp(4j * np.pi / 3)

def is_unit_modulus(matrix):
    """Check if all entries in the matrix have unit modulus (absolute value of 1)."""
    return np.allclose(np.abs(matrix), 1)

def is_pairwise_orthogonal(matrix):
    """Check if the columns of the matrix are pairwise orthogonal."""
    return np.allclose(np.diag(matrix @ matrix.T.conjugate()), matrix.shape[0])

def is_hadamard(matrix):
    return is_unit_modulus(matrix) and is_pairwise_orthogonal(matrix)
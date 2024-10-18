import numpy as np

GAM = np.exp(1j * np.pi / 3)
GAM2 = np.exp(2j * np.pi / 3)


def is_unit_modulus(matrix):
    """Check if all entries in the matrix have unit modulus (absolute value of 1)."""
    for row in matrix:
        for entry in row:
            if not np.isclose(np.abs(entry), 1):
                return False
    return True


def check_orthogonality(matrix):
    """Check if the rows of the matrix are pairwise orthogonal using Hermitian inner product."""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Hermitian inner product
            inner_product = np.vdot(matrix[i], matrix[j])
            if i == j:  # Diagonal elements should have modulus n
                if not np.isclose(inner_product, n):
                    return False
            else:  # Off-diagonal elements should have modulus 0
                if not np.isclose(inner_product, 0):
                    return False
    return True


def is_complex_hadamard(matrix):
    """Check if a matrix is a complex Hadamard matrix."""
    if not is_unit_modulus(matrix):
        print("Matrix does not satisfy unit modulus condition.")
        return False
    if not check_orthogonality(matrix):
        print("Matrix rows are not orthogonal.")
        return False
    return True

import numpy as np

# Define constants for common roots of unity
GAM: complex = np.exp(2j * np.pi / 3)  # Cube root of unity
GAM2: complex = np.exp(4j * np.pi / 3)  # Another cube root of unity

EPS: complex = np.exp(2j * np.pi / 5)  # Fifth root of unity
EPS2: complex = np.exp(4j * np.pi / 5)
EPS3: complex = np.exp(6j * np.pi / 5)
EPS4: complex = np.exp(8j * np.pi / 5)

def is_unit_modulus(matrix: np.ndarray) -> bool:
    """Check if all entries in the matrix have unit modulus (absolute value of 1).
    This function uses NumPy's allclose function for efficient element-wise comparison.
    """
    return np.allclose(np.abs(matrix), 1)

def is_pairwise_orthogonal(matrix: np.ndarray) -> bool:
    """Check if the columns of the matrix are pairwise orthogonal.
    This function calculates the matrix product and checks for the appropriate diagonal
    and off-diagonal values.
    """
    matrix_product: np.ndarray = matrix @ matrix.T.conjugate()  # Matrix product
    # Check if the diagonal elements are equal to the matrix size
    correct_diagonal: bool = np.allclose(np.diag(matrix_product), matrix.shape[0])
    # Check if the off-diagonal elements are close to zero
    correct_off_diagonal: bool = np.allclose(
        matrix_product - np.diag(np.diag(matrix_product)), 0
    )
    return correct_diagonal and correct_off_diagonal  # Return True if both conditions are met

def is_hadamard(matrix: np.ndarray) -> bool:
    """Check if a given matrix is a Hadamard matrix.
    A matrix is Hadamard if it has unit modulus and its columns are pairwise orthogonal.
    """
    return is_unit_modulus(matrix) and is_pairwise_orthogonal(matrix)
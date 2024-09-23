from cmath import isclose
from typing import List

tolerance = 0.00005

#basic function to check if a given mxn matrix is a (real) hadamard matrix
def checkHadamard(mat: List[List[int]]) -> bool:
    numRows = len(mat)
    for i in range(numRows):
        mainRow = mat[i]
        for j in range(i+1, numRows):
            compareRow = mat[j]
            sum = 0
            for i in range(len(mainRow)):
                sum += mainRow[i] * (1/compareRow[i])
            if sum != 0:
                return False
    return True

#basic function to check if a given mxn matrix is a complex hadamard matrix
def checkComplexHadamard(mat: List[List[complex]]) -> bool:
    numRows = len(mat)
    for i in range(numRows):
        mainRow = mat[i]
        for j in range(i+1, numRows):
            compareRow = mat[j]
            sum = 0
            for i in range(len(mainRow)):
                sum += mainRow[i]/compareRow[i] #a*(b^-1)=a/b
            if not isclose(sum, 0, abs_tol=tolerance): #allow for small margin of error
                return False
    return True
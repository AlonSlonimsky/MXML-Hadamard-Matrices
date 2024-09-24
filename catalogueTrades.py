from copy import deepcopy
from math import sqrt
from checkHadamard import *
import time
import multiprocessing

x = complex(-1/2, sqrt(3)/2) #this is one of the cube roots of unity
y = x**2 #this is the other cube root of unity
foundCounterExample = False
matrixOrder = 6

#catalogue all possible trades in an mxn complex hadamard matrix 
def catalogueTradesCubeRoots(mat: List[List[complex]]) -> List:
    if not checkComplexHadamard(mat):
        print("Given Matrix is not a Complex Hadamard Matrix")
        return None
    
    for row in mat:
        for element in row:
            if not (isclose(element, x, abs_tol=tolerance)) and (not isclose(element, y, abs_tol=tolerance)) and (not isclose(element, 1, abs_tol=tolerance)):
                print("Matrix must only consist of cube roots of unity")
                return None
    
    #should be in a loop for larger operation sizes (4th/5th/6th/... roots of unity)
    #result = recursiveIteration(mat, 0, 0, 0)
    #print("1/3 done\n")
    #result += (recursiveIteration(mat, 0, 1, 0))
    #print("2/3 done\n")
    #result += (recursiveIteration(mat, 0, 2, 0))
    #print("3/3 done\n")
    
    result = []
    if __name__ == '__main__':
        with multiprocessing.Pool(processes = 3) as pool:
            result = pool.starmap(recursiveIteration, [(mat, 0, 0, 0), (mat, 0, 1, 0), (mat, 0, 2, 0)])
            pool.close()
            pool.join()
            result = result[0] + result[1] + result[2]
        
    
    
    return result
            
#operation == 0 means do nothing, 1 means times by x, 2 means times by x^2
def recursiveIteration(mat: List[List[complex]], index, operation, changes): 
    global foundCounterExample
    if foundCounterExample == True:
        return
    curRow = index//len(mat[0])
    curCol = index%len(mat[0])
    
    newMat = deepcopy(mat) #VERY INEFICIENT, THERE IS A BETTER WAY HERE
    
    match operation:
        case 0:
            pass
        case 1:
            newMat[curRow][curCol] *= x
            changes += 1
        case 2:
            newMat[curRow][curCol] *= y
            changes += 1
            
    result = []
    if checkComplexHadamard(newMat) and not operation == 0:
        result.append((newMat, changes))
        if changes < matrixOrder:
            foundCounterExample = True
            return result
         
    if changes > 6:
        return result            
    
    for newIndex in range(index+1, len(mat)*len(mat[0])):
        result += (recursiveIteration(newMat, newIndex, 0, changes))
        result += (recursiveIteration(newMat, newIndex, 1, changes))
        result += (recursiveIteration(newMat, newIndex, 2, changes))
            
    return result
    
def simplifyMatrixCubeRoots(mat: List[List[complex]]) -> List[List[str]]:
    for r, row in enumerate(mat):
        for c, num in enumerate(row):
            if isclose(num, 1, abs_tol=tolerance):
                mat[r][c] = "+"
            elif isclose(num, x, abs_tol=tolerance):
                mat[r][c] = "x"
            elif isclose(num, y, abs_tol=tolerance):
                mat[r][c] = "y"
            else:
                print("Invalid Element")
                return None
                        
    
start = time.time()    
#result = catalogueTradesCubeRoots([[1,1,1],[1,x,y],[1,y,x]]) #example
result = catalogueTradesCubeRoots([[1,1,1,1,1,1],[1,1,x,x,y,y],[1,x,1,y,y,x],[1,x,y,1,x,y],[1,y,y,x,1,x],[1,y,x,y,x,1]])
print("Finished Computing All Trades\n")

for (mat, changes) in result: #make the output look nice
    simplifyMatrixCubeRoots(mat)
    
result.sort(key = lambda x: x[1]) #sort by the size of the trade

with open('output.txt', 'w') as f:
    print("Total Possible Trades: ", len(result), "\n", file = f) 
    for (mat, changes) in result:
        for row in mat:
            print(str(row), "\n", file = f)
        print("Trade Size: ", changes, "\n", file = f)
        
end = time.time()
timeElapsed = end-start
print("Time Elapsed: ", timeElapsed, "seconds\n")
    
        
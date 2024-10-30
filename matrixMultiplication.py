from random import random

def randomListNumbers(n):
    lst = []
    for i in range(n):
        lst.append(round(random() * 100))
    return lst

def matrixEquals(mtz1, mtz2):
    if len(mtz1) != len(mtz2):
        return False
    for row1, row2 in zip(mtz1, mtz2):
        if len(row1) != len(row2):
            return False
    return True

def isSquareMatrix(mtz1):
    return len(mtz1) == len(mtz1[0])

def matrixMultiplication(mtz1, mtz2):
    if not matrixEquals(mtz1, mtz2) or not isSquareMatrix(mtz1):
        print("Las matrices no son iguales o no son cuadradas")
        return None
    
    size = len(mtz1)
    mtz3 = [[0] * size for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                mtz3[i][j] += mtz1[i][k] * mtz2[k][j]
    
    return mtz3

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:5}" for num in row)) 

matrix1 = [randomListNumbers(3), randomListNumbers(3), randomListNumbers(3)]
matrix2 = [randomListNumbers(3), randomListNumbers(3), randomListNumbers(3)]

print("Matrix 1:")
printMatrix(matrix1)
print("Matrix 2:")
printMatrix(matrix2)

if matrixEquals(matrix1, matrix2):
    result = matrixMultiplication(matrix1, matrix2)
    print("Resultado de la multiplicación de matrices:")
    printMatrix(result)
else:
    print("Las matrices no tienen el mismo tamaño.")

from random import random


def randomListNumbers(n):
    list = []
    for i in range(n):
        list.append(round(random() * 100))
    return list


matrix1 = [randomListNumbers(3), randomListNumbers(3), randomListNumbers(3)]
matrix2 = [randomListNumbers(3), randomListNumbers(3), randomListNumbers(3)]


print(matrix1)
print(matrix2)


def matrixMultiplication(mtz1, mtz2):
    mtz3 = []
    if len(mtz1) != len(mtz2):
        print("Matrices desiguales")

from random import random


def randomListNumbers(n):
    list = []
    for i in range(n):
        list.append(round(random() * 100))
    return list


def bubbleSort(listNumbers):
    listCopy = listNumbers.copy()
    for i in range(len(listCopy) - 2):
        for j in range(len(listCopy) - i - 2):
            if listCopy[j] > listCopy[j + 1]:
                listCopy[j], listCopy[j + 1] = listCopy[j + 1], listCopy[j]
    return listCopy


rlist = randomListNumbers(10)
print(f"Lista no ordenada, {rlist}")
print(f"Lista ordenada, {bubbleSort(rlist)}")

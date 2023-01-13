#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

"""
bir kare matrisi verilecek ve bunun 2 diyagonal ındaki sayıları ayrı ayrı toplayıp mutlak farkını döndüreceğimiz
bir fonksiyon yazalım 
"""

def diagonalDifference(arr):
    toplam1 = 0
    toplam2 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                toplam1 = arr[i][j] + toplam1
            if i + j == len(arr) - 1:
                toplam2 = arr[i][j] + toplam2

    return abs(toplam1 - toplam2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

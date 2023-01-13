#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
"""
10 luk tabanda verilen bir sayıyı önce 32 lik tabana çevirip sonra tersine çevirin (1 leri 0 0 ları 1 yaoın)
daha sonra bu sayıyı tekrar 10 luk tabana çevirin 


Çözüm sırasında gpt3 ten yararlanılmıştır 
"""
def flippingBits(n):
    binary_num = format(n, "032b")
    str_num = str(binary_num)
    flipped_binary = ''.join(['1' if i == '0' else '0' for i in str_num])
    decimal_num = int(flipped_binary, 2)
    return decimal_num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

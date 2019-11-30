# Solutions
==================================================

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

def diagonalDifference(arr):
    # Write your code here
    a=0;b=0;r=n-1
    for i in range(n):
        for j in range(n):
            if i==j:
                a+=arr[i][j]
    p=0
    while p<r:
        while r>=0:
            b+=arr[p][r]
            p+=1
            r-=1
    return abs(a-b)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

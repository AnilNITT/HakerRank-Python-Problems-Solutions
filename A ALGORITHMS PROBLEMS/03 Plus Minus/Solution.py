# Solution of Plus Minus problem
--------------------------------------------------

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n=len(arr)
    a=b=c=0
    for i in arr:
        if i>0:
            a+=1
        elif i<0:
            b+=1
        else:
            c+=1
    print('{:5f}'.format(a/n))
    print('{:5f}'.format(b/n))
    print('{:5f}'.format(c/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

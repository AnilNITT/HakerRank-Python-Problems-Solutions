# solution :
------------------------------------------------------------------------------

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    n=len(arr)
    arr.sort()
    a=b=0
    for i in range(n-1):
        a+=arr[i]
    for j in range(1,n):
        b+=arr[j]
    print(a,b)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

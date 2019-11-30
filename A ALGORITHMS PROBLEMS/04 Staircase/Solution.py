# Staircase solution
---------------------------------------------------------------------

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    p=n-1   # used for no of space

    # used for row
    for i in range(0,n):

        # used for space control
        for j in range(0,p):
            print(end=" ")
        p-=1   # everytime space decreased

        # used for print the symbol
        for r in range(0,i+1):
            print("#",end="")

        # for new row print
        print()
        
if __name__ == '__main__':
    n = int(input())

    staircase(n)

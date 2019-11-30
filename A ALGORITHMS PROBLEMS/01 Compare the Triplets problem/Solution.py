# Solution of the Compare the Triplets problem
========================================================================================

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
# Write ur code here
    count=0;count1=0
    for i in range(len(a)):
        for j in range(len(b)):
            if i==j:
                if a[i]>b[i]:
                    count+=1
                elif a[i]==b[i]:
                    continue
                else:
                    count1+=1
    return [count,count1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# solution
---------------------------------------------------------

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2:]=="AM" and s[:2]=="12":
        return "00"+s[2:-2]         # like "12:25:30AM"
    
    # remove "AM"
    elif s[-2:]=="AM":
        return s[:-2]             # like "01:50:56AM"

    elif s[-2:]=="PM" and s[:2]=="12":
        return s[:-2]             # like "12:43:12PM"

    else:
        # if "PM" thn add 12 hours and remove PM
        return str(int(s[:2])+12)+s[2:-2]      # [2:-2] or [2:8]

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

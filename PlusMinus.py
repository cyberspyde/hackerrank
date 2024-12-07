#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    null = 0
    size = len(arr)
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            null += 1

    print(f"{positive/size:.6f}\n {negative/size:.6f}\n {null/size:.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

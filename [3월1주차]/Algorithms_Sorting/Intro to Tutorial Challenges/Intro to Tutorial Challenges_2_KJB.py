#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(V):#def introTutorial(V,n,arr)해야 할것 같은데 V만 해도 잘 실행됩니당. 제가 한것과 v,n, arr 다 넣은것에 차이가 있나요?
    
    for i in range(n):
        if arr[i]==V:
            return i
             
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V)

    fptr.write(str(result) + '\n')

    fptr.close()

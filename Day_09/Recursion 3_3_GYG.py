![9](https://user-images.githubusercontent.com/56713634/72675449-8f948680-3ac7-11ea-97e3-b85ffc689e53.jpg)
https://wikidocs.net/22547
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n==1:
        return 1
    else: 
        return n*factorial(n-1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys


def number_sum():
    array = []
    for i in range(1,5):
        for j in range(1,5):

            value = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            
            array.append(value)
    ans = max(array)
    return ans
    




if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    result = number_sum()
    print(result)

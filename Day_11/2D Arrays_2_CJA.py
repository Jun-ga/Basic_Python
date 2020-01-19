#!/bin/python3

import math
import os
import random
import re
import sys


def hourglass_sum(arr, col, row):
    return sum(arr[row][col:col+3]) + arr[row+1][col+1] + sum(arr[row+2][col:col+3])

arr = []
for arr_i in range(6):
    arr_temp = [i for i in map(int, input().strip().split(' '))]
    arr.append(arr_temp)
rows = len(arr)
columns = len(arr[0])
sums = []
for i in range(columns - 2):
    for j in range(rows - 2):
        sums.append(hourglass_sum(arr, i, j))
print(sorted(sums)[-1])

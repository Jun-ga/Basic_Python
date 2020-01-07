#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    N = int(input())
    result = 'Weird'
    if not N % 2 == 0:
        result = 'Weird'
    elif N % 2 == 0 and 2 <= N <= 5:
        result = 'Not Weird'
    elif N % 2 == 0 and 6 <= N <= 20:
        result = 'Weird'
    elif 20 < N:
        result = 'Not Weird'
    print(result)

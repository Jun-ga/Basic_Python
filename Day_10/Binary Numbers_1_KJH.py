#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    count1, count2 = 0, 0

    while n != 0:
        factor = n // 2
        remainder = n - 2 * factor
        n = factor
        if remainder == 1:
            count1 += 1
            count2 = max(count2, count1)
        else:
            count1 = 0

print(count2)

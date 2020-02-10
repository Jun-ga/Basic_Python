#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s_1, s_2 = list(set(s1)), list(set(s2))
    l_1, l_2 = len(s_1), len(s_2)
    cnt = 0

    for i in range(l_1):
        for j in range(l_2):
            if s_1[i] == s_2[j]:
                cnt += 1
            else:
                pass

    if cnt >= 1:
        return('YES')
    else :
        return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

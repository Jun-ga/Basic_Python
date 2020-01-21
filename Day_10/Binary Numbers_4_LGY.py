import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    cnt = 0
    mx = 0
    while n > 0:
        if n%2 == 1:
            cnt += 1
            if cnt > mx: mx = cnt
        else: cnt = 0
        n //= 2
    print( mx )

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    print( " ".join(str(i) for i in arr) )

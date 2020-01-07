#!/bin/python3

import math
import os
import random
import re
import sys
#다시


n = int(input().strip()) 
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')] 
 
 
 
rarr = map(str, arr[::-1]) 
print(" ".join(rarr)) 

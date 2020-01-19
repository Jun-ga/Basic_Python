#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    n = int(input())
    0<n<101
    
    if n%2==1 or 6<n<21 :
        print("Weird")
    else :
         print("Not Weird")

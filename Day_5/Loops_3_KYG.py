#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for number in range(10):
        print(str(n) + ' x ' + str(number+1) + ' = ' + str(n*(number+1)))


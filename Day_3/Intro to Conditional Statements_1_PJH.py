#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if (1<=N)&(100>=N):
        if N%2!=0:
            print('Weird')
        elif((2<=N)&(5>=N)):
            print('Not Weird')
        elif(6<=N & N<=20):  
            print('Weird')
        elif(20<N):
            print('Not Weird')

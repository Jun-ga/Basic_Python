#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    Arr = list(arr) # 배열을 리스트했다는것은 어떤의미인지... 어떻게 표현되는지 궁금합니다.
    if Arr[n-i]< Arr[n-i-1]: # 3 < 8  3이 리스트는뒤에 있지만 숫자는 작으므로
        # Arr[n-i]리스트와 Arr[n-i-1] 리스트 자리바꾸기? switch
        #이렇게 하면 23468 한줄만 나올듯 
        2 4 6 8 8 
        2 4 6 6 8 
        2 4 4 6 8 
        2 3 4 6 8 이렇게 네줄 나와야하는데 
        수정해주시면 감사하겠습니다... 제 나름대로 짠건데 잘모르겠네요
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

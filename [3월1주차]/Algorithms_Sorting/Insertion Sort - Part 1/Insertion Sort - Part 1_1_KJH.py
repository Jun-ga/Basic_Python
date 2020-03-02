import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    Arr = list(arr)
    num = arr.pop()
    #print("num", num)
    for i in range(1,n+1):#1,n-1
        #print(i)
        com = Arr[n-i-1]#-1
        #print("com", com)
        
        if com > num:

            Arr[n-i] = com#-1
            if i == n:
            #print("i",i)
            #print(Arr[0])
            #print(num)
                if num < Arr[0]:
                #Arr[0]이 비교하는거보다 클때
                    Arr[0] = num
                    #print(" ".join(map(str, Arr)))
        else :
            Arr[n-i] = num
            print(" ".join(map(str, Arr)))
            break
        
        print(" ".join(map(str, Arr)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

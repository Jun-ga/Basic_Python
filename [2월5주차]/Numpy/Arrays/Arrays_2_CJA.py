import numpy

def arrays(arr):
    arr.reverse()
    arr_ = numpy.array(arr, float)
   
    return arr_

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

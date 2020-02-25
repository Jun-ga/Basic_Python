import numpy


def arrays(arr): #numpy를 의미하는거?
   
    return(numpy.array(arr[::-1], float))
   
#raw 는 string 그냥 input 쓰면
arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
#실행안됨 

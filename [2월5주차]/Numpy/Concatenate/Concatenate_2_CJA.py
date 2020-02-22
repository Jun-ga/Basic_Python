import numpy

N,M,P =  map(int,input().split())

arrA = []
arrB = []
for _ in range(N):
    arrA.append(list(map(int,input().split())))

for _ in range(M):
    arrB.append(list(map(int,input().split())))

arrA = numpy.array(arrA)
arrB = numpy.array(arrB)

print(numpy.concatenate((arrA,arrB), axis=0))

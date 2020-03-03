import numpy


N, M = map(int, input().split()) #M은 어디서 활용?N은 밑에줄에서 보이는데 M이 안보인다
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(A, axis=1), axis=0))

import numpy

#두번째 방법
N, M = map(int, input().split()) #M은 어디서 활용?N은 밑에줄에서 보이는데 M이 
안보인다
A = []
for i in range(N): #for _ in range(N)하면 왜 실행안되는지...
    B = list(map(int, input().split()))
    A.append(B)
print(numpy.max(numpy.min(A, axis=1), axis=0))




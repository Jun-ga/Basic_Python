import numpy as np

n,m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)



np.set_printoptions(legacy='1.13') #이것을 함으로써의 효과 궁금. 이거 안하면 실행안되던데
print(np.mean(b, axis = 1))
print(np.var(b, axis = 0))
print(np.std(b))

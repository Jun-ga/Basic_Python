import numpy as np
a, b, c = map(int,input().split())
arrA = np.array([input().split() for _ in range(a)],int)
arrB = np.array([input().split() for _ in range(b)],int)
print(np.concatenate((arrA, arrB), axis = 0))

#import numpy as np
#N, M, _ = [intx for i in input().strip().split()]
#a, b = map(lambda x: np.array([raw_input().strip().split() for i in xrange(int(x))], int), [N, M])
#print np.concatenate((a, b), axis = 0)

import numpy

mnp=input().split()
m=int(mnp[0])
n=int(mnp[1])
p=int(mnp[2])
f=[]
g=[]

for i in range(m):
    f.append(input().split())
    arr1=numpy.array(f,int)

for j in range(m,n+m):
    g.append(input().split())
    arr2=numpy.array(g,int)
    

print (numpy.concatenate((arr1,arr2),axis=0))

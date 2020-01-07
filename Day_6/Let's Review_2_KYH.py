i=int(input())
for T in range(i):
    S=input()    
    odd=""
    even=""
    for j in range(len(S)):
        if j%2==0:
            even+=S[j]
        if j%2==1:
            odd+=S[j] 
    print(even,odd)

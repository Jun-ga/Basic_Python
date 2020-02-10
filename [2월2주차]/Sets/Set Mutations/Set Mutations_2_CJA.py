N = int(input())
A = set(map(int,input().split()))

n = int(input())

for _ in range(n):
    s = list(input().split())
    B = set(map(int,input().split()))
    
    if s[0] == 'intersection_update': 
        A.intersection_update(B)
    if s[0] == "update":
        A.update(B)
    if s[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    if s[0] == 'difference_update':
        A.difference_update(B)
        
print(sum(A))

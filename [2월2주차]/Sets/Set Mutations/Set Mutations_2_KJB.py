An = int(input()) 
A = set(map(int, input().split())) 
n = int(input()) 

for i in range(n):
    name, size = input().split() #사이즈의 역할
    B = set(map(int, input().split()))
    if name == "intersection_update": 
        A.intersection_update(B)
    if name == "update":
        A.update(B)
    if name == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    if name == "difference_update":
        A.difference_update(B)

print(sum(A))

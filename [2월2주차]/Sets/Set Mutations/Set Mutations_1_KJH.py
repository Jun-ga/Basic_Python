An = int(input()) # 집합 A 요소 수
A = set(map(int, input().split())) # 집합 A
n = int(input()) 

for i in range(n):
    name, *size = input().split()
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

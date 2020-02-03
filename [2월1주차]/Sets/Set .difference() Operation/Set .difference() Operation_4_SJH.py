A_num = int(input())
A = set(map(int,input().split()))
B_num = int(input())
B = set(map(int,input().split()))

result = len(A.difference(B))
print(result)

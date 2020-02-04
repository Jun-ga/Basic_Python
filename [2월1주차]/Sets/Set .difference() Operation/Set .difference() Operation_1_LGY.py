A = int(input())
B = set(map(int, input().split()))
C = int(input())
D = set(map(int, input().split()))

print(len(B - D))

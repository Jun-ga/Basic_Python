k = int(input())
G = list(map(int, input().split()))
g = list(set(R))

C = (sum(g)*k-sum(G))/(k-1)

print (int(C))

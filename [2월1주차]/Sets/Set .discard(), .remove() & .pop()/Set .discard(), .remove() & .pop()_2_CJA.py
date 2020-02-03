n = int(input())
s = set(map(int, input().split()))

m = int(input())

for i in range(m):
    S = input().split()
    if S[0] == 'pop' :
        s.pop()

    elif S[0] == 'remove':
        s.remove(int(S[1]))
    
    elif S[0] == 'discard':
        s.discard(int(S[1]))

print(sum(s))

n = int(input())
s = set(map(int, input().split()))
t = int(input())

for i in range(t):

    a = list(input().strip().split())

    if a[0] == 'pop':
        s.pop()
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    else:
        s.remove(int(a[1]))

print(sum(s))

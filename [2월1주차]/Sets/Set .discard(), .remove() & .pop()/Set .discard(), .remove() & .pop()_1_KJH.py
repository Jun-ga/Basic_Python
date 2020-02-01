n = int(input())
s = set(map(int, input().split()))
k = int(input())

for _ in range(k):
    x = input().split(" ")
    cmd = x[0]
    if cmd == 'remove':
        s.remove(int(x[1]))
    if cmd == 'pop':
        s.pop()
    if cmd == 'discard':
        s.discard(int(x[1]))
    
print(sum(s))

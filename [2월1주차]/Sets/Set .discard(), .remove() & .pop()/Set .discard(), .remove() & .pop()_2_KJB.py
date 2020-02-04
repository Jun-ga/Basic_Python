
n = int(input())
s = set(map(int, input().split()))
number = int(input())
for _ in range(number):
    
    a = list(input().strip().split())

    
    if a == 'pop':
        s.pop()
    if a == 'remove':
        s.remove(int(a[1]))#
    if a == 'discard':
        s.discard(int(a[1]))#

print(sum(s))

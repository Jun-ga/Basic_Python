n = int(input())
s = set(map(int, input().split()))

case_num = int(input())

for i in range(case_num):
    l = input().split()
    case = l[0]
    
    if case == 'pop':
        s.pop()

    if case == 'remove':
        s.remove(int(l[1]))
    
    if case == 'discard':
        s.discard(int(l[1]))

print(sum(s))

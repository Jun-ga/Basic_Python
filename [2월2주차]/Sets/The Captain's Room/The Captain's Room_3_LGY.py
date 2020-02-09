# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
whole = list(map(int,input().split()))
count = [0 for i in range(max(whole)+1)]
for i in whole:
    count[i] += 1

for i in count:
    if i  == 1:
        print(count.index(i))
        
#위의 방법이 더 간단할 줄 알았는데 생각해보니 아래방법이 계산량이 적은거 같다.


_ = input()
a = input().split()
s = set()
t = set()
for i in a:
    if i not in s:
        s.add(i)
        t.add(i)
    else:
        t.discard(i)
print(t.pop())


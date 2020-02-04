n = int(input())
s = set()
for i in range(n):
    str = input()
    s.add(str)#set은 중복을 허용하지 않음
print(len(s))

# Enter your code here. Read input from STDIN. Print output to STDOUT

T=int(input())
for j in range(T):
    S=input()
    even,odd=S[::2], S[1::2]
    print(even + ' ' + odd)

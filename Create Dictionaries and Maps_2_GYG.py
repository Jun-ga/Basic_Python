n = int(input())
Contact = {}
for i in range(n):
    number = input().split()
    Contact[number[0]] = number[1]
    
for i in range(n):
    find_name = input()
    result = find_name + '=' + Contact[find_name] if find_name in Contact else 'Not found'
    print(result)

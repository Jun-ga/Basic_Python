![8](https://user-images.githubusercontent.com/56713634/72675423-2f9de000-3ac7-11ea-873f-6014ab2c3deb.jpg)
https://wikidocs.net/16
n = int(input())
Contact = {}
for i in range(n):
    number = input().split()
    Contact[number[0]] = number[1]
    
for i in range(n):
    find_name = input()
    result = find_name + '=' + Contact[find_name] if find_name in Contact else 'Not found'
    print(result)

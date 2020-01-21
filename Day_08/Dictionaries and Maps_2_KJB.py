n = int(input())
phonebook = {}
for _ in range(n):
    name, phonenumber = input().split()
    phonebook[name] = phonenumber
while True:
    try:
        query = input()
    except:
        break
    if query in phonebook:
        print( query + "=" + phonebook[query] )
    else:
        print( "Not found" )

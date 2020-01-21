n=int(input())
phoneBook={}

for _ in range(n):
    name, number = input().split()
    phoneBook[name]=number

for _ in range(n):
    name=input()

    if name in phoneBook:
        number=phoneBook[name]
        print (name+"="+ number)
    else:
        print ("Not found")

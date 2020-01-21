#Runtime Error_case1
 
N = int(input()) 
d = {}

for _ in range(0, N): 
    name, number = input().split()
    d[name] = number

arr = d.keys()
#print(arr)


for _ in range(0, N): 
    name_ = input() 
    if name_ not in arr: 
        print("Not found")
    else: 
        print("{}={}".format(name_, d[name_])) 

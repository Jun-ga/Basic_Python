if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    x = max(arr)
    arr.remove(x)
    y = max(arr)
    while x==y :
    
        arr.remove(x)
        y = max(arr)
        
    c = max(arr)
    

    print(c)


if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split()
        a = x[0]
        if a == 'append':
            result.append(int(x[1]))
        if a == 'print':
            print(result)
        if a == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if a == 'reverse':
            result = result[::-1]
        if a == 'pop':
            result.pop()
        if a == 'sort':
            result = sorted(result)
        if a == 'remove':
            result.remove(int(x[1]))
            

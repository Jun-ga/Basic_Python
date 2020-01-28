if __name__ == '__main__':
    N = int(input())
    result = []

    for _ in range(N):
        x= input().split(' ')
        a = x[0] #물음

        if a == 'insert': # 물음
            result.insert(int(x[1]), int(x[2])) #물음

        if a == 'print':
            print(result)

        if a == 'remove': 
            result.remove(int(x[1]))

        if a == 'append': 
            result.append(int(x[1]))

        if a == 'sort':
            result.sort()

        if a == 'pop': 
            result.pop()

        if a == 'reverse': 
            result.reverse()


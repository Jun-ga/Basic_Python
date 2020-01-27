if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = []

    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if a+b+c != n:
                    result.append([a,b,c])

    print([*result]) # 왜 []를 넣으니까 자동으로 ,(콤마)가 생기는지는 모르겠다.

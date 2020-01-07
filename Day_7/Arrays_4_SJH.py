if __name__ == '__main__':
    n = int(input()) # 입력을 int로 받음.
    
    arr = list(map(int, input().rstrip().split()))
    
    arr.reverse() # reverse 함수는 리스트를 역순으로 뒤집어준다.
    
    for n in arr:            
        print(n, end=' ')

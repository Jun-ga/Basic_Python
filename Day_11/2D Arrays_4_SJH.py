def hourglass():
    array_sum = [] # 각 모레시계 합을 저장하기 위해 만든 리스트.

    for i in range(1,5): # arr 리스트의 행과 열을 따로 고려해야 하므로 for 문을 2개 사용한다.
        for j in range(1,5):
            value = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            
            array_sum.append(value)

    ans = max(array_sum)
    return ans
    
if __name__ == '__main__':
    arr = [] # 각 경우에 따라 주어질 6X6 형태의 리스트 ( => 6X6 2D Array, A )

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
                
    result = hourglass()
    print(result)

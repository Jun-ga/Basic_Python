
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    mx = -100
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            sm = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] \
                + arr[i][j] \
                + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if( sm > mx ): mx = sm
    print( mx )

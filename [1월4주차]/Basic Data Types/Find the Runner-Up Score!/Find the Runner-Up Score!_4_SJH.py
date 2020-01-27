if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) # arr을 리스트로 만들기
    arr_max_number = max(arr) # arr 리스트에서 가장 큰 수

    result = []
    for i in range(n):
        if arr[i] != arr_max_number:
            result.append(arr[i])

    print(max(result))

'''
    # 오류
    for i in range(n):
        if arr[i] == arr_max_number:
            del arr[i]
'''

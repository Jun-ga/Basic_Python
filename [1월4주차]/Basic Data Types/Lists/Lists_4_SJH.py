if __name__ == '__main__':
    N = int(input())
    result = []

    for _ in range(N):
        case = input().split(' ')
        case_name = case[0]

        if case_name == 'insert': # (a, b) : a번째 인덱스에 b요소를 추가한다.
            result.insert(int(case[1]), int(case[2]))

        if case_name == 'print':
            print(result)

        if case_name == 'remove': # ()안의 요소를 삭제한다.
            result.remove(int(case[1]))

        if case_name == 'append': # ()안의 요소를 리스트 맨 끝에 추가한다.
            result.append(int(case[1]))

        if case_name == 'sort': # 오름차순 정렬
            result.sort()

        if case_name == 'pop': # 리스트 맨 끝의 요소를 삭제한다.
            result.pop()

        if case_name == 'reverse': # 리스트 요소 순서를 반전 시켜준다.
            result.reverse()

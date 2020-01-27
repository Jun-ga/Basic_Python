def merge_the_tools(string, k):
    n = len(string)
    out = int(n/k)

    for i in range(out):
        slicing = string[k*i:k*(i+1)] # 문자열 슬라이싱
        
        result = []
        
        for j in range(len(slicing)):
            if slicing[j] in result:
                pass
            else:
                result.append(slicing[j])

        print(''.join(result)) # join을 사용하여 리스트를 문자열로 변환

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

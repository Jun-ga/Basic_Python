def merge_the_tools(string, k):
    n = len(string)

    for i in range(0, n, k):
        m = string[i:i+k]
        M = []
        
        for j in range(len(m)):
            if m[j] not in M:
                M.append(m[j])

        print("".join(M))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

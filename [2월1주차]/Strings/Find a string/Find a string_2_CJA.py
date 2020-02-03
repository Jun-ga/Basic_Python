def count_substring(string, sub_string):
    cnt = 0
    n = len(string)
    m = len(sub_string)
    for i in range(n-m+1):
        s = ''
        s = string[i : i+m]
        if s == sub_string:
            cnt += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

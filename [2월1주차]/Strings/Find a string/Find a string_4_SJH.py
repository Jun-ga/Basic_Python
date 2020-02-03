def count_substring(string, sub_string):
    st = list(string)
    sub_st = list(sub_string)
    count = 0

    for i in range(0,len(st)): 
        a = st[i:i+len(sub_st)]
        if a == sub_st:
            count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

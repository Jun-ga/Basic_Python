def count_substring(string, sub_string):
    ans=0
    for i in range (len(string)-2):
        if sub_string in string[i:i+len(sub_string)]:
            ans+=1
    return ans

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

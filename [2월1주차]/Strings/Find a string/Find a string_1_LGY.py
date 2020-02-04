def count_substring(string, sub_string):
    length = len(string)
    sub_length = len(sub_string)
    number = 0
    for i in range(length-sub_length+1):
        if string[i:i+sub_length] == sub_string:
            number += 1
    return number

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

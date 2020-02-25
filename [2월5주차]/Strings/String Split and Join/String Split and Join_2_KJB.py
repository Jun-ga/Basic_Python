def split_and_join(line):#밑에   
    # write your code here
    
    print "-".join(raw_input().split())


if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result

def split_and_join(line):
    A = line.split(' ')
    res = "-".join(A)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

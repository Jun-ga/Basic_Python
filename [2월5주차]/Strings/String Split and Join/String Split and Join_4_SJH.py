def split_and_join(line):
    line_ = line.split(" ")
    return "-".join(line_)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

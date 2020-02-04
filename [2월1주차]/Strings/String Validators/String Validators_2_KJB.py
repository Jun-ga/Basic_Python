if __name__ == '__main__':
    s = input()

    print(any(map(str.isalnum, s))) #map이 각각 하니씩 요소로 나누어져 적용시키는것
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))

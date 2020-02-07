def mutate_string(s, p, c):
    return s[:p] + c + s[p+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

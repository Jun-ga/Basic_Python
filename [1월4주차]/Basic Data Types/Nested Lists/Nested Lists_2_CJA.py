if __name__ == '__main__':
    list_d = []
    list_s = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        list_d += [[name,score]]
        list_s += [score]

    list_d.sort()
    A = sorted(list(set(list_s)))

    for a,b in list_d:
        if b == A[1]:
            print(a)

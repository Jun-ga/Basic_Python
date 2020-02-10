import os

def twoStrings(s1, s2):
    s1_, s2_ = list(set(s1)), list(set(s2))
    pair = []

    for i in s1_:
        for j in s2_:
            if i == j:
                pair.append(i)

    if len(pair) != 0: return('YES')
    else: return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

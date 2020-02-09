#Mutation 변화

def mutate_string(string, position, character):
    list_string = list(string)

    list_string[position] = character
    
    ans = ''.join(list_string)
    return ans

# S는 문자열, i, c도 문자열 position은 정수형.
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

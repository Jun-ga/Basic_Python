def minion_game(string):
    vowel = ['A','E','I','O','U']
    S_count = 0
    K_count = 0

    for i in range(len(string)):
        if string[i] in vowel: K_count += len(string) - i
        else: S_count += len(string) - i
            
    if S_count > K_count: print("Stuart", S_count)
    elif K_count > S_count: print("Kevin", K_count)
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

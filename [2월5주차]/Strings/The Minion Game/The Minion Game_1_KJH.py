def minion_game(string): # BANANA
    stuart, kevin = 0,0 
    n=len(string)

    for i in range(n):
        if string[i] in 'AEIOU': kevin += n - i
        else: stuart += n - i

    if kevin > stuart: print ('Kevin', kevin)
    elif stuart > kevin: print ('Stuart', stuart)
    else: print ('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

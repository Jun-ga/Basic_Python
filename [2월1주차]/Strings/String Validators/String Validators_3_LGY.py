if __name__ == '__main__':
    s = input()
    p = [0, 0, 0, 0, 0]
    for i in s:
        if i.isalnum() == True:
            p[0] = 1
        if i.isalpha() == True:
            p[1] = 1
        if i.isdigit() == True:
            p[2] = 1
        if i.islower() == True:
            p[3] = 1
        if i.isupper() == True:
            p[4] = 1
    
    for a in p:
        if a == 1:
            print('True')
        else :
            print('False')


    



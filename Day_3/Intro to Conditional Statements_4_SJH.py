if __name__ == '__main__':
    N = int(input())
    
    if N % 2 == 1:
        print('Weird') 

    else:
        if 2 <= N <= 5 or N > 20:
            print('Not Weird')

        else:
            print('Weird')

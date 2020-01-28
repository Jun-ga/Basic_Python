if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
'''
if __name__ == '__main__':
    n = int(input())
    print(hash(tuple(map(int, input().split())))) '''

# Enter your code here. Read input from STDIN. Print output to STDOUT
def method(A):
    name, size = input().split()
    other = set(map(int, input().split()))

    if(name == "intersection_update"):
        A.intersection_update(other)
    if(name == "update"):
        A.update(other)
    if(name == "symmetric_difference_update"):
        A.symmetric_difference_update(other)
    if(name == "difference_update"):
        A.difference_update(other)



if __name__ == '__main__':
    size = int(input())
    A = set(map(int, input().split()))
    N = int(input())

    for i in range(N):
        method(A)
        
    print(sum(A))

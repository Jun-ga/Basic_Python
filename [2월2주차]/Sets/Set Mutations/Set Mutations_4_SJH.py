A_number = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N): 
    case, size = input().split()
    B = set(map(int, input().split()))

    if case == 'intersection_update': A.intersection_update(B)

    if case == 'update': A.update(B)

    if case == 'symmetric_difference_update': A.symmetric_difference_update(B)

    if case == 'difference_update': A.difference_update(B)

print(sum(A))

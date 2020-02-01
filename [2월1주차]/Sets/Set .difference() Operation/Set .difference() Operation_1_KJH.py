E_num = int(input())
E_engaged = set(map(int, input().split()))
F_num = int(input())
F_engaged = set(map(int, input().split()))

print(len(E_engaged - F_engaged))

from collections import Counter

K = int(input())
guest = list(map(int, input().split()))

#1
ans = Counter(guest)
print(sorted(ans.items(), key=lambda x:x[1])[0][0])

#2
# room={}
# for num in guest:
#     try: room[num] += 1
#     except: room[num] =1
# print(sorted(room.items(), key=lambda x:x[1])[0][0])

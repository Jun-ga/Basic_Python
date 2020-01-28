def merge_the_tools(string, k):
    
    batch = int(len(string)/k)
    a = list(string)
    
    for i in range(batch):
        like_set = []
        part1 = a[:k]
        
        for i in range(k):
            if part1[i] in like_set: # 중복된게 있으면
                continue # 그냥 넘어감.
            else: #중복된 게 없으면
                like_set.append(part1[i]) #리스트에 추가
        
        print("".join(like_set)) #띄어쓰기 없애려고
        del a[:k] #한건 지우기


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

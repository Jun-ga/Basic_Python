if __name__ == '__main__':
    dic = {}
    for i in range(int(input())):
        
        name = input()
        
        score = float(input())
        dic[name] = score
    
    scores = dic.values()
    
    Scores = list(set(scores))
    
    Scores.sort()
    

    Q = Scores[1]
   
    ans = []
    for na, sc in dic.items():
        
        if sc == Q:
            ans.append(na)
            answer = sorted(ans)
            
    for i in answer:
        print(i)

   

def minion_game(string):
    S = list(s)
    kevin = 0
    stuart = 0
    N = len(S)
    for j in range(N):
        for i in range(N-j):
            
            L = S[:i+1]
            
            if L[0] in ['A','E','I','O','U'] :
                kevin += 1
            else:
                stuart += 1
        
        del S[0]
   
        
    if kevin == stuart:
        print("Draw")
        return 0
    
    high =  max(kevin, stuart)
    if high == kevin:
        print("Kevin", high)
    else:
        print("Stuart", high)
    
    
  

if __name__ == '__main__':
    s = input()
    minion_game(s)

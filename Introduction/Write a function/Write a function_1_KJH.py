def is_leap(year):
    leap = False
    
    a=year%4
    b=year/4

    #print(a,b)

    if year%400==0:
        leap=True
    elif a!=0 or b%25==0:
        leap=False
    else:
        leap=True
        
    
    
    return leap

year = int(input())
print(is_leap(year))

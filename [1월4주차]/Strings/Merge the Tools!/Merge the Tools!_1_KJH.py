def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    a_=[]
    for i in range(n//k):
        a_ = string[k*i:k*(i+1)]
        result=list()
        for A in a_:
            if result.count(A)<1:
                result.append(A)
        print("".join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

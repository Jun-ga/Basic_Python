def merge_the_tools(string, k): #해석
    n = len(string)
    p = int(k/n)

    for i in range(0, n, k): #해석
        l = string[i:i+k]
        #??
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

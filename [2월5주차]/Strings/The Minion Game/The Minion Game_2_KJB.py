def minion_game(string):
    s = raw_input()

vowels = 'AEIOU'


for i in range(len(s)):
    if s[i] in vowels:
        K += (len(s)-i) #쓰는방식이 맞나...
    else:
        S += (len(s)-i)

if K > S:
    print "Kevin"
elif K < S:
    print "Stuart"
else:
    print "Draw"
    # your code goes here

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)

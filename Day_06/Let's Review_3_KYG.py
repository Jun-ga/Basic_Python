# Enter your code here. Read input from STDIN. Print output to STDOUT

test_case_count = int(input())
test_case_input = []
for test_case_index in range(test_case_count):
    current_word = input()
    odd_string = ''
    even_string = ''
    for string_index in range(len(current_word)):
        if not string_index % 2 == 0:
            even_string = even_string + current_word[string_index]
        else:
            odd_string = odd_string + current_word[string_index]
    print(odd_string + ' ' + even_string)


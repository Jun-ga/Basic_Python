if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    want_mark_score = student_marks[query_name]
    # print(want_mark_score)
    
    average_score = sum(want_mark_score) / 3
    print('%.2f' % average_score)

if __name__ == '__main__':
    student_score =[]
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        student_score.append([name,score])
        scores.append(score)
    
    second_score = sorted(list(set(scores)))[1]
    if score == second_score :
        sort(name)???
    #알파벳 정렬

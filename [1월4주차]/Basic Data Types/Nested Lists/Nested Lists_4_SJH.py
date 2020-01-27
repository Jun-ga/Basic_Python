if __name__ == '__main__':
    name_score_list = []
    score_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score_list.append([name,score])
        score_list.append(score)

    second_score = sorted(list(set(score_list)))[1]

    for name_,score_ in sorted(name_score_list): # 알파벳순으로 출력하기 위해 sorted 사용
        if score_ == second_score:
            print(name_)

# raw_scores = input("Enter scores: ")
raw_scores = input("Enter score: ")
scores_split = raw_scores.split(" ")
scores_list = [int(i) for i in scores_split]

best = max(scores_list)

for score in scores_list:
    if score >= best - 10:
        grade = "A"
        student_num = scores_list.index(score)
    elif score >= best - 20 and score < best - 10:
        grade = "B"
        student_num = scores_list.index(score)
    elif score >= best - 30 and score < best - 20:
        grade = "C"
        student_num = scores_list.index(score)
    elif score >= best - 40 and score < best - 30:
        grade = "D"
        student_num = scores_list.index(score)
    else:
        grade = "F"
        student_num = scores_list.index(score)
    print(f"Student {student_num} score is {score} and grade is {grade}")

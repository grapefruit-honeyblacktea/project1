def my_point(hfdd):
    combo_score = 0
    current_score = 0
    for ox in hfdd:
        if ox == "o":
            combo_score += 1
        else:
            combo_score = 0
        current_score += combo_score
    return current_score

test_case = int(input())
for i in range(test_case):
    ox_quiz = input()
    print(my_point(ox_quiz))

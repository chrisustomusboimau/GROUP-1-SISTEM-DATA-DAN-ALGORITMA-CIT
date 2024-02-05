def input_data():
    data = {}
    while True:
        try:
            print("input the score")
            score = int(input("score = "))
            if score in range(101):
                data[score] = "-"
                return data
            print("please enter a score between 0-100")
        except:
            print("please enter a score between 0-100")

def convert_scores(only_score):
    score_list = only_score.copy()
    for score in score_list:
        if score in range(91,101):
            score_list[score] = "A"
        elif score in range(86,91):
            score_list[score] = "A-"
        elif score in range(81,86):
            score_list[score] = "B+"
        elif score in range(76,81):
            score_list[score] = "B"
        elif score in range(71,76):
            score_list[score] = "B-"
        elif score in range(61,71):
            score_list[score] = "C+"
        elif score in range(51,61):
            score_list[score] = "C"
        elif score in range(46,51):
            score_list[score] = "C-"
        elif score in range(41,46):
            score_list[score] = "D"
        else:
            score_list[score] = "F"
    return score_list
    
def print_score(score_list):
    for i in score_list:
        print(f"Score {i} ({score_list[i]})")


score_list = input_data()
score_list = convert_scores(score_list)
print_score(score_list)








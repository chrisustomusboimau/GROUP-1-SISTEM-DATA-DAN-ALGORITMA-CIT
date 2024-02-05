import random

def input_guess():
    while True:
        print("""choose scissors, rock, or paper
1. scissors
2. rock
3. paper\n
""")
        guess = input("guess = ")
        if guess == "1":
            return "scissors"
        elif guess == "2":
            return "rock"
        elif guess == "3":
            return "paper"
        else:
            print("Choose a number between 1, 2, or 3.\n")

def check_round(Human,Bot):
    print(f"""Human = {Human}
Bot = {Bot}
""")
    if Human == "scissors":
        if Bot == "scissors":
            return "Tie"
        elif Bot == "rock":
            return "Bot"
        elif Bot == "paper":
            return "Human"
    if Human == "rock":
        if Bot == "scissors":
            return "Human"
        elif Bot == "rock":
            return "Tie"
        elif Bot == "paper":
            return "Bot"  
    if Human == "paper":
        if Bot == "scissors":
            return "Bot"
        elif Bot == "rock":
            return "Human"
        elif Bot == "paper":
            return "Tie"

def score_board(Human,Bot):
    print(f"Human-Bot = {Human}-{Bot}")

# -----main code----
score = {"Human":0,"Bot":0}
while True:
    Human_guess = input_guess()
    Bot_guess = random.randint(1,3)

    if Bot_guess == 1:
        Bot_guess = "scissors"
    elif Bot_guess == 2:
        Bot_guess = "rock"
    else:
        Bot_guess = "paper"
    
    round = check_round(Human_guess,Bot_guess)
    
    if round == "Human":
        score["Human"] += 1
    elif round == "Bot":
        score["Bot"] += 1
    else:
        print("Tie")

    score_board(score["Human"],score["Bot"])

    if score["Human"] == 3:
        print("\n\nHuman is the winner")
        break

    if score["Bot"] == 3:
        print("\n\nBot is the winner")
        break    





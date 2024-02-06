import random

def input_guess():
    while True:
        try:
            guess = int(input("Your move ?(1-3): "))
            if 1 <= guess <= 3:
                return guess
            else:
                print("Invalid Move, you must only choose one of them (1-3).")
        except ValueError:
            print("What yous just enter is not (1-3) please make a valid move.")

def check_winner(bot_move, human_move):
    if bot_move == human_move:
        return "draw"
    elif (bot_move == 1 and human_move == 3) or (bot_move == 2 and human_move == 1) or (bot_move == 3 and human_move == 2):
        return "bot"
    else:
        return "human"

def display_scoreboard(human_score, bot_score):
    print(f"Human-Bot = {human_score} - {bot_score}")

def display_message(score):
    if score == 1:
        print("Wow, you're a little bit good at this :)")
    elif score == 2:
        print("Wow! You're starting to show your skills.")
    elif score == 3:
        print("Wow! You really are superior.")
    elif score == 4:
        print("Wow! Maybe this isn't my lucky day, but it's certainly yours :)")
    elif score == 5:
        print("Congratulations! You have won.")

def play_game():
    start_game = str(input("Do you want to play a game? (yes/no): "))
    if start_game.lower() == "yes":
        human_score = 0
        bot_score = 0

        while human_score < 5 and bot_score < 5:
            bot_guess = random.randint(1, 3)
            human_guess = input_guess()
            winner = check_winner(bot_guess, human_guess)

            if winner == "bot":
                bot_score += 1
                if bot_score == 1:
                    print("Wow! This is MY lucky day ;)")
                elif bot_score == 2:
                    print("Get ready to lose ;)")
                elif bot_score == 3:
                    print("Are you sure you want to resume? I am, of course, WINNING ;)")
                elif bot_score == 4:
                    print("Admit it, You ARE losing, Humanity has Fallen, The AI will Triumph :D :D")
                elif bot_score == 5:
                    print("Better luck next time")
            elif winner == "human":
                human_score += 1
                display_message(human_score)

            display_scoreboard(human_score, bot_score)

        if human_score == 5:
            print("Congratulations! You have won.")
        elif bot_score == 5:
            print("Better luck next time")
    elif start_game.lower() == "no":
        print("Alright, There's always tomorrow")
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

play_game()
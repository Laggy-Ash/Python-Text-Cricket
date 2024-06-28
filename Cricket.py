"""
Cricket
Copyright (C) 2022  Laggy-Ash

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import random

expressions = {
    "toss": "Choose Odd or Even\n>",
    "bat_or_ball": "What do you choose? Bat or Ball?\n>",
    "invalid": "Invalid option\n",
    "bat": "Attempt a score from 0-6:\n>",
    "ball": "Predict the score from 0-6:\n>",
    "not_int_runs": "Score is supposed to be an integer less than 6\n",
    "out": "You and the Program chose the same runs. That's an out",
    "user_score": "Your score is: ",
    "program_score": "Program's score is: ",
    "user_won": "Congratulations! You've won!\n",
    "program_won": "The program won this game. Better luck next time!\n",
    "user_to_win": "The score required for the user to win is",
    "program_to_win": "The score required for the program to win is",
    "tie": "It's a tie! Looks like a rematch to me\n"
}

# Variables
toss_options = ['odd', 'even', 'o', 'e']
tosscho_ice = 0
toss_win = False
toss_pending = True
play_choice = ['bat', 'ball']
runs = [0, 1, 2, 3, 4, 5, 6]
try_program = 0
play_choice_program = 0
score_program = 0
chose_user = False
try_user = 0
play_choice_user = 0
score_user = 0


while toss_pending:
    toss_choice = str.lower(input(expressions["toss"]))
    if toss_choice in toss_options:
        toss_pending = False
    else:
        print(expressions["invalid"])
        

def main():
    print(toss(toss_choice))
    print(choice(toss_win))
    play()


def toss(user_toss_choice):
    tossresult = random.choice(toss_options)
    global toss_win
    if user_toss_choice == str(tossresult):
        toss_win = True
        return 'You won the toss!'
    else:
        return 'Computer won the toss!'


def choice(toss_win_status):
    global play_choice_user
    global play_choice_program
    global chose_user
    choice_invalid = True
    if toss_win_status:
        chose_user = True
        while choice_invalid:
            play_choice_user = str.lower(input(expressions["bat_or_ball"]))
            if play_choice_user not in play_choice:
                print(expressions["invalid"])
            else:
                return f"You chose to {play_choice_user}"
    else:
        play_choice_program = random.choice(play_choice)
        return f"Program chose to {play_choice_program}"


def compare(userscore, programscore):
    def scores(user_score, program_score, win=None):
        print(f"Your final score is {user_score}")
        print(f"Program's final score is {program_score}")
        if win:
            print(expressions["user_won"])
        elif win == False:
            print(expressions["program_won"])
        else:
            print(expressions["tie"])

    if userscore > programscore:
        scores(userscore, programscore, True)
    elif userscore < programscore:
        scores(userscore, programscore, False)
    else:
        scores(userscore, programscore)
    exit()


def user_bat():
    global round_1_over
    global try_user
    global try_program
    global score_user
    global score_program
    round_1_over = False
    try_user = 7
    if score_user or score_program > 0:
        round_1_over = True
    while try_user != try_program:
        if round_1_over and score_user>score_program:
            break
        try_user = input(expressions["bat"])
        try:
            try_user = int(try_user)
            if try_user not in runs:
                print(expressions["not_int_runs"])
            else:
                try_program = random.choice(runs)
                print(f"Program chose: {try_program}")
                if try_user == 0:
                    score_user = score_user + try_program
                else:
                    score_user = score_user + try_user
        except ValueError:
            print("Only integers are allowed")
    score_user = score_user - int(try_user)
    if round_1_over:
        compare(score_user, score_program)
    else:
        print(expressions["out"])
        print(f"You scored a total of {score_user} runs")
        round_1_over = True
        


def user_ball():
    global round_1_over
    global try_user
    global try_program
    global score_user
    global score_program
    try_user = 7
    round_1_over = False
    if score_user or score_program > 0:
        round_1_over = True
    while try_user != try_program:
        if round_1_over and score_program>score_user:
            break
        try_user = input(expressions["ball"])
        try:
            try_user = int(try_user)
            if try_user not in runs:
                print(expressions["not_int_runs"])
            else:
                try_program = random.choice(runs)
                print(f"Program chose: {try_program}")
                if try_program == 0:
                    score_program = score_program + try_user
                else:
                    score_program = score_program + try_program
        except ValueError:
            print("Only integers are allowed")
    score_program = score_program - try_program
    if round_1_over:
        compare(score_user, score_program)
    else:
        print(expressions["out"])
        print(f"Program scored a total of {score_program} runs")
        round_1_over = True


def play():
    if chose_user:
        if play_choice_user == 'bat':
            user_bat()
            if round_1_over:
                print(f'{expressions["program_to_win"]} {score_user + 1}')
                user_ball()
        if play_choice_user == 'ball':
            user_ball()
            if round_1_over:
                print(f'{expressions["user_to_win"]} {score_program + 1}')
                user_bat()
    if not chose_user:
        if play_choice_program == 'bat':
            user_ball()
            if round_1_over:
                print(f'{expressions["user_to_win"]} {score_program + 1}')
                user_bat()
        if play_choice_program == 'ball':
            user_bat()
            if round_1_over:
                print(f'{expressions["program_to_win"]} {score_user + 1}')
                user_ball()


if __name__ == '__main__':
    main()

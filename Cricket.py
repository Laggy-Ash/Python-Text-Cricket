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
    "not_int_runs": "Score is supposed to be an integer less than 6, Dum-Dum\n",
    "out": "You and the Program chose the same runs. That's an out\n",
    "user_score": "Your score is: ",
    "program_score": "Program's score is: ",
    "user_won": "Congratulations! You've won!",
    "program_won": "The program won this game. Better luck next time!",
    "user_to_win": "The score required for the user to win is",
    "program_to_win": "The score required for the program to win is"
}

# Variables
tossoptions = ['odd', 'even', 'o', 'e']
tosschoice = 0
tosswin = False
toss_invalid = True
playchoice = ['bat', 'ball']
runs = [0, 1, 2, 3, 4, 5, 6]
round_1_over = False
try_program = 0
play_choice_program = 0
score_program = 0
chose_user = False
try_user = 0
play_choice_user = 0
score_user = 0
balls = 0


def main():
    print(toss(tosschoice))
    print(choice(tosswin))
    play()


def toss(user_tosschoice):
    tossresult = random.choice(tossoptions)
    global tosswin
    if user_tosschoice == str(tossresult):
        tosswin = True
        return 'You won the toss!'
    else:
        return 'Computer won the toss!'


while toss_invalid:
    tosschoice = str.lower(input(expressions["toss"]))
    if tosschoice in tossoptions:
        toss_invalid = False
    else:
        print(expressions["invalid"])


def choice(toss_win_status):
    global play_choice_user
    global play_choice_program
    global chose_user
    choice_invalid = True
    if toss_win_status:
        chose_user = True
        while choice_invalid:
            play_choice_user = str.lower(input(expressions["bat_or_ball"]))
            if play_choice_user not in playchoice:
                print(expressions["invalid"])
            else:
                return f"You chose to {play_choice_user}"
    else:
        play_choice_program = random.choice(playchoice)
        return f"Program chose to {play_choice_program}"


def compare(userscore, programscore):
    def scores(user_score, program_score, win):
        print(f"Your final score is {user_score}")
        print(f"Program's final score is {program_score}")
        if win:
            print(expressions["user_won"])
        elif win == False:
            print(expressions["program_won"])
        else:
            superover()

    if userscore > programscore:
        scores(userscore, programscore, True)
    elif userscore < programscore:
        scores(userscore, programscore, False)
    else:
        scores(userscore, programscore, None)
    exit()


def user_bat(super = False):
    global round_1_over
    global try_user
    global try_program
    global score_user
    global score_program
    global balls
    try_program = 7
    while try_user != try_program:
        if round_1_over:
            if score_user > score_program:
                compare(score_user, score_program)
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
            if super:
                balls+=1
                return balls
        except ValueError:
            print("Only integers are allowed")
    score_user = score_user - try_user
    if round_1_over:
        compare(score_user, score_program)
    while not super:
        print(expressions["out"])
        print(f"You scored a total of {score_user} runs")
        round_1_over = True


def user_ball(super = False):
    global round_1_over
    global try_user
    global try_program
    global score_user
    global score_program
    global balls
    try_user = 7
    while try_user != try_program:
        if round_1_over:
            if score_program > score_user:
                compare(score_user, score_program)
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
            if super:
                balls+=1
                return balls
        except ValueError:
            print("Only integers are allowed")
    score_program = score_program - try_program
    if round_1_over:
        compare(score_user, score_program)
    while not super:
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

def superover():
    global balls
    global score_program
    global score_user
    score_user = score_program = 0
    while balls < 6:
        user_bat(True)
    print('\nThe program bats now')
    balls = 0
    while balls < 6:
        user_ball(True)
    print (f"\nThe final scores after the superover are: \n Program's score:  {score_program} \n User's score: {score_user}")
    if score_user > score_program:
        print(expressions["user_won"])
    else:
        print(expressions["program_won"])

if __name__ == '__main__':
    main()

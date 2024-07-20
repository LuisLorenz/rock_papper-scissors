import time
import random 
import sys

# flow writing class
class flow_writing:
    def __init__(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

            if char in ".!?":
                time.sleep(0.5) 
            

class flow_writing_v2:
    def __init__(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

            if char in ".!?":
                time.sleep(0.5) 
            print(' ') # adding a new row

# define maybe a class
    # advantages
        # storing multiple modules in this class 
        # seems not to be that necessary at this level 

def get_integer_input(text_int):
    while True:
        user_input = input(text_int)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Your input was invalid please try again!")

def game(): 

    # introduction 
    text_intro = 'ROCK! Paper! Scissors! '
    intro = flow_writing_v2(text_intro)

    # asking user 
    test_int = 'Are you ready? Yes (1), No (2)\n'
    # flow_text_question = flow_writing(test_question)

    get_integer_input(test_int)

    if get_integer_input == 1:
        text_continue = 'Very nice!'
        flow_text_continue = flow_writing(text_continue)

    elif get_integer_input == 2: 
        print('Okay :(')
        text_closing_program = '''
    Okay :( ...
    The game has been closed.\n'''
        flow_text_closing_program = flow_writing(text_closing_program)
        exit() # does not work!!!
        # end this game

    # fix when the user does not input an int!

    text_starting ='''
Here are the rules ... 
The player that reaches 10 subwins wins the whole game ...
Additionally, ...
If one user wins two times in a row, his next win counts as double subwin ...
Also the oppenent will get -1 for his amount of subwins ...
Last but not least ...
The amount of subwins don't goes below 0 ...
'''

    flow_test_starting = flow_writing(text_starting)

    options = ['r', 'p', 's']

    # while loop 
        # stops when 10 wins are obtained 

    user_subwins = 0 
    computer_subwins = 0 

    streak_user = 0
    streak_computer = 0 
  
    while user_subwins != 10 and computer_subwins != 10:
        # logical mistake
        # ...
        # user_sw = 10 or computer_sw = 10 -> break 
        # user_sw =! 10 and computer_sw =! 10 

        # minimal board for subwins

        if user_subwins < 0:
            user_subwins = 0

        if computer_subwins < 0:
            computer_subwins = 0 

        print(f'''
Currtens stats:
- user_subwins = {user_subwins} 
- computer_subwins = {computer_subwins}''')

        # random choice computer
        choice_computer = random.choice(options)
        
        # random choice user
        choice_user = input('''
Make a choice: 
- "r" for rock
- "p" for paper
- "s" for scissors 
''')
        
            # checkup 
            # if True -> continue
            # else -> try again 

        if choice_user == 'r' or choice_user == 'p' or choice_user == 's': 
                

            # implent a checkup for the right input -> try ...

            # evalution & record
            # implement counter of wins
                # reset after each lose
                # while loop 
                # first checks if the condition is fulfilled 

            

            if streak_user > 1: 

                # computer has won 
                if choice_computer == "r"and choice_user == "s" or choice_computer == "p" and choice_user == "r" or choice_computer == "s" and choice_user == "p": 
                    computer_subwins += 1 
                    streak_user = 0 
                    streak_computer += 1 
                    print("You have lost this round!") 

                # user has won
                elif choice_user == "r"and choice_computer == "s" or choice_user == "p" and choice_computer == "r" or choice_user == "s" and choice_computer == "p": 
                    user_subwins += 2
                    computer_subwins -= 1 
                    streak_user += 1 
                    streak_computer = 0 
                    print("You have won this round")

                # it's a tie 
                else:
                    streak_user = 0 
                    streak_computer = 0 
                    print("It's a tie!")

            elif streak_computer > 1:

                # computer has won 
                if choice_computer == "r"and choice_user == "s" or choice_computer == "p" and choice_user == "r" or choice_computer == "s" and choice_user == "p": 
                    user_subwins -= 1
                    computer_subwins += 2 
                    streak_user = 0 
                    streak_computer += 1 
                    print("You have lost this round!")

                # user has won
                elif choice_user == "r"and choice_computer == "s" or choice_user == "p" and choice_computer == "r" or choice_user == "s" and choice_computer == "p": 
                    user_subwins += 1
                    streak_user += 1 
                    streak_computer = 0 
                    print("You have won this round")

                # it's a tie 
                else:
                    streak_user = 0 
                    streak_computer = 0 
                    print("It's a tie!")

            else: 

                # computer has won 
                if choice_computer == "r"and choice_user == "s" or choice_computer == "p" and choice_user == "r" or choice_computer == "s" and choice_user == "p": 
                    user_subwins -= 1
                    computer_subwins += 1 
                    streak_user = 0 
                    streak_computer += 1 
                    print("You have lost this round!")

                # user has won
                elif choice_user == "r"and choice_computer == "s" or choice_user == "p" and choice_computer == "r" or choice_user == "s" and choice_computer == "p": 
                    user_subwins += 1
                    computer_subwins -= 1 
                    streak_user += 1 
                    streak_computer = 0 
                    print("You have won this round")

                # it's a tie 
                else:
                    streak_user = 0 
                    streak_computer = 0 
                    print("It's a tie!")

        else:
            print('Sorry, your input was invalid. Please try again!')

    # end 
    if user_subwins > 9:
        text_win = '\nCongrates, you are the winner of this game!\n'
        flow_text_win = flow_writing(text_win)
    else:
        text_lose = '\nSorry, the computer has beaten you!\n'
        flow_text_lose = flow_writing(text_lose)

# initializing game 
game()

# want to play again? - input
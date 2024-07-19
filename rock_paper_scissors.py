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
        print(' ') # adding a new row

# define maybe a class


# def game(): 

    # introduction 

    # random choice computer

    # random choice user

    # evalution & record

    # end 

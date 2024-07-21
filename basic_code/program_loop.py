# def main_program():
#     # Dein Programmcode hier
#     print("Das Programm läuft...")

# # Hauptschleife
# while True:
#     main_program()
    
#     # Den Benutzer fragen, ob das Programm erneut ausgeführt werden soll
#     erneut_ausfuehren = input("Möchten Sie das Programm erneut ausführen? (ja/nein): ").strip().lower()
    
#     # Überprüfen, ob die Antwort "nein" ist, um die Schleife zu beenden
#     if erneut_ausfuehren != 'ja':
#         print("Programm beendet.")
#         break

# # very easy 
# # simply are loop that breaks only when the users denys the loop

import time
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

def game():
    print('This is my game')

continue_loop = None 

while True:
    
    if continue_loop == 'y': 
        game()

    text_loop = 'Do you want to play again? yes (y)/ no (n)'
    flow_text_loop = flow_writing(text_loop)
    continue_loop = input()

    if continue_loop == 'y': 
        pass  

    elif continue_loop == 'n':
        text_closing_program = '''Okay :( ...
The game has been closed.\n'''
        flow_text_closing_program = flow_writing(text_closing_program)
        break
    else:
        print('Your input was invalid. Please try again!')
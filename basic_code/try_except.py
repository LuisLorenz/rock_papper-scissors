def get_integer_input(prompt="Bitte eine Ganzzahl eingeben: "):
    while True:
        user_input = input(prompt)
        try:
            # Versuche, die Eingabe in eine Ganzzahl umzuwandeln
            user_input = int(user_input)
            return user_input
        except ValueError:
            # Wenn die Eingabe keine gültige Ganzzahl ist, zeige eine Fehlermeldung und wiederhole die Anfrage
            print("Ungültige Eingabe. Bitte eine Ganzzahl eingeben.")

get_integer_input()

# ... research the character of try and except
    # when does the loop stops and when does it continue? 


def get_integer_input(text):
    while True:
        user_input = input(text)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Your input was invalid please try again!")
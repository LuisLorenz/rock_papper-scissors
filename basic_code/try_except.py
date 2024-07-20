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
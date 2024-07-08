import math

print("ESERCIZIO 1\n\n\n")
def safe_sqrt(number):
    try:
        return math.sqrt(number)
    except ValueError as error:
        print(f"il valore non puo essere negativo")
        return -1

number = -10
print(safe_sqrt(number))

print("\n\n\nESERCIZIO 2\n\n\n")

def validate_password(password):
    charspecial : list = ["!", "\"", "£", "$", "%", "&", "/", "(", ")", "=", "?", "^"]
    if len(password) >= 20:
        pass
    else:
        raise InvalidPasswordError("La password deve essere di almeno 20 caratteri")
    
    count = 0
    for i in charspecial:
        if i in password:
            count += 1
    if count >= 4:
        pass
    else:
        raise InvalidPasswordError("La password deve contenere alemno 4 caratteri speciali")
           
    if sum([1 if c.isupper() else 0 for c in password]) >= 3:
        pass
    else:
        raise InvalidPasswordError(f"La password deve contenere almeno 3 lettere maiuscole")

class InvalidPasswordError(Exception):
    pass

password = "leonardoa!£$%&/FhAAffba"

validate_password(password)

print("\n\n\nESERCIZIO 3\n\n\n")

with open("Lezione18/file_per_eesercitarsi.txt") as file:
    file.close()
    try:
        read_data = file.read()
    except ValueError:
        print("Failed reading")
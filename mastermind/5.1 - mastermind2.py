import random

kleuren = ( "R", "G", "B", "O", "P", "W" )
antwoord = []

for i in range(4):
    antwoord.append( kleuren[random.randint(0,5)])

print(antwoord)

while True:
    # input vragen aan de gebruiker
    gok = input("Doe een nieuwe gok: ")
    gok = gok.strip()

    # stoppen als de gebruiker het spel vroegtijdig beu is
    if ( gok.upper() == "STOP" ):
        print("Jammer! Het juiste antwoord was: ")
        print(antwoord)
        break
    else:
        print("OK")
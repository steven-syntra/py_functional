import random

kleuren = ( "R", "G", "B", "O", "P", "W" )
antwoord = []

for i in range(4):
    antwoord.append( kleuren[random.randint(0,5)])

print(antwoord)

while True:
    aantal_juiste_plaatsen = 0

    # input vragen aan de gebruiker
    gok = input("Doe een nieuwe gok: ")
    gok = gok.strip()

    # stoppen als de gebruiker het spel vroegtijdig beu is
    if ( gok.upper() == "STOP" ):
        print("Jammer! Het juiste antwoord was: ")
        print(antwoord)
        break
    else:
        # aantal juiste plaatsen bepalen
        for i in range(4):
            if gok[i] == antwoord[i]:
                aantal_juiste_plaatsen += 1
        if ( aantal_juiste_plaatsen == 4 ):
            # spel beëindigen als alles gevonden is
            print("Proficiat!")
            print("Het juiste antwoord was: ")
            print(antwoord)
            break
        else:
            print(str(aantal_juiste_plaatsen) + " letters op de juiste plaats")

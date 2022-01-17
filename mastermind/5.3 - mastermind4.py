import random

kleuren = ("R", "G", "B", "O", "P", "W")
antwoord = []

for i in range(4):
    antwoord.append(kleuren[random.randint(0, 5)])

# print(antwoord)

while True:
    aantal_juiste_plaatsen = 0

    # input vragen aan de gebruiker
    gok = input("Doe een nieuwe gok: ")
    gok = gok.strip()

    # stoppen als de gebruiker het spel vroegtijdig beu is
    if gok.upper() == "STOP":
        print("Jammer! Het juiste antwoord was: ")
        print(antwoord)
        break
    else:
        # aantal juiste plaatsen bepalen
        antwoord_kopie = antwoord.copy()
        gok_kopie = list(gok)

        for i in range(4):
            if gok_kopie[i] == antwoord_kopie[i]:
                aantal_juiste_plaatsen += 1
                gok_kopie[i] = "X"
                antwoord_kopie[i] = "Y"

        if aantal_juiste_plaatsen == 4:
            # spel beëindigen als alles gevonden is
            print("Proficiat!")
            print("Het juiste antwoord was: ")
            print(antwoord)
            break
        else:
            print(str(aantal_juiste_plaatsen) + " letters op de juiste plaats")

            # aantal foute plaatsen bepalen
            aantal_foute_plaatsen = 0
            for g in range(4):
                for k in range(4):
                    if gok_kopie[g] == antwoord_kopie[k]:
                        aantal_foute_plaatsen += 1
                        gok_kopie[g] = "X"
                        antwoord_kopie[k] = "Y"

            print(str(aantal_foute_plaatsen) + " letters op een foute plaats")

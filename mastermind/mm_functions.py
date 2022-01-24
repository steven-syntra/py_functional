import random
import mm_database


# 4 willekeurige kleuren (uit kleuren) kiezen
def Choose4Colors(kleuren):
    antwoord = []
    for i in range(4):
        antwoord.append(kleuren[random.randint(0, 5)])

    gameid = mm_database.DB_InsertGameinDB(antwoord)
    return antwoord, gameid


# input vragen aan speler
def GetInputFromUser(userinput):
    gok = input("Doe een nieuwe gok: ").strip()
    userinput += ''.join(gok) + '|'
    return gok, userinput


# stoppen als de gebruiker het spel vroegtijdig beu is
def UserWantsToQuitEarly(gok, antwoord, gameid, userinput):
    if gok.upper() == "STOP":
        print( f"Jammer! Het juiste antwoord was: {antwoord}" )
        mm_database.DB_CancelGameInDB(gameid, userinput)
        return True

    return False


# spel beëindigen als alles gevonden is
def SolutionFoundEndGame(antwoord, gameid, userinput):
    mm_database.DB_FinishGameInDB(gameid, userinput)
    print("Proficiat!")
    print( f"Het juiste antwoord was: { antwoord }")


# aantal juiste plaatsen bepalen
def FindColorsOnRightPosition(antwoord, gok):
    aantal_juiste_plaatsen = 0
    antwoord_kopie = antwoord.copy()
    gok_kopie = list(gok)

    for i in range(4):
        if gok_kopie[i] == antwoord_kopie[i]:
            aantal_juiste_plaatsen += 1
            gok_kopie[i] = "X"
            antwoord_kopie[i] = "Y"

    return aantal_juiste_plaatsen, antwoord_kopie, gok_kopie


# aantal foute plaatsen bepalen
def FindColorsOnWrongPosition(antwoord_kopie, gok_kopie):
    aantal_foute_plaatsen = 0
    for i in range(4):
        for j in range(4):
            if gok_kopie[i] == antwoord_kopie[j]:
                aantal_foute_plaatsen += 1
                gok_kopie[i] = "X"
                antwoord_kopie[j] = "Y"
    return aantal_foute_plaatsen


# feedback aan speler, met x juiste plaatsen, y foute plaatsen
def GiveFeedback(juiste_plaatsen, foute_plaatsen):
    print( f" - {juiste_plaatsen} letters op de juiste plaats")
    print( f" - {foute_plaatsen} letters op een foute plaats")


# hoofdprocedure spel
def PlayGame(antwoord, gameid):

    userinput = ""

    while True:
        gok, userinput = GetInputFromUser(userinput)

        if UserWantsToQuitEarly(gok, antwoord, gameid, userinput):
            break

        juiste_plaatsen, antwoord_kopie, gok_kopie = FindColorsOnRightPosition(antwoord, gok)

        if juiste_plaatsen == 4:
            SolutionFoundEndGame(antwoord, gameid, userinput)
            break

        foute_plaatsen = FindColorsOnWrongPosition(antwoord_kopie, gok_kopie)
        GiveFeedback(juiste_plaatsen, foute_plaatsen)

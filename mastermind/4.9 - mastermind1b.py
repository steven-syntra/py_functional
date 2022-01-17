import random

kleuren = ( "R", "G", "B", "O", "P", "W" )
antwoord = []

for i in range(4):
    antwoord.append( kleuren[random.randint(0,5)])

print(antwoord)
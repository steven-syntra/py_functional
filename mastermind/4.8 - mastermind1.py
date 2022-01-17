import random

kleuren = ( "rood", "groen", "geel", "blauw", "oranje", "paars" )
antwoord = []

for i in range(4):
    antwoord.append(random.choice(kleuren))
    #antwoord.append( kleuren[random.randint(0,5)])

print(antwoord)

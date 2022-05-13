import random
print("Welkom bij Galgje!")

woorden = ("informatica", "informatiekunde", "spelletje", "aardigheid", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")

def get_woorden():

    print(random.choice(woorden))

    return woorden

get_woorden()


import random
print("Welkom bij Galgje!")

word = ("informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk")

def get_word():

    print(random.choice(word))

    return word

get_word()

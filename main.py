import random as r
print("Welkom bij Galgje!")
wordlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

randomWord = r.choice(wordlist)

print(randomWord)
print(len(randomWord))

isGameRunning = True

def get_woorden():

    print(r.choice(randomWord))

    return randomWord

get_woorden()
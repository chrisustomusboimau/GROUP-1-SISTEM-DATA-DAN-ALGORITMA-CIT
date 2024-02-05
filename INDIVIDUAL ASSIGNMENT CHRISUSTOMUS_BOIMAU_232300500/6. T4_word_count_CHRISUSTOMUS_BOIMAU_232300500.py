"""
T4 - WORDS COUNT

NAMA = CHRISUSTOMUS BOIMAU
NIM  = 232300500
"""

def histo(file):
    histo = {}
    for i in file:
        text = i.upper().split()
        for i2 in text:
            if i2 not in histo:
                histo[i2] = 0
            histo[i2] += 1
    return histo

def search(histo):
    while True:
        print("Please enter a word, once you have finished type -1")
        word = input("word = ").upper()
        if word == "-1":
            break
        elif word not in histo:
            print(f"{word} = 0 words\n")
        else:
            print(f"{word} = {histo[word]} words\n")

file = open("Kejadian 1 1-10.txt","r")
histogram = histo(file)
search(histogram)
file.close()


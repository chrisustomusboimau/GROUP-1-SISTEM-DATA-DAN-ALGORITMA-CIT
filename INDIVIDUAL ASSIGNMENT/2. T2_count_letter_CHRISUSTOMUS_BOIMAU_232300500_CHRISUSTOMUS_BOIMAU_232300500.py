"""
T2 - COUNT LETTER

NAMA = CHRISUSTOMUS BOIMAU
NIM  = 232300500
"""

def Histogram():
    letter = {}
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
        letter[i] = 0
    return letter

def input_word(histo):
    update_histo = histo.copy()
    input_letter = list(input().upper())

    for i in input_letter:
        update_histo[i] += 1
    return update_histo

def print_data(data):
    for i in data:
        print(f"{i} = {data[i]}")

histo = Histogram()
histo = input_word(histo)
print_data(histo)
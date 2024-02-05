# T2 ->Count Letter 
# FUNCTION
def get_word ():
    print ("Word Count!")
    theword = input ("Masukan Kata untuk dihitung: ")
    lettercount = {}
    for letter in theword:
        if letter in lettercount:
            lettercount[letter] += 1
        else:
            lettercount[letter] = 1
    print (lettercount)

# MAIN 
get_word()
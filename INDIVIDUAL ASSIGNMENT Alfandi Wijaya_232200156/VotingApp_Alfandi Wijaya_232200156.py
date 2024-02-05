# Voting APP
# FUNCTION
def get_guess():
    guess = int(input("Pilih Nomor brapa (1/2/3): "))
    while guess > 3:
        print ("Please Input Number beetween 1 - 3!")
        guess = int(input("Pilih Nomor brapa (1/2/3): "))
    return guess
def system():
    print ("Pemungutan Suara dengan 3 Kandidat\nSilahkan pilih salahsatu!")
    count_guesess = {}
    for i in range(1,4):
        count_guesess[i] = 0
    the_guess = get_guess()
    while the_guess != 0: 
        if the_guess in count_guesess:
            count_guesess[the_guess] += 1
        else:
            count_guesess[the_guess] = 1    
        print (f"Total Vote: 1 ({count_guesess[1]}) - 2 ({count_guesess[2]}) - 3 ({count_guesess[3]})")
        the_guess = get_guess()

# MAIN
system()

# T4 Bubble sort
# FUNCTION
def get_number():
    numebrs = []
    total_number = int(input("Masukan jumlah angka yang akan diurutkan: "))
    for i in range (total_number):
        numebrs.append(int(input(f"Masukan Angka {i+1}: ")))
    return numebrs
    
def bubble_sort(list):
    listnumber = list
    for j in range (len(listnumber)):
        for i in range(len(listnumber)-1):
            if listnumber[i] > listnumber[i+1]:
                temp = listnumber[i]
                listnumber[i] = listnumber[i+1]
                listnumber[i+1] = temp
    print(f"Berikut hasil sortir dari yang terkecil: \n {listnumber}")

# MAIN
bubble_sort(get_number())
"""
T4 - BUBBLE SORT

NAMA = CHRISUSTOMUS BOIMAU
NIM  = 232300500
"""

def input_number():
    list_number = []
    while True:
        print("please input a number, and if you done type done\n")
        try:
            numbers = input("numbers = ")
            if numbers == "done":
                break
            numbers = int(numbers)
            list_number.append(numbers)
        except:
            print("please type only a numbers or 'done'")
    return list_number

def bubble_short(list_numbers):
    new_list_numbers = list_numbers.copy()
    for i in range(len(new_list_numbers)):
        for i2 in range(len(new_list_numbers)-1):
            if new_list_numbers[i2] > new_list_numbers[i2+1]:
                new_list_numbers[i2],new_list_numbers[i2+1]=new_list_numbers[i2+1],new_list_numbers[i2]
    return new_list_numbers

def print_numbers(list_numbers,sorted_list_number):
    print("list number before sorted")
    print(list_numbers)
    print("list number after sorted")
    print(sorted_list_number)
    

list_numbers = input_number()
sorted_list_number = bubble_short(list_numbers)
print_numbers(list_numbers,sorted_list_number)

        


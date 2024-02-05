def input_numbers():
    while True:
        try:
            print("Enter a positive integer number for calculations and -1 to terminate the program")
            numbers = int(input("numbers = "))
            if numbers == -1:
                return "done"
            if numbers > 0:
                    return numbers
            print("Enter an integer number greater than zero")
        except:
            print("Enter an integer number greater than zero")

def input_type():
    while True:
        print(""" calculation type:
            1. summation
            2. factorial
            3. fibonaci
            
            -1 = finish
    """)
        try:
            numbers = int(input("type = "))
            if numbers in range(1,4):
                return numbers
            elif numbers == -1:
                return numbers
            print("Enter a number between -1, 1, 2 or 3")
        except:
            print("Enter a number between -1, 1, 2 or 3")
            
        
def sum(numbers):
    hasil = 0
    for i in range(numbers+1):
        hasil += i   
    return hasil
              
def factorial (numbers):
    if numbers == 2:
        return(2)
    return(numbers * factorial(numbers-1))

def fibonaci(target,first_number=1,second_number=1):
    fibonaci_numbers = first_number + second_number  
    if target <= 0:
        return("there are no zero or negative Fibonacci numbers")
    if target == 1:
        return(first_number)
    if target == 2:
        return(second_number)
    if target == 3:
        return(fibonaci_numbers)
    return(fibonaci(target-1,second_number,fibonaci_numbers))

def calculation_type(n,kind):
    if kind == 1 :
        return sum(n)
    if kind == 2 :
        return factorial(n)
    if kind == 3:
        return fibonaci(target=n)



while True:
    numbers = input_numbers()
    if numbers == "done":
        break
    type_0 = input_type()
    if type_0 == -1:
        break
    print(calculation_type(numbers,type_0))



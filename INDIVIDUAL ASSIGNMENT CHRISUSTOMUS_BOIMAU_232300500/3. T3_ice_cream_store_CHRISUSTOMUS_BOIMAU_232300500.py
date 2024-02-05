"""
T3 - ICE CREAM STORE

NAMA = CHRISUSTOMUS BOIMAU
NIM  = 232300500
"""

# ----------------------------- CRUD FUNCTION ----------------------------------- 

def create(flavour_and_price):
    new_flavour_and_price = flavour_and_price.copy()
    while True:
            print("""\nadd new flavour, if you done please press 1\n""")
            flavour = input("flavour = ")
            if flavour == "1":
                break
            if flavour in new_flavour_and_price:
                print("\nplease add another flavour\n")
                continue
            harga = int(input("price = "))

            new_flavour_and_price[flavour] = harga
    return new_flavour_and_price

def read(flavour_and_price):
    for i in flavour_and_price:
        print(f"flavour {i} = Rp.{flavour_and_price[i]}")
    print()

def update(flavour_and_price):
    new_flavour_and_price = dict(flavour_and_price).copy()
    while True:
        print("""\nPlease select the flavor you want to change the price, and if you done please press 1\n""")
        flavour = input("flavour = ")
        if flavour == "1":
            break
        if flavour not in new_flavour_and_price:
            print("\nPlease choose an existing flavor\n")
            continue
        new_price = int(input("new price = "))
        new_flavour_and_price[flavour] = new_price
    return new_flavour_and_price

def delete(flavour_and_price):
    new_flavour_and_price = (flavour_and_price).copy()
    while True:
        print("""\nPlease select the flavor you want to delete, and if you done please press 1\n""")
        flavour = input("flavour = ")
        if flavour == "1":
            break
        if flavour not in new_flavour_and_price:
            print("\nPlease choose an existing flavor\n")
            continue
        new_flavour_and_price.pop(flavour)
    return new_flavour_and_price 


# ----------------------------- MAIN CODE ----------------------------------- 


flavour_and_price = {}
while True:
    print("""welcome, please select the command you want to run
          1. add new flavour
          2. shows the flavour and price
          3. update the price
          4. remove the flavour
          5. done\n""")
    command = input("command = ")
    print()
    if command == "1":
        flavour_and_price = create(flavour_and_price) 
    elif command == "2":
        read(flavour_and_price)
    elif command == "3":
        flavour_and_price = update(flavour_and_price) 
    elif command == "4":
        flavour_and_price = delete(flavour_and_price) 
    elif command == "5":
        break  
    else:
        print("please choose a number in range of 1 to 5")


            
    


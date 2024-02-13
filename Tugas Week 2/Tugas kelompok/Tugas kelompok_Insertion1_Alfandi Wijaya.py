# Insertion Sort 1
def insertion1(listin, type):
    unorder_data = listin
    if type == "A":
        des = 'dari yang terkecil'
        for i in range (1,len(unorder_data)):
            key = unorder_data[i]
            j = i-1
            while j >= 0 and key < unorder_data[j]:
                unorder_data[j+1] = unorder_data[j]
                j -= 1
            unorder_data[j+1] = key
    if type == "D":
        des = 'dari yang terbesar'
        for i in range (1,len(unorder_data)):
            key = unorder_data[i]
            j = i-1
            while j >= 0 and key > unorder_data[j]:
                unorder_data[j+1] = unorder_data[j]
                j -= 1
            unorder_data[j+1] = key
    print(f"Berikut hasil sortir {des}: \n {unorder_data}")



data = [[9,1,11,7,3,13,5],[10,4,14,8,2,12,5],['John','Jack','Jane','Jill'],['A','a','Z','z','1','10']]
order_type = ["A","D","A","D"]
print ("\nInsertion Sort 1!")
for i in range(len(data)):
    thelist = data[i]
    theorder = order_type[i]
    insertion1(thelist,theorder)
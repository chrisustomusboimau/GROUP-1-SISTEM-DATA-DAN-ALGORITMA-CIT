def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

list_1 = [9 , 1 , 11 , 7 , 3 , 13 , 5]
bubble_sort_ascending(list_1)
print("List 1 Sorted (Ascending):", list_1)


list_2 = ['John', 'Jack', 'Jane', 'Jill']
bubble_sort_ascending(list_2)
print("List 2 sorted(Ascending):", list_2)

def selection_sort_ascending(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


list_1 = [9 , 1 , 11 , 7 , 3 , 13 , 5]
selection_sort_ascending(list_1)
print("List 1 Sorted (Ascending):", list_1)


list_2 = ['John', 'Jack', 'Jane', 'Jill']
selection_sort_ascending(list_2)
print("List 2 sorted(Ascending):", list_2)
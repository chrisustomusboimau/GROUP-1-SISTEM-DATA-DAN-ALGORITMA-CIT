def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]


list_3 = [10, 4, 14, 8, 2, 12, 6 ]
selection_sort_descending(list_3)
print("List 3 sorted (descending):", list_3)


list_4 = ['A', 'a', 'Z', 'z', '1', '10']
selection_sort_descending(list_4)
print("List 3 sorted (descending):", list_4)




























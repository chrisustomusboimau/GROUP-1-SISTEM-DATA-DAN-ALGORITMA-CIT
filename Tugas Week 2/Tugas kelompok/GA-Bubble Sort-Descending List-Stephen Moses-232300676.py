def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


list_3 = [10, 4, 14, 8, 2, 12, 6 ]
bubble_sort_descending(list_3)
print("List 3 sorted (descending):", list_3)


list_4 = ['A', 'a', 'Z', 'z', '1', '10']
bubble_sort_descending(list_4)
print("List 3 sorted (descending):", list_4)
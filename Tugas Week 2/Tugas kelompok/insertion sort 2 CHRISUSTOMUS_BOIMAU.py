def insertion_sort_ascending(A):
    for k in range(1,len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j-=1
        A[j] = cur

def insertion_sort_descending(A):
    for k in range(1,len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] < cur:
            A[j] = A[j-1]
            j-=1
        A[j] = cur

a = [9,1,11,7,3,13,5]
insertion_sort_ascending(a)
print(a)

b = [10,4,14,8,2,12,6]
insertion_sort_ascending(b)
print(b)

c = ['Jhon','Jack','Jane','Jill']
insertion_sort_ascending(c)
print(c)

d = ['A','a','Z','z','1','10']
insertion_sort_ascending(d)
print(d)
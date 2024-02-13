maxSize = 10
nItems = 0
arr = [None] * maxSize

def length():
    return nItems

def get(n):
    if n >= 0 and n < nItems:
        return arr[n]

def set(n, value):
    if n >= 0 and n < nItems:
        arr[n] = value

def find(item):
    lo = 0
    hi = nItems - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def search(item):
    index = find(item)
    if index != -1:
        return arr[index]
    return None

def insert(item):
    global nItems
    if nItems >= maxSize:
        print("Overflow!")
        return
    index = find(item)
    for j in range(nItems, index, -1):
        arr[j] = arr[j - 1]
    arr[index] = item
    nItems += 1

def delete(item):
    global nItems
    j = find(item)
    if j != -1:
        nItems -= 1
        for k in range(j, nItems):
            arr[k] = arr[k + 1]
        return True
    return False

def traverse():
    for i in range(nItems):
        print(arr[i], end=' ')
    print()

# Driver code
insert(34)
insert(20)
insert(18)
insert(25)
insert(30)
insert(26)
insert(33)
insert(2)
insert(23)

target = 36
item = search(target)
if item is None:
    print(f"{target} is not found!")
else:
    print(f"Found item: {item}")

traverse()



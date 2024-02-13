# Array5 - Ordered Array (no Class)

maxSize = 10                      # Max size of the objArray
nItems = 0                        # No items in array initially

def length():                     # Special def for length() function
  return nItems                   # Return number of items

def get(n):                       # Return the value at index n
  if n >= 0 and n < nItems:       # Check if n is in bounds, and
    return arr[n]                 # only return item if in bounds

def set(n, value):                # Set the value at index n
  if n >= 0 and n < nItems:       # Check if n is in bounds, and
    arr[n] = value                # only set item if in bounds

def find(item):                   # Find index at or just below
  lo = 0                          # item in ordered list
  hi = nItems-1                   # Look between lo and hi
  while lo <= hi:
    mid = (lo + hi) // 2          # Select the midpoint
    if arr[mid] == item:          # Did we find it at midpoint?
      return mid                  # Return location of item
    elif arr[mid] < item:         # Is item in upper half?
      lo = mid + 1                # Yes, raise the lo boundary
    else:
      hi = mid - 1                # No, but could be in lower half
  return lo                       # Item not found, return insertion point instead

def search(item):
  global nItems
  index = find(item)                          # Search for item
  if index < nItems and \
    arr[index] == item:
      return arr[index]                         # and return item if found

def insert(item):                       # Insert item into correct position
  global nItems
  if nItems >= len(arr):                # If array is full,
    print("Overflow!")                  # Print an error message
  index = find(item)                    # Find index where item should go
  for j in range(nItems, index, -1):    # Move bigger items
    arr[j] = arr[j-1]                   # to the right
  arr[index] = item                     # Insert the item
  nItems += 1                           # Increment the number of items

def delete(item):                       # Delete any occurrence
  global nItems
  j = find(item)                        # Try to find the item
  if j < nItems and arr[j] == item:     # If found,
    nItems -= 1                         # One fewer at end
    for k in range(j, nItems):            # Move bigger items left
      arr[k] = arr[k+1]
    return True                         # Return success flag
  return False                          # Made it here; item not found     

def traverse():                         # Traverse all items
  for i in range(nItems):               # and apply a function
    print(arr[i], end=' ')
  print("\n")  

# driver
arr = [None] * maxSize           

insert(9)           
insert(3)
insert(11)
insert(7)

traverse()
insert(5)           
traverse()

insert(1)
traverse()

insert(13)
traverse()


target = 7
item = search(target)
if item is None:
  print(f"{target} is not found!\n")
else:
  print(f"Found item : {item}\n")

target = 15
item = search(target)
if item is None:
  print(f"{target} is not found!\n")
else:
  print(f"Found item : {item}\n")

# target = 30
# item = search(target)
# if item is None:
#   print(f"{target} is not found!\n")
# else:
#   print(f"Found item : {item}\n")

# target = 100
# item = search(target)
# if item is None:
#   print(f"{target} is not found!\n")
# else:
#   print(f"Found item : {item}\n")

# traverse()

# target = 20
# if delete(target):
#   print(f"Item {target} has been deleted!\n")
# else:
#   print(f"{target} is not found!\n")

# target = 21
# if delete(target):
#   print(f"Item {target} has been deleted!\n")
# else:
#   print(f"{target} is not found!\n")

# traverse()

# print(f"Array capacity : {maxSize}\n")

# print(f"Array size : {nItems}\n")
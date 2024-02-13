
class Array():
    def __init__(self, initialSize):        # Constructor
        self.__arr = [None] * initialSize     # The array stored as a list
        self.__nItems = 0                     # No items in array initially
        self.__maxSize = initialSize 
    
    def __len__(self):                      # Special def for len() function
        return self.__nItems                  # Return number of items

    def get(self, n):                       # Return the value at index n
        if n >= 0 and n < self.__nItems:      # Check if n is in bounds, and
            return self.__arr[n]                # only return item if in bounds

    def set(self, n, value):                # Set the value at index n
        if n >= 0 and n < self.__nItems:      # Check if n is in bounds, and
            self.__arr[n] = value 
    
    def find(self, item):                   # Find index at or just below
        lo = 0                          # item in ordered list
        hi = self.__nItems-1                   # Look between lo and hi
        while lo <= hi:
            mid = (lo + hi) // 2          # Select the midpoint
            if self.__arr[mid] == item:          # Did we find it at midpoint?
                return mid                  # Return location of item
            elif self.__arr[mid] < item:         # Is item in upper half?
                lo = mid + 1                # Yes, raise the lo boundary
            else:
                hi = mid - 1                # No, but could be in lower half
        return lo    
    
    def search(self, item):
        index = self.find(item)                          # Search for item
        if index < self.__nItems and \
            self.__arr[index] == item:
            return self.__arr[index]   
         
    def insert(self, item):                       # Insert item into correct position
        if self.__nItems >= len(self.__arr):                # If array is full,
            print("Overflow!")                  # Print an error message
        index = self.find(item)                    # Find index where item should go
        for j in range(self.__nItems, index, -1):    # Move bigger items
            self.__arr[j] = self.__arr[j-1]                   # to the right
        self.__arr[index] = item                   # Insert the item
        self.__nItems += 1                           # Increment the number of items

    def delete(self, item):                       # Delete any occurrence
        j = self.find(item)                        # Try to find the item
        if j < self.__nItems and self.__arr[j] == item:     # If found,
            self.__nItems -= 1                         # One fewer at end
            for k in range(j, self.__nItems):            # Move bigger items left
                self.__arr[k] = self.__arr[k+1]
            return True                         # Return success flag
        return False                          # Made it here; item not found     

    def traverse(self):                         # Traverse all items
        for i in range(self.__nItems):               # and apply a function
            print(self.__arr[i], end=' ')
        print("\n")  


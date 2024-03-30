import numpy as np

#COPY

#Make a copy, change the original array, and display both arrays:

arr = np.array ([1,2,3,4,5])

x = arr.copy()
arr[0] = 42

print (arr) # [42  2  3  4  5]
print (x) # [1 2 3 4 5]

# VIEW

#Make a view, change the original array, and display both arrays:

# arr1 = np.array([1, 2, 3, 4, 5])
# x1 = arr.view()
# arr1[0] = 42

# print(arr1)
# print(x1)

# arr1 = np.array([1, 2, 3, 4, 5])
# x1 = arr.view()
# x1[0] = 31

# print(arr1) #[1 2 3 4 5]
# print(x1) # [31  2  3  4  5]


# Check if Array Owns its Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

# Every NumPy array has the attribute base that returns None if the array owns the data.

# Otherwise, the base  attribute refers to the original object.

# Print the value of the base attribute to check if an array owns it's data or not:

arr2 = np.array([1, 2, 3, 4, 5])

x = arr2.copy()
y = arr2.view()

print(x.base) # None
print(y.base) # [1 2 3 4 5]
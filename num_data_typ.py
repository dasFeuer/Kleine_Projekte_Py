import numpy as np

# arr = np.array([1,2,3,4,5])
# arr1 = np.array(['apple', 'banana', 'pineapple'])

# print(arr.dtype) #int32
# print(arr1.dtype) #<U9

arr = np.array([1, 2, 3, 4], dtype='S') # S = string

print(arr)
print(arr.dtype)

arr1 = np.array([1, 2, 3, 4], dtype='i4') # i4 = integer with 4 bytes

print(arr1)
print(arr1.dtype)

# arr = np.array(['a', '2', '3'], dtype='i') # A non integer string like 'a' can not be converted to integer (will raise an error)

# Converting Data Type on Existing Arrays
# Change data type from float to integer by using 'i' as parameter value:

arr3 = np.array([1.1, 2.1, 3.1])
new_arr = arr.astype('i') # The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
# OR
new_arr = arr.astype(int)

print(new_arr)
print(new_arr.dtype)

# Change data type from integer to boolean:
arr4 = np.array([1, 0, 3])

new_arr1 = arr.astype(bool)

print(new_arr1)
print(new_arr1.dtype)

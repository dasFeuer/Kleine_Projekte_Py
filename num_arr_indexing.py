import numpy as np

# a = np.array(42)
# b = np.array([1,2,3,4,5])
# c = np.array([[1,2,3,4],[5,6,7,8]])
# d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# arr = np.array([1,2,3,4], ndmin=5)
# print(arr)
# print("Number of dimensions:", arr.ndim)

arr = np.array([1,2,3,4,5])
print (arr[1])
print (arr[2] + arr[3])

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print("The 2nd element om 1st row:", arr1[0, 3])

arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3[0,1,2])

arr4 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print ("Last element from 2nd dim:", arr4[1, -1]) 

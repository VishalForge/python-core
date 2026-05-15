import numpy as np
# Topic = Array creation and basic operations

# 1) 10 1D array of even numbers
a = np.arange(2, 21)[np.arange(2,21) % 2 == 0]
print(a)

# 2) 3 x 3 array of zeros, then replace the diagonal with 5
zero_array = np.zeros((3, 3))
print(zero_array)
np.fill_diagonal(zero_array, 5)
print(zero_array)


#  3) multiply 2 arrays elementwise and then find sum of the result
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(sum(a * b))


# 4) 4x4 array of random numbers
random_array = np.random.randint(1, 101, size = (4, 4))
print(random_array)
print(np.max(random_array))
print(np.min(random_array))
print(np.mean(random_array))

row, column = np.unravel_index(np.argmax(random_array), random_array.shape)
print("Index of max value: ", row, column)



# Topic: Indexing and Slicing
# 5) 
arr = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
print(arr[1:])  # Extract every element starting from index 1

# 6) 5x5 array and then extract only 3x3 block
c = np.arange(1, 26).reshape(5, 5)
print(c)
print(c[1:4, 1:4])

# 7) Extracting negative integers
arr = np.array([3, -1, 7, -4, 2, -9, 5, -2])
print(arr[arr>0])


# 8) comvert numbers greater than 0.5 into 1 and rest into 0
arr1 = np.random.rand(4, 4)
print(arr1)

binary_arr1 = (arr1 > 0.5).astype(int)  # astype() func will convert True into 1 and False into 0
print(binary_arr1)



# Topic = Shape and Reshaping

# 9) 
matrix = np.arange(12) 
print(matrix)
print(matrix.reshape(3, 4))
print(matrix.reshape(2, 6))
print(matrix.flatten())



# 10) what does Transpose means
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Original shape of the array: ", a.shape)
transposed_a = a.T
print("Shape of a after transpose: ", transposed_a.shape)  
'''Transpose swaps rows with columns.
Shape changes from (2 x 3) to (3 x 2).
Element at (i,j) moves to (j,i)'''



# 11) what is the reason for the shape of the c is (3, 3)
a = np.arange(3).reshape(3, 1)
b = np.arange(3).reshape(1, 3)

c = a + b
print(c)
print(c.shape)
'''Broadcasting: Numpy automatically expands the shapes (3, 1) and (1, 3)
to make them compatible. It stretches the first array along the columns
and the second array along the rows, resulting in a (3, 3) array'''
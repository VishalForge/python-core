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
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



# Topic = Statical and Mathematical Operations

# 12) 1D array of 1000 random numbers from a normal distribution
data = np.random.randn(1000)

mean_val = np.mean(data)
std_val = np.std(data)
median_val = np.median(data)
p25 = np.percentile(data, 25)
p75 = np.percentile(data, 75)

print(f"Mean: {mean_val:.6f}")
print(f"Std: {std_val:.6f}")
print(f"Median: {median_val:.6f}")
print(f"25th percentile: {p25:.6f}")
print(f"75th percentile: {p75:.6f}")

# How close to 0
distance_from_zero = abs(mean_val)    # abs() removes the negative sign
print(f"\nDistance of mean from 0 = {distance_from_zero:.6f}")



# 13) 2D array of shape (4, 5) filled with random floats
data_2 = np.random.rand(4, 5)
print(data_2)
mean_row = np.mean(data_2, axis=1)
mean_column = np.mean(data_2, axis=0)

print(f"Mean of each row: {mean_row}")
print(f"Mean of each column: {mean_column}")



# 14) Operations on the given array
arr = np.array([4, 9, 16, 25, 36])

print(f"Square root of elements: {np.sqrt(arr)}")
print(f"Natural log of elements: {np.log(arr)}")



# Topic = Real-World Thinking

# 15) You have a dataset of 100 student scores as 1D array:

scores = np.random.randint(40, 101, 100)

print(scores)
above_75 = scores[scores>75]
below_60 = scores[scores < 60]
percentage_below_60 = (len(below_60)/100) * 100

# replace all scores below 50 with exact 50
print("Before replacement min score:", scores.min())
scores[scores < 50] = 50

print(f"Students scored above 75: {len(above_75)}")
print(f"Percentage scored below 60: {percentage_below_60:.2f}%")
print(f"Minimum score after replacement: {scores.min()}")

# Normalization
min_score = scores.min()
max_score = scores.max()

normalized_scores = (scores - min_score) / (max_score - min_score)

print(f"Normalized scores (first 10): {normalized_scores[:10]}")
print(f"Min value: {normalized_scores.min()}")
print(f"Max value: {normalized_scores.max()}")





# 16) Operations on two arrays that represents predicted values and actual values:
actual = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1])
predicted = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

# how many predictions were correct
correct = np.sum(actual == predicted)

# accuracy
accuracy = (correct/len(actual)) * 100

# False positives (predicted 1, actual 0)
false_positives = np.sum(predicted == 1) & (actual == 0)

# False negatives (predicted 0, actual 1)
false_negatives = np.sum(predicted == 0) & (actual == 1)

print(f"Total samples          : {len(actual)}")
print(f"Correct predictions    : {correct}")
print(f"Accuracy               : {accuracy:.2f}% ")
print(f"False positives        : {false_positives}")
print(f"False  negatives       : {false_negatives}")





# 17) Operations on 2D array of shape (5, 4) representing days and products of sales:
sales = np.random.randint(100, 1001, size=(5, 4))

print("Sales Data (5 days x 4 Products):")
print(sales)

# Best-selling product (highest total across all days)
product_totals = np.sum(sales, axis=0)    #sum across days
best_product_idx = np.argmax(product_totals)  # Index of best product
best_product_sales = product_totals[best_product_idx]

print(f"\nTotal sales per product: {product_totals}")
print(f"Best selling product: Product {best_product_idx + 1} with {best_product_sales} sales")

# worst day (lowest total sales)
daily_totals = np.sum(sales, axis=1)    # sum across products
worst_day_idx = np.argmin(daily_totals)
worst_day_sales = daily_totals[worst_day_idx]

print(f"Total sales per day: {daily_totals}")
print(f"Worst day: Day {worst_day_idx + 1} with {worst_day_sales} sales")


# Normalize each product's sales to 0-1 range
col_min = np.min(sales, axis=0)
col_max = np.max(sales, axis=0)

normalized_sales = (sales - col_min)/(col_max - col_min)

print("Noramlized sales (each product 0-1):")
print(np.round(normalized_sales, 4))
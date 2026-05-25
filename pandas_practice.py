import pandas as pd

# ----Section 1: Creating & Inspecting DataFrames-------

# 1) Create a DataFrame from a given dictionary
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 28, 22],
    "salary": [50000, 60000, 75000, 55000, 45000],
    "department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"]
}

df = pd.DataFrame(data)
print(df)

print("===DataFrame Info===")
print(f"Shape of df: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nFirst 3 Rows:\n {df.head(3)}")



# 2) Some other operations on the same DF.
print(f"Summary of all numeric columns:\n {df.describe()}")
print(f"\nNull values in each column:\n{df.isnull().sum()}")
print(f"Duplicate rows:\n{df.duplicated()}")


#----Section 2: Selecting & Filtering---------

# 3) select only the name and salary columns
print(df[['name', 'salary']])

# rows where salary > 55000
print("\nRows where salary > 55000:")
print(df[df['salary']>55000])


# 4) Filter employees who are in 'Engineering' department
print("\nEngineering Department Employees:")
print(df[df['department'] == 'Engineering'])

# 5) Add a new column called 'senior' that is true if 'age' > 28, else false
df['senior'] = df['age'] > 28
print("\nUpdated DF:")
print(df)


#------Section 3: Cleaning Data----------

# 6) create a messy DF then perform some operations
df2 = pd.DataFrame({
    "product": ["apple", "banana", None, "cherry", "banana"],
    "price": [1.2, 0.5, 2.0, None, 0.5],
    "quantity": [10, 20, 15, 8, 20]
})
print("\nOriginal DF:")
print(df2)

print("\nColumns with null values:")
print(df2.isnull().sum())

df2 = df2.dropna(subset=['product'])     # removes null value of product column
df2['price'] = df2['price'].fillna(df2['price'].mean())  # Fill the null value of price column with mean price

# Remove duplicate values
df2 = df2.drop_duplicates()
print("\nFinal clean DataFrame:")
print(df2)


# 7) Clean DataFrame:
# Rename the columns 'product' and 'price'
df2 = df2.rename(columns={
    'product': 'item',
    'price': 'unit_price'
})

# Reset index
df2 = df2.reset_index(drop=True)

print("\nFinal DataFrame after renaming and resetting index:")
print(df2)



#-------Section: GroupBy & Aggregation---------
# 8) Using the Data from df
result = df.groupby('department').agg({
    'salary': 'mean',
    'age': 'max',
    'name': 'count'
})

print("\nGroupby and Aggeration result:")
print(result)



# 9) Highest paid salary in each department:
idx = df.groupby('department')['salary'].idxmax()
highest_paid = df.loc[idx, ['department', 'name', 'salary']]

print("\nHighest paid Employee in each department:")
print(highest_paid)





#-------Merging & Joining------------
# 10)
df_employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "Diana"]
})

df_salaries = pd.DataFrame({
    "emp_id": [1, 2, 3, 5],
    "salary": [50000, 60000, 75000, 80000]
})

# Inner join: Only employees who have matching emp_id in Both tables
inner_join = df_employees.merge(df_salaries, on='emp_id', how='inner')

print("\nInner Join:")
print(inner_join)   # emp 4 is removed because no salary record and emp 5 is removed bcoz no employee record


# left join + Fill missing salary with 0
left_join = df_employees.merge(df_salaries, on='emp_id', how='left')
left_join['salary'] = left_join["salary"].fillna(0)

print("\nLeft Join (with missing value filled as 0):")
print(left_join)
# emp 4 remains bcoz with salary = 0 9after fillna; emp 5 is not included bcoz it's not in the left table






#----------Real-World ML Thinking-----------------------

# 11) Create the fake data (100 rows)
import numpy as np

np.random.seed(42)    # It locks the random no. generator so you get the same output

n = 100

data = {
    'feature_1': np.random.rand(n),
    'feature_2': np.random.randint(1, 101, n),
    'feature_3': np.random.choice(["A", "B", "C"], n),
    'target': np.random.randint(0, 2, n)
}

df = pd.DataFrame(data)

# what % of rows have feature_1 > 0.8
percentage = (df['feature_1'] > 0.8).mean() * 100
print(f"\nPercentage of rows with feature_1 > 0.8: {percentage:.2f}%")

# Class balance of target (% of 0svs 1s)
class_balance = df['target'].value_counts(normalize=True) * 100
print(f"\nClass balance: {class_balance}")

# How any unique values does feature_3 have
unique_count = df['feature_3'].nunique()
print(f"\nUnique values in feature_3: {unique_count}")


# Correletaion between feature_1 and feature_2
coorelation = df['feature_1'].corr(df['feature_2'])
print(f"\nCoorelation between feature_1 and feature_2: {coorelation}")







# 12) Create clean data (50 rows)
np.random.seed(42)

data = {
    'age': np.random.randint(20, 60, 50),
    'salary': np.random.randint(30000, 120000, 50),
    'department': np.random.choice(['HR', 'IT', 'Finance', 'Marketing'], 50)
}

df_3 = pd.DataFrame(data)

# Inject Data Quality issues

# Duplicate 4 rows
duplicates = df_3.sample(4, random_state=42)
df_3 = pd.concat([df_3, duplicates], ignore_index=True)

# set 5 random 'age' column to null
null_indices = np.random.choice(df_3.index, 5, replace=False)
df_3.loc[null_indices, 'age'] = None

# set 3 random rows in salary to -999
sentinel_indices = np.random.choice(df_3.index, 3, replace=False)
df_3.loc[sentinel_indices, 'salary'] = -999


print("\n=== Data Quality Report ===\n")


# A. column with null values
null_counts = df_3.isnull().sum()
for col, count in null_counts.items():
    if count > 0:
        print(f"CRITICAL: column '{col}' has {count} null values")


# B. Rows containg -999
sentinel_count = (df_3 == -999).any(axis=1).sum()
if sentinel_count > 0:
    print(f"\nWARNING: {sentinel_count} rows contain sentinel value -999")


# C. Duplicate rows
duplicate_count = df_3.duplicated().sum()
if duplicate_count > 0:
    print(f"\nWARNING: {duplicate_count} duplicate rows detected")






# 13) DataFrame representing model predictions:
actual = pd.Series([1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1])
predicted = pd.Series([1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1])

df = pd.DataFrame({'actual': actual, 'predicted': predicted})

# Accuracy
correct = (actual == predicted).sum()
accuracy = (correct/len(actual)) * 100
print(f"\nAccuracy: {accuracy:.2f}%")

# False positives (predicted 1, actual 0)
fp = ((predicted == 1) & (actual == 0)).sum()
print(f"\nFalse positives: {fp}")

# False negatives (predicted 0, actual 1)
fn = ((predicted == 0) & (actual == 1)).sum()
print(f"\nFalse negatives: {fn}")

# adding a column correct
df['correct'] = df['actual'] == df['predicted']

# adding a column error_type
conditions = [
    (df['predicted'] == 1) & (df['actual'] == 0),
    (df['predicted'] == 0) & (df['actual'] == 1)
]

choices = ['fp', 'fn']

df['error_type'] = np.select(conditions, choices, default='correct')

print(df)
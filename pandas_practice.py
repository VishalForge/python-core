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

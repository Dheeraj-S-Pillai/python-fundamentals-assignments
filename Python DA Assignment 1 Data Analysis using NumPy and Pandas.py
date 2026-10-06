import numpy as np
import pandas as pd

# PART 1: NUMPY ARRAY OPERATIONS

# Creating a 1D NumPy array (Week 1 temperatures)
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print("Week 1 temperatures:", temperatures_w1)
print("\n")

# Inspection and properties 

print("Shape:", temperatures_w1.shape)
print("Data type:", temperatures_w1.dtype)
print("Number of elements:", temperatures_w1.size)
print("\n")

# Array operations
temperatures_f = (temperatures_w1 * 9 / 5) + 32
print("Temperatures in Fahrenheit:", temperatures_f)

print("Maximum:", temperatures_w1.max())
print("Minimum:", temperatures_w1.min())
print("Mean:", temperatures_w1.mean())
print("\n")

# Slicing and indexing 

print("First three days:", temperatures_w1[:3])
print("Weekend (last two days):", temperatures_w1[-2:])
print("Middle three days:", temperatures_w1[2:5])
print("\n")

temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],   
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]    
])
print("2D temperatures array:")
print(temperatures)
print("\n")

# Inspect and slice the 2D array
print("Shape:", temperatures.shape)
print("Data type:", temperatures.dtype)
print("Total number of elements:", temperatures.size)
print("\n")

print("Week 1 temperatures:", temperatures[0])
print("Week 2 temperatures:", temperatures[1])
print("Weekend of both weeks (last two days):")
print(temperatures[:, -2:])
print("\n")


# PART 2: PANDAS SERIES

# Creating a Series with custom index labels
marks = pd.Series([95, 92, 89, 85, 80],
                  index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])
print("Marks Series:")
print(marks)
print("\n")

# Indexing and slicing

print("Mark of 1st rank student:", marks.iloc[0])

print("Top 3 ranks using loc:")
print(marks.loc['Rank1':'Rank3'])

print("Mark of 3rd rank student using iloc:", marks.iloc[2])

print("Ranks where marks are greater than 90:")
print(marks[marks > 90])
print("\n")

# Manipulating the Series 

marks['Rank1'] = 100
print("After modifying Rank1 to 100:")
print(marks)
print("\n")

marks = marks.drop('Rank5')
print("After removing Rank5:")
print(marks)
print()

cgpa = marks / 10
print("CGPA:")
print(cgpa)
print("\n")

# PART 3: PANDAS DATAFRAME

# Creating the DataFrame

transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture',
                        'Clothing', 'Electronics', 'Furniture', 'Clothing',
                        'Furniture', 'Electronics'],
    'Region': ['North', 'South', 'North', 'East', 'West',
               'North', 'East', 'West', 'South', 'North'],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

# Data exploration 
print("Transactions DataFrame:")
print(transactions)
print("\n")

print("First 5 rows (head):")
print(transactions.head())
print("\n")

print("Last 5 rows (tail):")
print(transactions.tail())
print("\n")

print("Shape (rows, columns):", transactions.shape)
print("Column names:", list(transactions.columns))
print("\n")

print("Data types:")
print(transactions.dtypes)
print("\n")

print("Basic info:")
transactions.info()
print("\n")

print("ProductCategory and Amount columns:")
print(transactions[['ProductCategory', 'Amount']])
print("\n")

print("Last 3 columns:")
print(transactions.iloc[:, -3:])
print("\n")

print("Region is North AND Amount greater than 200:")
print(transactions[(transactions['Region'] == 'North') & (transactions['Amount'] > 200)])
print("\n")

print("Value counts of ProductCategory:")
print(transactions['ProductCategory'].value_counts())
print("\n")

print("Unique values in Region:", transactions['Region'].unique())
print("\n")

print("Mean Amount for each Region:")
print(transactions.groupby('Region')['Amount'].mean())
print("\n")

# Manipulating the DataFrame

transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165
print("After updating Amount of TransactionID 102 to 165:")
print(transactions)
print("\n")

transactions['Discount'] = transactions['Amount'] * 0.10
print("After adding Discount column:")
print(transactions)
print("\n")

transactions = transactions[transactions['TransactionID'] != 109]
print("After removing TransactionID 109:")
print(transactions)
print("\n")

transactions = transactions.drop('Discount', axis=1)
print("After deleting Discount column:")
print(transactions)

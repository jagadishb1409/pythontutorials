import pandas as pd

# Read data from Excel file
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Print the first 5 rows
print(df.head())


import pandas as pd
# Create a DataFrame
data = {'Name': ['John', 'Jane', 'Bob', 'Sue'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)
# Write data to Excel file
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# Print a message
print('Data written to Excel file.')


import pandas as pd

# Read data from Excel file
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Filter data based on condition
filtered_data = df[df['Age'] > 30]

# Print the filtered data
print(filtered_data)

import pandas as pd

# Read data from Excel file
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Group data by "Gender" column and calculate the mean of the "Age" column for each group
grouped_data = df.groupby('Gender')['Age'].mean()

# Print the grouped data
print(grouped_data)

import pandas as pd

# Read data from Excel file
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Sort data by "Age" column in ascending order
sorted_data = df.sort_values('Age')

# Print the sorted data
print(sorted_data)


import pandas as pd

# Read data from Excel file
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Aggregate data by "Gender" column and calculate the mean and standard deviation of the "Age" column for each group
agg_data = df.groupby('Gender')['Age'].agg(['mean', 'std'])

# Print the aggregated data
print(agg_data)



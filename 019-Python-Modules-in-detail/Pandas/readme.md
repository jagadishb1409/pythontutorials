# Pandas

Pandas is a popular Python library for data manipulation and analysis. It is widely used in fields such as data science, finance, and economics, among others. As a first-year engineering student, you may encounter Pandas in your coursework, and understanding its features and functions can help you effectively analyze data.

In this blog post, we will explore Pandas in detail, covering its key features, data structures, and basic operations.

## Data Structures in Pandas

Pandas provides two main data structures for data manipulation: Series and DataFrame.

Series: A Series is a one-dimensional labeled array that can hold data of any type. It can be created from a list, tuple, or dictionary, and can be indexed and sliced like a NumPy array.

DataFrame: A DataFrame is a two-dimensional table that consists of rows and columns, where each column can have a different data type. It can be created from a list of dictionaries, a NumPy array, or a CSV file.

Basic Operations in Pandas

Pandas provides various functions to perform basic operations on data, such as filtering, sorting, grouping, and aggregating. Let's discuss some of these functions:

Filtering: Pandas provides the ability to filter data based on certain conditions. For example, to filter a DataFrame based on a specific column value, you can use the loc function. Here's an example:

````python
import pandas as pd

df = pd.read_csv('data.csv')
filtered_df = df.loc[df['column_name'] == 'value']
````

Sorting: You can sort data in a DataFrame using the sort_values function. Here's an example:

````python
import pandas as pd

df = pd.read_csv('data.csv')
sorted_df = df.sort_values(by='column_name')
````

Grouping: Pandas allows you to group data based on one or more columns using the groupby function. Here's an example:

````python
import pandas as pd

df = pd.read_csv('data.csv')
grouped_df = df.groupby(['column_name_1', 'column_name_2']).mean()
````

Aggregating: You can perform various aggregations on grouped data, such as mean, sum, and count, using the agg function. Here's an example:

````python
import pandas as pd

df = pd.read_csv('data.csv')
grouped_df = df.groupby(['column_name_1', 'column_name_2']).agg({'column_name_3': 'mean', 'column_name_4': 'sum'})
````

## Using the CoinGecko API to Fetch and Save Blockchain Data as a CSV File Using Python and Pandas.

````python
import requests
import pandas as pd

# Set the API endpoint URL for Bitcoin
url = 'https://api.coingecko.com/api/v3/coins/bitcoin'

# Fetch data from the API
response = requests.get(url)

# Convert the response to a JSON object
data = response.json()

# Create a Pandas DataFrame from the JSON data
df = pd.json_normalize(data)

# Save the DataFrame as a CSV file
df.to_csv('bitcoin_data.csv', index=False)

# Print a success message
print('Bitcoin data saved to bitcoin_data.csv')
````

In this code, we first import the necessary libraries - requests and pandas. We then set the API endpoint URL for Bitcoin using the CoinGecko API. We make a request to the API using the requests.get() function, which returns a response object. We convert the response to a JSON object using the .json() method.

Next, we create a Pandas DataFrame from the JSON data using the pd.json_normalize() function. We then save the DataFrame as a CSV file using the .to_csv() method, with the index=False parameter to exclude the index column from the output. Finally, we print a message indicating that the data has been saved successfully.

This code fetches and saves Bitcoin data from the CoinGecko API, but you can easily customize it to fetch data for other cryptocurrencies or blockchain projects by changing the API endpoint URL. You can also modify the output file name and directory by specifying a different file path in the .to_csv() method.


## Conclusion

In this blog post, we've covered some of the key features and functions of Pandas, including its data structures, basic operations, and more. As a first-year engineering student, understanding Pandas can help you effectively manipulate and analyze data in your coursework and future projects. Happy coding!

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

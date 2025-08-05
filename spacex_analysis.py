
import requests
import pandas as pd

# Fetch SpaceX Launches
url = 'https://api.spacexdata.com/v4/launches'
response = requests.get(url)

if response.status_code != 200:
    raise Exception("Failed to fetch SpaceX data!")

data = response.json()

# Convert to DataFrame
launches = pd.json_normalize(data)

# Show the column names to understand structure
print("Available columns:", launches.columns.tolist())

# Extract only required columns
required_columns = ['name', 'date_utc', 'success', 'rocket']
existing_columns = [col for col in required_columns if col in launches.columns]

print("\nSample Launch Data:")
print(launches[existing_columns].head())

# Save to CSV
launches.to_csv("spacex_launches.csv", index=False)
print("\nCSV file saved successfully.")

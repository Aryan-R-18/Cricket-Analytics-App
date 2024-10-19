import pandas as pd

# Load the dataset
df = pd.read_csv('odibat.csv')

# Convert relevant columns to numeric, forcing errors to NaN
df['Runs'] = pd.to_numeric(df['Runs'], errors='coerce')
df['Mat'] = pd.to_numeric(df['Mat'], errors='coerce')
df['Inns'] = pd.to_numeric(df['Inns'], errors='coerce')
df['SR'] = pd.to_numeric(df['SR'], errors='coerce')

# Drop columns that are not needed
df.drop(columns=['Unnamed: 0', 'Unnamed: 13'], inplace=True)

# Display the cleaned DataFrame and check for any NaN values
print(df.head())
print(df.isnull().sum())  # Check for NaN values

import matplotlib.pyplot as plt

# Select the top 5 players by runs
top_players = df.nlargest(5, 'Runs')


# Fill NaN values with 0
df.fillna(0, inplace=True)

# Display the cleaned DataFrame
print(df.head())

import matplotlib.pyplot as plt

# Select the top 5 players by runs
top_players = df.nlargest(5, 'Runs')

# Create a bar plot
import matplotlib.pyplot as plt

# Convert Runs to numeric if not done already
df['Runs'] = pd.to_numeric(df['Runs'], errors='coerce')

# Get top 10 players by Runs
top_players = df.nlargest(10, 'Runs')

# Create a bar plot
plt.figure(figsize=(12, 6))
plt.barh(top_players['Player'], top_players['Runs'], color='skyblue')
plt.xlabel('Runs')
plt.title('Top 10 Players by Runs')
plt.gca().invert_yaxis()  # To display the highest at the top
plt.show()


df['Runs'] = pd.to_numeric(df['Runs'], errors='coerce')

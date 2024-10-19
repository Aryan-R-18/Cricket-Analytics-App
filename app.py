import streamlit as st
import pandas as pd

# Load your data
df = pd.read_csv('odibat.csv')  # Update with your file path
st.title('Cricket Player ODI Stats')
st.write(df.head())  # Display the first few rows of the dataframe

player = st.selectbox('Select Player', df['Player'].unique())
filtered_data = df[df['Player'] == player]
st.write(filtered_data)

# Example: Convert 'Runs' column to numeric
df['Runs'] = pd.to_numeric(df['Runs'], errors='coerce')  # This will convert non-numeric values to NaN

import matplotlib.pyplot as plt

st.subheader('Player Performance')
fig, ax = plt.subplots()
ax.bar(filtered_data['Inns'], filtered_data['Runs'])
st.pyplot(fig)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have your DataFrame 'df' ready
# Sample data for plotting
# Replace this with your actual DataFrame
data = {
    'Player': ['SR Tendulkar', 'KC Sangakkara', 'RT Ponting'],
    'Runs': [18426, 14234, 13704],
    'Matches': [463, 404, 375],
}
df = pd.DataFrame(data)

# Line Graph
st.subheader('Runs Over Matches')
plt.figure(figsize=(10, 5))
plt.plot(df['Player'], df['Runs'], marker='o')
plt.title('Runs Scored by Players')
plt.xlabel('Players')
plt.ylabel('Runs')
plt.grid()
st.pyplot(plt)

# Pie Chart
st.subheader('Runs Distribution')
plt.figure(figsize=(8, 8))
plt.pie(df['Runs'], labels=df['Player'], autopct='%1.1f%%')
plt.title('Runs Distribution Among Players')
st.pyplot(plt)


player1 = st.selectbox('Select First Player', df['Player'].unique())
player2 = st.selectbox('Select Second Player', df['Player'].unique())



import streamlit as st
import pandas as pd

# Expanded sample data for players with consistent lengths
data = {
    'Player': [
        'SR Tendulkar (INDIA)', 
        'KC Sangakkara (Asia/ICC/SL)', 
        'RT Ponting (AUS/ICC)', 
        'ST Jayasuriya (Asia/SL)', 
        'DPMD Jayawardene (Asia/SL)',
        'AB de Villiers (SA)', 
        'Brian Lara (WI)', 
        'Virat Kohli (INDIA)', 
        'Rohit Sharma (INDIA)', 
        'Jacques Kallis (SA)',
        'Inzamam-ul-Haq (PAK)', 
        'M. S. Dhoni (INDIA)', 
        'Shane Warne (AUS)', 
        'Sachin Baby (INDIA)', 
        'Chris Gayle (WI)'
    ],
    'Mat': [463, 404, 375, 445, 448, 228, 131, 254, 227, 328, 378, 350, 194, 124, 301],
    'Runs': [18426, 14234, 13704, 13430, 12650, 9577, 10405, 12809, 9203, 11579, 11739, 10773, 350, 236, 331],
    '100': [49, 25, 30, 28, 19, 25, 19, 43, 30, 24, 10, 10, 0, 0, 1],
    '50': [96, 93, 82, 68, 77, 53, 48, 62, 44, 49, 45, 73, 0, 2, 2],
}

# Make sure each list has the same length
if all(len(value) == len(data['Player']) for value in data.values()):
    df = pd.DataFrame(data)
else:
    raise ValueError("All lists in the data dictionary must have the same length.")

# Title
st.title('Cricket Player Comparison')

# Player selection
players = df['Player'].tolist()
selected_players = st.multiselect('Select Players to Compare:', players, default=players[:2])  # Defaulting to the first two players

# Filter DataFrame based on selection
comparison_df = df[df['Player'].isin(selected_players)]

# Check if two players are selected
if len(comparison_df) == 2:
    # Display comparison table
    st.subheader('Comparison Table')
    st.table(comparison_df[['Player', 'Mat', 'Runs', '100', '50']])
else:
    st.warning('Please select exactly 2 players to compare.')

# You can add additional visualizations or stats below as needed


# You can add additional visualizations or stats below as needed



player1_data = df[df['Player'] == player1]
player2_data = df[df['Player'] == player2]

# Add comparison logic here

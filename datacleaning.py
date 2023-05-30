import pandas as pd
import json

# Load the CSV data
df1 = pd.read_csv('dataset/Eurovision Winners - Winner Data KG-3.csv')

# Remove the quotation marks from the 'song' entries
df1['Song'] = df1['Song'].str.replace('"', '')

# Save the cleaned CSV data to a new CSV file
df1.to_csv('newdata/cleaned_winner_data.csv', index=False)

# Load the JSON data
with open('dataset/eurovision-lyrics-2022.json') as f:
    data = json.load(f)

# Convert the data to a list of dictionaries
data_list = [v for k, v in data.items()]

# Create a DataFrame from the list
df2 = pd.DataFrame(data_list)

# If 'Lyrics translation' is "English", replace it with the value in 'Lyrics'
df2.loc[df2['Lyrics translation'] == 'English', 'Lyrics translation'] = df2['Lyrics']

# Rename the "Lyrics translation" column to "English Lyrics"
df2.rename(columns={'Lyrics translation': 'English Lyrics'}, inplace=True)

# Select only the 'Song' and 'English Lyrics' columns
df2 = df2[['Song', 'English Lyrics']]

# Save the lyrics dataset to a new CSV file
df2.to_csv('newdata/lyrics_data.csv', index=False)

# Load and print the first few rows of the cleaned CSV data
df1 = pd.read_csv('newdata/cleaned_winner_data.csv')
print(df1.head())

# Load and print the first few rows of the lyrics CSV data
df2 = pd.read_csv('newdata/lyrics_data.csv')
print(df2.head())

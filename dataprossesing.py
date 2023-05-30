import pandas as pd
import json

# Load the CSV data
df1 = pd.read_csv('dataset/Eurovision Winners - Winner Data KG-3.csv')

# Remove the quotation marks from the 'song' entries
df1['Song'] = df1['Song'].str.replace('"', '')

# Load the JSON data
with open('dataset/eurovision-lyrics-2022.json') as f:
    data = json.load(f)

# Convert the data to a list of dictionaries
data_list = [v for k, v in data.items()]

# Create a DataFrame from the list
df2 = pd.DataFrame(data_list)

# Merge the datasets on the "Song" column
merged_df = pd.merge(df1, df2, left_on='Song', right_on='Song', how='inner')

# Check if 'Lyrics translation' is "English", if so, replace it with the value in 'Lyrics'
merged_df.loc[merged_df['Lyrics translation'] == 'English', 'Lyrics translation'] = merged_df['Lyrics']

# Rename the "Lyrics translation" column to "lyrics"
merged_df.rename(columns={'Lyrics translation': 'English Lyrics'}, inplace=True)

# Select only the 'lyrics', 'song', and 'Year' columns
merged_df = merged_df[['Song', 'English Lyrics']]

# Save the merged dataset to a new CSV file
merged_df.to_csv('newdata/merged.csv', index=False)

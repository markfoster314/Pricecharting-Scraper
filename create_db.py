import pandas as pd
import sqlite3

# Load from CSV (or JSON with pd.read_json)
df = pd.read_csv('gamegear_prices.csv')
# Clean prices: Remove '$' and convert to float
#for col in ['Loose Price', 'CIB Price', 'New Price']:
#    df[col] = df[col].str.replace('$', '').str.replace(',', '').astype(float)

conn = sqlite3.connect('gameprices.db')  # Creates local DB file
df.to_sql('games', conn, if_exists='replace', index=False)
conn.close()
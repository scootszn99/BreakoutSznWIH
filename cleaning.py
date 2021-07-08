import numpy as np
import pandas as pd
from pandas import DataFrame
import os

# reading in data
df = pd.read_csv("pick224data.csv")

# sorting dataframe by player and season to get groupings
df = df.sort_values(['UNIQUE ID', 'SEASON'], kind='mergesort')

# filtering out defenders
df = df[df['POS'] == "F"]

# creating a new variable for each row flagging if it's a breakout season
df['Breakout Season'] = np.where(df['P1/e60'] >= df['P1/e60'].shift(1) + 0.5, True, False)
df.loc[df['UNIQUE ID'] != df['UNIQUE ID'].shift(1), "Breakout Season"] = False

# code to see seasons that occur before a player's breakout season
# df = df.reset_index(drop=True)
# indices = df[df['Breakout Season'] == True].index-1
# df = df.loc[indices]

# can you have more than one breakout season????
# df = df.drop_duplicates(subset=['UNIQUE ID'])

# exporting normal dataset
df.to_csv('normal.csv', index=False)

# exporting three season dataset without advanced numbers
df2 = df[df['SEASON'] >= 2019]
df2.to_csv('threeseason.csv', index=False)
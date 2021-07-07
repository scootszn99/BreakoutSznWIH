import numpy as np
import pandas as pd
from pandas import DataFrame
import os

# reading in data
df = pd.read_csv("pick224data.csv")

# sorting dataframe by player and season to get groupings
df = df.sort_values(['UNIQUE ID', 'SEASON'], kind='mergesort')

# creating a new variable for each row flagging if it's a breakout season
df['Breakout Season'] = np.where(df['P1/e60'] >= df['P1/e60'].shift(1) + 0.5, True, False)
df.loc[df['UNIQUE ID'] != df['UNIQUE ID'].shift(1), "Breakout Season"] = False

df = df.reset_index(drop=True)
indices = df[df['Breakout Season'] == True].index-1
df = df.loc[indices]
df = df[df['POS'] == "F"]
df = df.drop_duplicates(subset=['UNIQUE ID'])

df

# df.to_csv('breakoutcalculator.csv', index=False)
# This code adds a flag 'Regulated' to the output to classify genes based on their 
# regulation level into Up/Down. A Z score cutoff of 1.65 equivalent to 95 % CI is used 
# for this purpose.

import pandas as pd

cutoff 			= 1.65
table 			= 	pd.read_csv('plosone.csv')#.dropna()
data 			= 	table['HUVEC']
table['zscore'] = (data - data.mean())/data.std(ddof=0)


table.loc[table['zscore'] > cutoff, 'Regulation'] = 'UP'
table.loc[table['zscore'] < -1*cutoff, 'Regulation'] = 'Down'

table.to_csv('Regulation.csv', sep=',', index = False)


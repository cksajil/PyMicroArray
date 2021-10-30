import pandas as pd

data 	= 	pd.read_csv('Edited_DownRegulatedGene_MiRNA.csv', index_col=0).iloc[:,[0,1,3,4]]

data 	= 	data.drop_duplicates(['miRNA', 'Target Gene'])

data.to_csv('Unique_DownRegulatedGene_MiRNA.csv', sep=',')


import pandas as pd
import numpy as np

data = pd.read_csv('Homo_sapiens.csv', low_memory=False)
data = data[['GeneID','Description']]

result = pd.DataFrame(columns = ['GeneID','Description'])

genes = np.loadtxt('input_hsa-miR-126-3p.txt')

for gene in genes:
	result.loc[len(result)] =  data[data['GeneID'] == gene].values[0]
	#print data[data['GeneID'] == gene].values[0]


result.to_csv('Output_hsa-miR-126-3p.csv', sep=',', index = False)
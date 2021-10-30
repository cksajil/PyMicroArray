import pandas as pd
import numpy as np
from os import listdir, curdir, path

data = pd.read_excel(open('Homo_sapiens.xlsx','rb'), sheetname=0)
data = data[['GeneID','type_of_gene']]

col = ['id', 'attribute']

files = listdir(curdir)

for file in files:
	if '.txt' in file:
		genes = np.loadtxt(file)
		result = pd.DataFrame(columns = col)
		for gene in genes:
			result.loc[len(result)] =  data[data['GeneID'] == gene].values[0]
		result.to_csv(path.splitext(file)[0]+'_Out.csv', sep=',', index = False)

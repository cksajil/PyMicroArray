import pandas as pd
import numpy as np
from pandas import ExcelWriter

	
data		= 		pd.read_excel(open('GSE49426_average_input.xlsx','rb'), sheetname=0, index=False).drop('ID_REF', axis=1)
columns 	= 		list(data)
result 		= 		pd.DataFrame(columns = columns)
genes 		= 		list(set(data['Gene_Symbol'].values))


for gene in genes:
	row = data[data['Gene_Symbol']==gene]
	repeat = row.shape[0]
	if repeat>1:
		Vc = np.mean(row['VALUE_control'])
		V6 = np.mean(row['VALUE_60min'])
		Ratio = V6/Vc
		Fc = np.log2(Ratio)
		value = [row['Gene_Title'].values[0], gene, row['ENTREZ_GENE_ID'].values[0], Vc, V6, Ratio, Fc]
		result.loc[len(result)] =  value
	else:
		result.loc[len(result)] = row.values[0]

writer = ExcelWriter('GSE49426_average_gene_expression_out.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()

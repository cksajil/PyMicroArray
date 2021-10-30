import pandas as pd
import numpy as np
from pandas import ExcelWriter

	
data		= 		pd.read_excel(open('Proteome_data_cell_fractions_combined.xlsx','rb'), sheetname=0, index=False)
columns 	= 		['UNIPROT', 'SYMBOL', 'GENENAME', 'UNTREATED', 'VEGF', 'Ratio', 'FC']
result 		= 		pd.DataFrame(columns = columns)
genes 		= 		list(set(data['SYMBOL'].values))


for gene in genes:
	row = data[data['SYMBOL']==gene]
	repeat = row.shape[0]
	if repeat>1:
		Vc = np.mean(row['VEGF'])
		V6 = np.mean(row['UNTREATED'])
		if V6==0:
			Ratio ='Inf'
			Fc    ='Inf'
		else: 
			Ratio = Vc/V6
			Fc = np.log2(Ratio)
		value = [row['UNIPROT'].values[0], gene, row['GENENAME'].values[0], V6, Vc, Ratio, Fc]
		result.loc[len(result)] =  value
	else:
		row = row.values[0].tolist()
		if row[-2]==0:
			Ratio ='Inf'
			Fc    ='Inf'
		else:
			Ratio = row[-1]/row[-2]
			Fc = np.log2(Ratio)
		row = row+[Ratio, Fc]
		result.loc[len(result)] = row

writer = ExcelWriter('Proteome_Profile_MeanCalculated_FC.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()

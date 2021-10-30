import pandas as pd
import numpy as np
from pandas import ExcelWriter
from time import time
import progressbar

InputFileName 	= 		'GEO2R ANALYSIS  GSE81465.xlsx'
data			= 		pd.read_excel(open(InputFileName,'rb'), sheet_name=0, index=False)
result 			= 		pd.DataFrame(columns = data.columns)
genes 			= 		list(set(data['Gene.symbol'].values))
count 			=		0
L 				=		len(genes)

with progressbar.ProgressBar(max_value=L) as bar:
	for gene in genes:
		count+=1
		row = data[data['Gene.symbol']==gene]
		repeat = row.shape[0]
		if repeat>1:
			Fc = np.mean(row['logFC'])
			value = [row['Gene.symbol'].values[0], Fc]
			result.loc[len(result)] =  value
		else:
			result.loc[len(result)] = row.values[0]
		bar.update(count)
	
writer = ExcelWriter(InputFileName.split('.')[0]+'_Output.xlsx')
result.to_excel(writer,'Sheet1',index=False)
writer.save()

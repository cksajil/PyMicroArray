# Program to retrieve gene deatails from NCBI dataset.


import pandas as pd

data = pd.read_csv('Homo_sapiens.csv', low_memory=False)
data = data[['Symbol', 'Synonyms', 'type_of_gene']]

genes = pd.read_excel(open('GSE837_DEGs_GSEA.xlsx','rb'), sheetname=0)['Total_DEG_GSE837_GSEA'].values

col = ['Symbol', 'Synonyms', 'type_of_gene']
result = pd.DataFrame(columns = col)



for index, row in data.iterrows():
	if row.values[1]!='-':
		line = row.values[0]+'|'+row.values[1]
	else:
		line = row.values[0]
	line = line.split('|')

	for gene in genes:
		if gene in line:
			result.loc[len(result)] = row.values

	# for item in line:
	# 	if item in genes:
	# 		result.loc[len(result)] = row.values


writer = pd.ExcelWriter('GSE837_DEGs_GSEA_Genetype_Out.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()

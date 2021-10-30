import pandas as pd

data		= 	pd.read_excel(open('AngiogenisisGeneAnnotation_Genes.xlsx','rb'), sheetname=0)
checklist	= 	pd.read_excel(open('Common_genes_out_unique_DEGs_C13_SKOV3_Angiogenesis_process_GO_consortium.xlsx','rb'), sheetname=0)['Common_genes']
result 		= 	pd.DataFrame()
cols 		= 	data.columns

print 'Common items are:\n'

for item in cols:
	common =  pd.Series(list(set(checklist).intersection(set(data[item]))))
	result[item] = common
	print item
	print common.to_string(index=False)
	print '\n'

writer = pd.ExcelWriter('Common_Angio_Annotation_SOC_cell_line.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()

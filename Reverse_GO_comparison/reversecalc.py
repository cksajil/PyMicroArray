import pandas as pd

data		= 	pd.read_excel(open('AngiogenisisGeneAnnotation_Genes.xlsx','rb'), sheetname=0)
checklist	= 	pd.read_excel(open('Total_DEGs_GSE71216_RNAseq.xlsx','rb'), sheetname='Final_DEGs_GSE71216')['DEGs_GSE71216']
result 		= 	pd.DataFrame()
cols 		= 	data.columns

print 'Common items are:\n'

for item in cols:
	common =  pd.Series(list(set(checklist).intersection(set(data[item]))))
	result[item] = common
	print item
	print common.to_string(index=False)
	print '\n'

writer = pd.ExcelWriter('Common_Angio_Annotation_GSE71216.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()

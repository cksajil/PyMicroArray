import pandas as pd


data 			= 		pd.read_excel(open('Angiogenesis_genes_GO_consortium.xlsx','rb'), sheetname=0)
genes 			= 		pd.read_excel(open('Total_DEGs_GSE837.xlsx','rb'), sheetname='Final_DEGs_p<0.05_GSE837_G2Rpro')

series1			= 		data['Gene_symbol'].tolist()	
series2			= 		data['Synonyms']	
series2 		= 		series2[~series2 .isnull()].tolist()
lookup_series 	= 		series1+series2
data 			= 		genes[genes['Gene_symbol'].isin(lookup_series)]


writer = pd.ExcelWriter('Common_Out_Angiogenesis_GO_Total_DEGs_GSE837.xlsx')
data.to_excel(writer,'Sheet1')
writer.save()



import pandas as pd
from pandas import ExcelWriter

data 	= 	pd.read_excel(open('Total_DEGs_Clear_cell_carcinoma.xlsx','rb'), sheetname=0)
genes 	= 	pd.read_csv('Common_genes_unique_DEGs_CCC_Cell_line_VEGF_pathway.txt').values.flatten()

print genes


result	= data[data['gene'].isin(genes)]

writer = ExcelWriter('Common_genes_VEGF_pathway_FoldChangeGeneInfo_Clear_cell_carcinoma.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()


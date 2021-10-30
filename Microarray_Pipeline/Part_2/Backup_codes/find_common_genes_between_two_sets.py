import pandas as pd
from pandas import ExcelWriter

data1 = pd.read_excel(open('Cytoplasmic_proteome_profile.xlsx','rb'), sheetname='Total_DE_proteins')['SYMBOL'].values
data2 = pd.read_excel(open('Total_DEGs_GSE53550_new.xlsx','rb'), sheetname=0)['GeneSymbols'].values

common = set(data1).intersection(data2)

outfile = open('Common_genes_out_DEGs_GSE53550_cytoplasmic_proteome_profile.txt', 'w')
if bool(common):
	outfile.write("\n".join(common))
else:
	outfile.write("No Common Genes Found")
outfile.close()




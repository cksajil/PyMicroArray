import pandas as pd

data 	= 	pd.read_csv('hsa_MTI_MIRTARBASE_DB_7.0.csv').iloc[:,[0,1,3,4]]

genes 	= 	pd.read_csv('RR_total_downregulated_gene_list.txt').values.flatten()
#genes 	= 	pd.read_csv('RR_total_upregulated_gene_list.txt').values.flatten()

result	= data[data['Target Gene'].isin(genes)]

result.to_csv('DownRegulatedGene_MiRNA.csv', sep=',')
#result.to_csv('UPRegulatedGene_MiRNA.csv', sep=',')
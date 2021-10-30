import pandas as pd

data1 = pd.read_csv("Human_TSGs_TSG2.0_database.csv")["GeneSymbol"]
data2 = pd.read_csv("DEGs_SRR926257.csv")["gene_id"]

common = set(data1).intersection(data2)
outfile = open('TSGs_in_DEGs_SRR926257.txt', 'w')
if bool(common):
	outfile.write("\n".join(common))
else:
	outfile.write("No Common Genes Found")
outfile.close()
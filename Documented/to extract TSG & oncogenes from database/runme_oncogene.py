import pandas as pd

data1 = pd.read_csv("ongene_human_Ongene_database.csv")["OncogeneName"]
data2 = pd.read_csv("DEGs_SRR926257.csv")["gene_id"]

common = set(data1).intersection(data2)
outfile = open('oncogene_in_DEGs_SRR926257.txt', 'w')
if bool(common):
	outfile.write("\n".join(common))
else:
	outfile.write("No Common Genes Found")
outfile.close()
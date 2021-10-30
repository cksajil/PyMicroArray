import pandas as pd
data = pd.read_csv("Mirtarbase_human_interactions_database.csv")
result = pd.DataFrame()
match  = data.miRNA.str.contains('^hsa-miR-6807-')
result = data[match]
result.to_csv('mirtarbase_miR-6807_SRR926257.csv', sep=',')
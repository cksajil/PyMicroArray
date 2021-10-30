import pandas as pd
data = pd.read_csv("Mirtarbase_human_interactions_database.csv")
result = pd.DataFrame()
match  = data.miRNA.str.contains('^hsa-miR-103a-')
result = data[match]
result.to_csv('mirtarbase_miR-103a.csv', sep=',')
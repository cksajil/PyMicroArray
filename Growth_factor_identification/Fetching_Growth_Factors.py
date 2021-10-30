import pandas as pd
from pandas import ExcelWriter

dataset 	= 	pd.read_excel(open('Growth_factors_and_receptors_GO_Consortium.xlsx','rb'), sheetname=0)
DEgs        =   pd.read_excel(open('unique_DEGs_LGSOC_HGSOC.xlsx','rb'), sheetname=0)

def word(row):
	first, rest = row.split('_HUMAN')
	rest = rest.split('|')[1:]
	rest.insert(0, first)
	return rest

items = dataset['Synonyms']
parsed = map(word, items)
dataset['Parsed'] = parsed

checklist = dataset['Parsed']
checklist = [item for row in checklist for item in row]

result	= DEgs[DEgs['Unique_gene_list_LGSOC_HGSOC'].isin(checklist)]


writer = ExcelWriter('GF_out_unique_DEGs_HGSOC_LGSOC.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()


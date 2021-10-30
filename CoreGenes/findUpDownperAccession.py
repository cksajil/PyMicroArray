import pandas as pd
from pandas import ExcelWriter
import numpy as np
import itertools

index = pd.read_excel(open('Hierarchy.xlsx','rb'), sheet_name=0, index=False)

accessions = set(index['Accession'])

TotalGenes =[]

for item in accessions:
	data = index[index['Accession']==item]
	filenames =	data['FileName'].values
	subdata = pd.DataFrame()
	for file in filenames:
		fetch = pd.read_excel(file, 'Total_DEGs')
		subdata = subdata.append(fetch)
	
	UpRegulated 	= 	subdata[subdata['LFC']>=1]
	DownRegulated 	= 	subdata[subdata['LFC']<=1]
	writer = ExcelWriter('Mixed/'+item+'.xlsx')
	subdata.to_excel(writer,'Total_DEGs', index=False)
	UpRegulated .to_excel(writer,'UpRegulated', index=False)
	DownRegulated .to_excel(writer,'DownRegulated', index=False)
	writer.save()


####################### Extra #######################################

# TotalGenes.append(subdata['Gene Symbol'].values)
# result = set(TotalGenes[0])
# for s in TotalGenes[1:]:
#     result.intersection_update(set(s))
# print "Common Genes Amoung all DataSets :"
# print result


# flat_list 	= [item for sublist in TotalGenes for item in sublist]
# TotalGenes 	= list(set(flat_list))
# common = pd.DataFrame()
# common['UniqueGenes']=TotalGenes

# writer = ExcelWriter('Results/Unique_Genes.xlsx')
# common.to_excel(writer,'Unique_Genes')
# writer.save()

#########################################################################

# import os
# import pandas as pd
# from pandas import ExcelWriter
# from openpyxl import load_workbook

# files 		= 	os.listdir('Mixed/')
# print files
# masterdata 	= 	pd.DataFrame()

# for file in files:
#     data = pd.read_excel('Mixed/'+file, 'Total_DEGs', index =False)
#     data = data[['Gene Symbol','LFC','Synonyms']]
#     masterdata = masterdata.append(data)

# writer = ExcelWriter('Results/MasterData.xlsx')
# masterdata.to_excel(writer,'Total_DEGs', index =False)
# writer.save()

# UpRegulated 	= 	data[data['LFC']>=1]
# DownRegulated 	= 	data[data['LFC']<=1]


# writernw 			= 	ExcelWriter('Results/MasterData.xlsx', engine='openpyxl')
# book 				= 	load_workbook('Results/MasterData.xlsx')
# writernw.book 		= 	book
# writernw.sheets 	= 	dict((ws.title, ws) for ws in book.worksheets)    

# UpRegulated.to_excel(writernw, 'UpRegulated', index=False)
# DownRegulated.to_excel(writernw, 'DownRegulated', index=False)
# writernw.save()

########################################################################

# N = len(TotalGenes)
# for pair in range(2,N):
# 	print list(itertools.combinations('ABCDEF',pair))
# print set(TotalGenes[0]).intersection(set(TotalGenes[1]))

########################################################################






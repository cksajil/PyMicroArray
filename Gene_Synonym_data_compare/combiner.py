# Read Excel File Names
import pandas as pd
from os import listdir
from pandas import ExcelWriter
from functools import reduce

files 		= 		listdir('.')
files 		=		[file for file in files if '.xlsx' in file]

for file in files:

	family 			= 		'Gene_name_'+file.split('.')[0]
	fields 			= 		[family, 'Synonyms', ]
	sampledata 		= 		pd.read_excel(open(file,'rb'), sheetname=0, usecols=fields)
	sampledata 		= 		sampledata .fillna('-')
	genenames 		= 		sampledata[family]+'|'+sampledata['Synonyms']



	def splitsorter(row):
		row 		= 		row.split('|')
		row 		= 		[item for item in row if item != '-']
		row.sort()
		return '|'.join(row)



	cleanrow			= 		map(splitsorter, genenames)
	sampledata 			= 		sampledata.drop([family,'Synonyms'], axis = 1)
	sampledata[family] 	= 		cleanrow

	# cols 				= 		sampledata.columns.tolist()
	# print cols
	# cols 				= 		cols[-1:]+cols[:2]
	# sampledata 		= 		sampledata[cols]


	writer 				= 		ExcelWriter('Results/Cleaned_'+file)
	sampledata.to_excel(writer,'Sheet1')
	writer.save()

processedfiles 			= 		listdir('Results')


dfList 					= 		[pd.read_excel(open('Results/'+processedfiles[3] ,'rb'), sheetname=0).ix[:,0].unique() for file in processedfiles]
commonitems 			= 		list(reduce(set.intersection, map(set, dfList)))
finaldata				=		pd.DataFrame(commonitems, columns=['Common_Gene_names'])
finalwriter 			= 		ExcelWriter('Results/Common.xlsx')
finaldata.to_excel(finalwriter,'Sheet1')
writer.save()


import pandas as pd
from pandas import ExcelWriter

probes 		= 		pd.read_excel(open('Input_GSE53550_ProbeNames_New.xlsx','rb'), sheetname=0)['Probename']
#probes 		= 		list(pd.read_csv('Input_GSE53550_new.csv')['Probes'])
Output 		= 		pd.read_excel(open('GPL15314_DataBase.xlsx','rb'))
Clean 		= 		Output[Output['ProbeName'].isin(probes)]
result 		= 		pd.DataFrame(columns = ['ProbeName', 'GeneSymbols', 'NCBIids'])



for index, row in Clean.iterrows():
	probename  	=	str(row['ProbeName'])
	gensymbol 	= 	str(row['GeneSymbols'])
	NCBIid 		=	str(row['NCBIids'])

	if '|' in gensymbol :
		gensymbol  = gensymbol.split('|')[0]
	if '|' in NCBIid:
		NCBIid  = NCBIid.split('|')[0]

	result.loc[len(result)] =  [probename, gensymbol, NCBIid]

writer = ExcelWriter('Genename_of_Probes_GSE53550.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()








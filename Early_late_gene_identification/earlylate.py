import pandas as pd
from pandas import ExcelWriter

files 		= 	pd.read_excel(open('Hierarchy.xlsx','rb'), sheet_name=0, index=False)
masterdata 	= 	pd.DataFrame()

for file in files['FileName']:
	data = pd.read_excel(open('Inputs/'+file,'rb'), sheet_name='Total_DEGs', index=False)
	data = data[['Gene Symbol', 'LFC', 'Synonyms']]
	data['Accession'] = files[files['FileName']==file]['Accession'].values[0]
	data['TimeFrame'] = files[files['FileName']==file]['TimePoint'].values[0]
	data['Hour'] 	  = files[files['FileName']==file]['Hour'].values[0]
	masterdata = masterdata.append(data)


TotalGenes 	= 	masterdata['Gene Symbol']
count 		= 	[]

for gene in TotalGenes:
	count.append(masterdata[masterdata['Gene Symbol']==gene].shape[0])
masterdata['Count'] = count

exprStatus = []

for gene in TotalGenes:
	subdata = masterdata[(masterdata['Gene Symbol']==gene)]
	repeats = subdata.shape[0]
	if repeats>1:
		if repeats == sum(subdata['LFC']>1):
			exprStatus.append('AlwaysUP')
		elif repeats == sum(subdata['LFC']<1):
			exprStatus.append('AlwaysDown')
		elif (sum(subdata['LFC']>1)/float(repeats))>0.5:
			exprStatus.append('MostlyUP')
		elif (sum(subdata['LFC']>1)/float(repeats))<0.5:
			exprStatus.append('MostlyDown')
		else:
			exprStatus.append('Oscillating')

	else:
		exprStatus.append('Instant')

masterdata['Dynamics'] = exprStatus


writer = ExcelWriter('Results/MasterData.xlsx')
masterdata.to_excel(writer,'Total_DEGs', index =False)
writer.save()

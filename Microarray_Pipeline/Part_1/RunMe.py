from os import listdir
import pandas as pd
from pandas import ExcelWriter
from openpyxl import load_workbook

accessions 	= 	listdir('DEG_Identification')
hierarchy 	= 	dict()
Timeinfo	= 	dict()
Controls 	=   dict()

print "******* Reading File Structure********* \n"

print str(len(accessions))+ ' Accessions found\n'

for accession in accessions:
	hierarchy[accession] = {'files':listdir('DEG_Identification/'+accession)}
	files = hierarchy[accession]['files']
	Controls[accession]  = [x for x in files if 'Control' in x]

for item in hierarchy:
	files = hierarchy[item]['files']
	times = []
	for dataset in files:
		first, last = dataset.split('_')
		if 'min' in last:
			time = last.split('min')[0]
			times.append(time)
	Timeinfo[item] = {'TimePoints':times}
	print 'Accesion '+item+' has '+str(len(files))+' files and '+str(len(Timeinfo[item]['TimePoints']))+' Time Points\n'

print "******* Removing AFFX Probes from Files ********* \n"


def PreProcessor(item, exlfile):
	path = 'DEG_Identification/'+item+'/'+exlfile
	writer = ExcelWriter(path)

	print 'Removing AFFX Probes from file: '+exlfile+'\n'
	rawdata  = pd.read_excel(open(path,'rb'), sheetname=0, index=False)
	noaffx   = rawdata[~rawdata['Probename'].str.contains('AFFX')]
	for col in noaffx.columns:
		if 'call_' in col:
			key = col
			break
	print 'Filtering Based on P Status from file: '+exlfile
	Ptrue   = noaffx[noaffx[key]=='P']
	
	rawdata.to_excel(writer,'Raw')
	noaffx.to_excel(writer,'NoAFFX')
	Ptrue.to_excel(writer,'ABS_CALL')
	writer.save()


def ControlTreatedUnique(item, expgroup):
	controlfile = Controls[item][0]
	pathc       = 'DEG_Identification/'+item+'/'+controlfile
	for expfile in expgroup:
		print 'Finding Common Probes for File : '+expfile
		pathe = 'DEG_Identification/'+item+'/'+expfile
		exprobes = pd.read_excel(open(pathe,'rb'), sheetname='ABS_CALL', index=False)['Probename']
		controlprobes = pd.read_excel(open(pathc,'rb'), sheetname='ABS_CALL', index=False)['Probename']
		commonprobes = list(set(exprobes) & set(controlprobes))
		expdata  = pd.read_excel(open(pathe,'rb'), sheetname='ABS_CALL', index=False)
		commondf = expdata[expdata['Probename'].isin(commonprobes)]
		writernw = ExcelWriter(pathe, engine='openpyxl')
		book = load_workbook(pathe)
		writernw.book = book
		writernw.sheets = dict((ws.title, ws) for ws in book.worksheets)    
		tme = expfile.split('_')[1].split('.')[0]
		commondf.to_excel(writernw, 'COMMN_'+tme, index=False)
		writernw.save()
		

for item in hierarchy:
	files = hierarchy[item]['files']
	for exlfile in files:
		 PreProcessor(item, exlfile)
		

for item in hierarchy:
	files = hierarchy[item]['files']
	for exlfile in files:
		 expgroup = [expitem for expitem in files if 'Control' not in expitem]
		 ControlTreatedUnique(item, expgroup)





# To combine data from RegNetwork database and TRRUST database.
# Column fileds which needs to be combined can be speccified according to user requirement.
# output will be saved for unique accessions and time points in the results folder.


import pandas as pd
import progressbar



files		= 		pd.read_excel(open('Inputs/list.xlsx','rb'))
Iterations 	= 		list(set(files['Accession']+'_'+files['TimePoint']))
Count 		=		0
L 			=		len(Iterations)

with progressbar.ProgressBar(max_value=L) as bar:

	for iteration in Iterations:
		Accession, TimePoint 	= 		iteration.split('_')
		FilesToCombine 			= 		files[(files['Accession']==Accession) & (files['TimePoint']==TimePoint)]
		RegFile 				=		FilesToCombine[FilesToCombine['DataBase']=='Regnetwork']['FileName'].values[0]
		TRRFile 				=		FilesToCombine[FilesToCombine['DataBase']=='TRRUST']['FileName'].values[0]

		Regdata					=		pd.read_excel(open('Inputs/'+RegFile,'rb'))[['regulator_symbol', 'target_symbol']]
		Regdata.columns 		= 		['TF', 'Target_Gene']
		TRRdata					=		pd.read_excel(open('Inputs/'+TRRFile,'rb'))[['TF', 'Target_Gene']]
		Mixdata					= 		pd.concat([Regdata, TRRdata])
		Mixdata['Interactions'] = 		Mixdata['TF']+'_'+Mixdata['Target_Gene']
		Mixdata 				= 		Mixdata.drop_duplicates(['Interactions'],  keep='first')
		writer 					= 		pd.ExcelWriter('Results/Mixed_'+Accession+'_'+TimePoint+'.xlsx')
		Count 					=		Count+1
		Mixdata.to_excel(writer,'Sheet1')
		writer.save()
		bar.update(Count)

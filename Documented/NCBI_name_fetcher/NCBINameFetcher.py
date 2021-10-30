import pandas as pd
import numpy as np
import requests
import time
import re

genes = np.loadtxt('input_hsa-miR-103a-3p.txt')
col = ['Id', 'Official Full Name']
result = pd.DataFrame(columns = col)
link = 'https://www.ncbi.nlm.nih.gov/gene/'

for gene in genes:

	page = requests.get(link+str(int(gene)))
	if page.status_code == 200:
		content = page.content
		content = content.replace('\n','')
		if content.find('Full Name</dt>'):
			location = content.find('Full Name</dt>')
			term = content[location:location+100]
			if re.search('(.*)(<dd>)(.*)(<span)(.*)', term ):
				name =re.search('(.*)(<dd>)(.*)(<span)(.*)', term )
				attribute = name.group(3)
			else:
				attribute = 'multiple hits'
		else:
			attribute = 'nofield'
	else:
		attribute = 'NA'

	result.loc[len(result)] = [str(int(gene)), attribute]
	#print gene, ',',attribute	
	print str(gene)+'\t'+attribute
	#time.sleep(5)

result.to_csv('Output_hsa-miR-103a-3p.csv', sep=',', index = False)
#with open('Output_hsa-miR-16-5p.csv', 'a') as f:
#    result.to_csv(f, sep=',', index = False)
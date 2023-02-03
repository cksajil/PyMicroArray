## PyMicroArray: A Python Codebase for Gene Expression Analysis

PyMicroArray is a set of scripts written to aid in the data retrieval and analysis of
micro-array expression data. A variety of code snippets which can be used from
data pulling to analysis are made open-source. This might save biologist from a
lot of manual effort and save the time needed.

### Dependencies
* Python 2.7.(Anaconda Distribution)
* Numpy, Scipy, Pandas and Matplotlib.

### How to run the program

### Systems Tested

```console
|OS Linux|Machine|OptiPlex 7010 (OptiPlex 7010)|64 bits|RAM 8GiB|
CPU : Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz

Python Version and Major Packages:
Python 2.7.13 |Anaconda custom (64-bit)
matplotlib==2.0.2,
numpy==1.13.1,
pandas==0.20.1,
pip==9.0.1,
scipy==0.19.1.
```

## PyMicroArray Ver 1.0 Documentation
This code base contains various programs for data retireval, cleaning filtering and analysis.

#### Find the microRNAs regulating the target genes
> PyMicroArray/to find miRNAs of target genes from mirtarbase/

To find the microRNAs regulating the target genes from the MIRTARBASE local database. Given the MIRTARBASE local database and a gene list, this program can findout all down regulated genes from the MIRTARBASE which is in the given gene list.

```python
import pandas as pd
data	=	pd.read_csv('hsa_MTI_MIRTARBASE_DB_7.0.csv').iloc[:,[0,1,3,4]]
genes	=	pd.read_csv('RR_total_downregulated_gene_list.txt').values.flatten()
result	= 	data[data['Target Gene'].isin(genes)]
result.to_csv('DownRegulatedGene_MiRNA.csv', sep=',')
```

The MIRTARBASE local database is available in the file **hsa_MTI_MIRTARBASE_DB_7.0.csv**. We can select the only required fields by specifying the columns needed in the *iloc* field. The result will be saved as a CSV file as given in the last line.

#### Find Common genes between two datasets
>PyMicroArray/to extract TSG & oncogenes from database

This code snippet finds common genes between two data sets and saves the same to a text file. The name of column in which gene name come can be specified in the program. If no common element is found then that is displayed as a message.

```python
import pandas as pd
data1	=	pd.read_csv("Human_TSGs_TSG2.0_database.csv")["GeneSymbol"]
data2	=	pd.read_csv("DEGs_SRR926257.csv")["gene_id"]
common	=	set(data1).intersection(data2)
outfile	=	open('TSGs_in_DEGs_SRR926257.txt', 'w')
if bool(common):
	outfile.write("\n".join(common))
else:
	outfile.write("No Common Genes Found")
outfile.close()
```

#### To filter dataset with a key matching
>PyMicroArray/toFilterDFwithKey

This code can filter a dataset with a coloumn matching a key term. Here we want to extract the rows which match/contain the term *hsa-miR-103a-*. The extracted data is saved into a file in CSV format.

```python
import pandas as pd
data	=	pd.read_csv("Mirtarbase_human_interactions_database.csv")
result	=	pd.DataFrame()
match	=	data.miRNA.str.contains('^hsa-miR-103a-')
result	=	data[match]
result.to_csv('mirtarbase_miR-103a.csv', sep=',')
```

#### To retrieve data from RegNetwork dataset online.
>PyMicroArray/RegNetworkParser

Given a list of items in an excel file (*miRNA_to_find_TF.xlsx*) whose data is to be fetched from Reg Network online. This program does the same and saves each result as a CSV file.

```python
import pandas as pd
import urllib
import time

testfile	=	urllib.URLopener()
searchterms	=	pd.read_excel(open('miRNA_to_find_TF.xlsx','rb'), sheetname=0)['miRNA']

for item in searchterms:
	time.sleep(5)
	#URL = 'http://www.regnetworkweb.org/export.jsp?format=csv&sql=SELECT+*+FROM+human+WHERE+%28%28UPPER%28target_symbol%29+in+%28%27'+item+'%27%29+OR+UPPER%28target_id%29+in+%28%27'+item+'%27%29%29%29+AND+%28evidence+%3D+%27Experimental%27%29+ORDER+BY+UPPER%28regulator_symbol%29+ASC'
	URL  = 'http://www.regnetworkweb.org/export.jsp?format=csv&sql=SELECT+*+FROM+human+WHERE+%28%28UPPER%28target_symbol%29+in+%28%27'+item+'%27%29+OR+UPPER%28target_id%29+in+%28%27'+item+'%27%29%29%29+AND+%28evidence+%3D+%27Experimental%27%29+ORDER+BY+UPPER%28regulator_symbol%29+ASC'
	testfile.retrieve(URL, item+".csv")
```

#### To find average expression levels
>PyMicroArray/proteome_data

This finds multiple occurances of a gene and finds the average value of control and treated expression for each gene. The result is exported into a spreadsheet.

```python
import pandas as pd
import numpy as np
from pandas import ExcelWriter

data	=	pd.read_excel(open('Proteome_data_cell_fractions_combined.xlsx','rb'),\
	sheetname=0,\
	index=False)

columns	=	['UNIPROT', 'SYMBOL', 'GENENAME', 'UNTREATED', 'VEGF', 'Ratio', 'FC']
result	=	pd.DataFrame(columns = columns)
genes 	=	list(set(data['SYMBOL'].values))

for gene in genes:
	row = data[data['SYMBOL']==gene]
	repeat = row.shape[0]
	if repeat>1:
		Vc = np.mean(row['VEGF'])
		V6 = np.mean(row['UNTREATED'])
		if V6==0:
			Ratio ='Inf'
			Fc    ='Inf'
		else:
			Ratio = Vc/V6
			Fc = np.log2(Ratio)
		value = [row['UNIPROT'].values[0], gene, row['GENENAME'].values[0], V6, Vc, Ratio, Fc]
		result.loc[len(result)] =  value
	else:
		row = row.values[0].tolist()
		if row[-2]==0:
			Ratio ='Inf'
			Fc    ='Inf'
		else:
			Ratio = row[-1]/row[-2]
			Fc = np.log2(Ratio)
		row = row+[Ratio, Fc]
		result.loc[len(result)] = row

writer = ExcelWriter('Proteome_Profile_MeanCalculated_FC.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()
```

#### Normalize and classify into UP/Down regulated
>PyMicroArray/Plos

This code adds a flag 'Regulated' to the output to classify genes based on their regulation level into Up/Down. A Z score cutoff of 1.65 equivalent to 95% CI is used for this purpose.

```python
import pandas as pd
cutoff	=	1.65
table	=	pd.read_csv('plosone.csv')
data	=	table['HUVEC']
table['zscore']	=	(data - data.mean())/data.std(ddof=0)

table.loc[table['zscore'] > cutoff, 'Regulation']	=	'UP'
table.loc[table['zscore'] < -1*cutoff, 'Regulation']	=	'Down'
table.to_csv('Regulation.csv', sep=',', index = False)
```

#### Filter specific gene details from NCBI dataset
>PyMicroArray/NCBIOfflineSelector

Given a set of genes check for its presece in local NCBI data set and retreive only necessary details. Here *Homo_sapiens.csv* is the local NCBI data. *GSE837_DEGs_GSEA.xlsx* contains the list of genes to be checked.

```python
import pandas as pd
data	=	pd.read_csv('Homo_sapiens.csv', low_memory=False)
data	=	data[['Symbol', 'Synonyms', 'type_of_gene']]
genes	=	pd.read_excel(open('GSE837_DEGs_GSEA.xlsx','rb'),\
	sheetname=0)['Total_DEG_GSE837_GSEA'].values
col		=	['Symbol', 'Synonyms', 'type_of_gene']
result	=	pd.DataFrame(columns = col)

for index, row in data.iterrows():
	if row.values[1]!='-':
		line = row.values[0]+'|'+row.values[1]
	else:
		line = row.values[0]
	line = line.split('|')

	for gene in genes:
		if gene in line:
			result.loc[len(result)] = row.values

writer = pd.ExcelWriter('GSE837_DEGs_GSEA_Genetype_Out.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()
```

#### Retrieving data from NCBI
>PyMicroArray/NCBI_name_fetcher

This python program fetch the official names of the genes from NCBI website given its gene id.

```python
import pandas as pd
import numpy as np
import requests
import time
import re

genes	=	np.loadtxt('input_hsa-miR-103a-3p.txt')
col		=	['Id', 'Official Full Name']
result	=	pd.DataFrame(columns = col)
link	=	'https://www.ncbi.nlm.nih.gov/gene/'

for gene in genes:
	page	=	requests.get(link+str(int(gene)))
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
	print str(gene)+'\t'+attribute
	#time.sleep(5)
result.to_csv('Output_hsa-miR-103a-3p.csv', sep=',', index = False)
```

#### Retrieving Gene type information from NCBI dataset
>PyMicroArray/NCBI_genetype_fetch_offline

This code is to fetch the details genetype (coding/non-coding) of the given Entrez gene ids from NCBI local database. It requires the Homosapiens downloaded database in Excel format in the same folder. This code will fetch the details for all the input files kept in the same folder and output will be named automatically.

```python
import pandas as pd
import numpy as np
from os import listdir, curdir, path

data	=	pd.read_excel(open('Homo_sapiens.xlsx','rb'), sheetname=0)
data	=	data[['GeneID','type_of_gene']]
col		= 	['id', 'attribute']
files	= 	listdir(curdir)

for file in files:
	if '.txt' in file:
		genes	=	np.loadtxt(file)
		result	=	pd.DataFrame(columns = col)
		for gene in genes:
			result.loc[len(result)] =  data[data['GeneID'] == gene].values[0]
		result.to_csv(path.splitext(file)[0]+'_Out.csv', sep=',', index = False)
```

#### Find Unique Average
>PyMicroArray/UniqueAverage

Given a list of genes and their log fold change values, this program looks if a given gene name is reapeated more than once. If yes, the same is replaced with average log fold change value.

```python
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from time import time
import progressbar

InputFileName	= 		'GEO2R ANALYSIS  GSE81465.xlsx'
data			= 		pd.read_excel(open(InputFileName,'rb'), sheet_name=0, index=False)
result 			= 		pd.DataFrame(columns = data.columns)
genes 			= 		list(set(data['Gene.symbol'].values))
count 			=		0
L 				=		len(genes)

with progressbar.ProgressBar(max_value=L) as bar:
	for gene in genes:
		count+=1
		row = data[data['Gene.symbol']==gene]
		repeat = row.shape[0]
		if repeat>1:
			Fc = np.mean(row['logFC'])
			value = [row['Gene.symbol'].values[0], Fc]
			result.loc[len(result)] =  value
		else:
			result.loc[len(result)] = row.values[0]
		bar.update(count)

writer = ExcelWriter(InputFileName.split('.')[0]+'_Output.xlsx')
result.to_excel(writer,'Sheet1',index=False)
writer.save()
```

#### Find Unique Average
>PyMicroArray/GSE837

Given a dataset, it filters the dataset based on a P-value threshold. Here the data set is given as an excel file and the P value threshold is less than or equal to 0.005. The filtered rows of input data is saved in excel format.

```python
import pandas as pd
xl		=	pd.ExcelFile("Book5.xlsx")
data	= 	xl.parse("Sheet1")
datan	= 	data[data['P.Value']<=0.005].dropna()
writer	= 	pd.ExcelWriter('output_pvalue-0.005.xlsx')
datan.to_excel(writer,'Sheet1')
writer.save()
```

#### Find Unique Average
>PyMicroArray/CSVMixer

This code reads all CSV files available in the current location and combines all of them into a single CSV file.

```python
import pandas as pd
import glob, os  
df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', '*.csv'))))
df.to_csv('mixeddB.csv', sep=',')
```

### Contact
**Sajil C. K.**,  
Research Scholar,  
Dept. of Computational Biology & Bioinformatics,  
University of Kerala, Kerala-695581, India.  
**Email : sajilck@gmail.com**

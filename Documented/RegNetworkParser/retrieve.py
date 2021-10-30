import pandas as pd
import urllib
import time

testfile = urllib.URLopener()
searchterms = pd.read_excel(open('miRNA_to_find_TF.xlsx','rb'), sheetname=0)['miRNA']

for item in searchterms:
	time.sleep(5)
	#URL = 'http://www.regnetworkweb.org/export.jsp?format=csv&sql=SELECT+*+FROM+human+WHERE+%28%28UPPER%28target_symbol%29+in+%28%27'+item+'%27%29+OR+UPPER%28target_id%29+in+%28%27'+item+'%27%29%29%29+AND+%28evidence+%3D+%27Experimental%27%29+ORDER+BY+UPPER%28regulator_symbol%29+ASC'
	URL  = 'http://www.regnetworkweb.org/export.jsp?format=csv&sql=SELECT+*+FROM+human+WHERE+%28%28UPPER%28target_symbol%29+in+%28%27'+item+'%27%29+OR+UPPER%28target_id%29+in+%28%27'+item+'%27%29%29%29+AND+%28evidence+%3D+%27Experimental%27%29+ORDER+BY+UPPER%28regulator_symbol%29+ASC'
	testfile.retrieve(URL, item+".csv")

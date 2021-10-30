import pandas as pd
from pandas import ExcelWriter

Data		= 		pd.read_excel(open('GSE49426_GEO.xlsx','rb'), sheetname="60vscontrol")
#Data 		= 		Data.parse("Sheet1")
Datan 		= 		Data.dropna()


writer = ExcelWriter('GSE49426_blank_dropped.xlsx')
Datan.to_excel(writer,'Sheet1')
writer.save()

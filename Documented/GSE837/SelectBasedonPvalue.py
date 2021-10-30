import pandas as pd
xl = pd.ExcelFile("Book5.xlsx")
data = xl.parse("Sheet1")
datan = data[data['P.Value']<=0.005].dropna()

#print datan[5:15:]
writer = pd.ExcelWriter('output_pvalue-0.005.xlsx')
datan.to_excel(writer,'Sheet1')
writer.save()
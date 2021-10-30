import pandas as pd
import numpy as np


data1 = pd.read_csv("Bushmanlab_cancer gene list.csv")
mainlist = data1["symbol"].tolist()

lister = pd.read_csv("DEGs_SRR926257.csv")
sublist = lister["gene_id"].tolist()

common = []

for item in sublist :
	if item in mainlist:
		common.append(item)


np.savetxt("common_names.csv", common, delimiter=",", fmt='%s')
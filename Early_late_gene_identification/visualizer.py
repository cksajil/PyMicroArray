import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

width  		= 	8
height 		= 	width / 1.618
lwidth 		= 	0.8
labelsize 	= 	12

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize = labelsize)
plt.rc('ytick', labelsize = labelsize)
plt.rc('axes', labelsize  = labelsize)

data		= 	pd.read_excel(open('Results/MasterData.xlsx','rb'), sheet_name='Total_DEGs', index=False)


fig, ax 	= 	plt.subplots()
fig.subplots_adjust(left=.17, bottom=.18, right=.95, top=.97)
time 		= 	data['Hour'].values
LFC  		= 	data['LFC'].values


# data.plot.scatter(x="Hour",y="LFC", c=data['Dynamics'].values=='AlwaysUP')

plt.scatter(time, LFC, color='k', s=2)
# plt.plot(x, mu, color='k', linewidth='0.6', label='$\mu_{RMS}$')
# plt.plot(x, stdlow, color='g', linewidth='0.6', label='$\mu_{RMS}-2*\sigma_{RMS}$')
# plt.plot(x, stdhigh, color='r', linewidth='0.6', label='$\mu_{RMS}+2*\sigma_{RMS}$')
plt.xlabel('Hour')
plt.ylabel('LFC')

# plt.xlim((0,3.5))
# plt.ylim((0,0.16))
# plt.grid(True, which='major', linestyle='--', linewidth='0.3')
# plt.legend(loc='upper left',fontsize = legendfont)
plt.show()

fig.set_size_inches(width, height)
fig.savefig('Results/Scatter.png', dpi = 600)

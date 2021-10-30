import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.normal(10,1,30).reshape(10,3), index = pd.date_range('2010-01-01', freq = 'M', periods = 10), columns = ('one', 'two', 'three'))
df['key1'] = (4,4,4,6,6,6,8,8,8,8)

# print df

colors = np.where(df["key1"]==4,'r','-')

print colors
colors[df["key1"]==6] = 'g'

print colors
colors[df["key1"]==8] = 'b'
print colors
df.plot.scatter(x="one",y="two",c=colors)
plt.show()

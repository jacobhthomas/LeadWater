import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

def shorten_zip(zip): 
    if len(str(zip))!= 10: 
        return np.NaN
    return zip[:5]

df = pd.read_csv('datasets/assessorSequential.csv')
df.drop(columns=['Unnamed: 0'])
df['ZIP'] = df['ZIP'].apply(lambda x: shorten_zip(x))
df = df[df['ZIP'].notna()]

# calculate average lead level and which interval it is in 
df['avg'] = df.filter(like='Draw').apply(lambda x: x.mean(), axis=1)
df['interval'] = ['ppb < 5' if (x < 5) else '5 <= ppb < 15' if (x < 15) else '15 <= ppb' for x in df['avg']]

df.sort_values(by=['Latitude'], inplace=True, ascending=False)

# filter out lead level intervals 
x1 = list(df[df['interval'] == 'ppb < 5']['ZIP'])
x2 = list(df[df['interval'] == '5 <= ppb < 15']['ZIP'])
x3 = list(df[df['interval'] == '15 <= ppb']['ZIP'])

print(len(x1), len(x2), len(x3))

# specify colors and labels of stacked bars
colors=['navy', 'seagreen', 'darkred']
names=['ppb < 5', '5 <= ppb < 15', '15 <= ppb']

# plot histogram 
plt.hist([x1, x2, x3], color=colors, label=names, density=True, stacked = True, rwidth=.9, bins=48, alpha = .7, align='mid')
plt.title('Density of Average Lead Intervals by ZIP Code')
plt.xlabel('ZIP Code')
plt.ylabel('Density')
plt.xticks(rotation=90, size=7)
plt.yticks(size = 8)
plt.legend(names, loc='upper right')

plt.show()

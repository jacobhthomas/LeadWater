import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 


zips = [60645, 60626, 60631, 60646, 60659, 60660, 
60656, 60630, 60625, 60640, 60634, 60641, 60618, 60613, 
60657, 606707, 60739, 60647, 60614, 60651, 60622, 
60610, 60654, 60611, 60601, 606, 60661, 60606, 60602, 
60603, 60604, 60644, 60624, 60612, 60607, 60605, 
60623, 60608, 60616, 
60632, 606099, 60653, 60615, 60638, 60629, 60636, 60621, 
60637, 60649, 60652, 60619, 60620, 60617, 
60655, 60643, 60628, 60633, 60827]

zips = [str(x) for x in zips]

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

df_zips = set(df['ZIP'])

zip_list = [] 
for z in zips: 
    if z in df_zips: 
        zip_list.append(z)

# df.groupby(['ZIP']).mean()

# # # filter out lead level intervals 
# x1 = list(df[df['interval'] == 'ppb < 5']['ZIP'])
# x2 = list(df[df['interval'] == '5 <= ppb < 15']['ZIP'])
# x3 = list(df[df['interval'] == '15 <= ppb']['ZIP'])

# specify colors and labels of stacked bars
colors=['navy', 'seagreen', 'darkred']
names=['ppb < 5', '5 <= ppb < 15', '15 <= ppb']

# # plt.hist([x1, x2, x3], color=colors, label=names, density=True, stacked = True, rwidth=.9, bins=48, alpha = .7, align='mid')
# # plt.title('Density of Average Lead Intervals by ZIP Code')
# # plt.xlabel('ZIP Code')
# # plt.ylabel('Density')
# # plt.xticks(rotation=90, size=7)
# # plt.yticks(size = 8)
# # plt.legend(names, loc='upper right')

# # plt.show()

cross_tab_prop = pd.crosstab(index=df['ZIP'], columns=df['interval'], normalize='index')
cross_tab =  pd.crosstab(index=df['ZIP'], columns=df['interval']) 

cross_tab_prop = cross_tab_prop[names]
cross_tab = cross_tab[names]

cross_tab_prop=cross_tab_prop.transpose()
cross_tab=cross_tab.transpose()

cross_tab_prop = cross_tab_prop[zip_list]
cross_tab=cross_tab[zip_list]

cross_tab_prop=cross_tab_prop.transpose()
cross_tab=cross_tab.transpose()

print(cross_tab)


cross_tab_prop.plot(kind='bar', stacked=True, color=colors, label=names, alpha = .6, figsize=(10,6))
plt.title('Proportion of Average Lead Intervals by ZIP Code')
plt.xticks(size=7)
plt.yticks(size = 8)
plt.ylabel('Proportion')
plt.legend(names, loc='upper right')

plt.show() 

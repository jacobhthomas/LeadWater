import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy.stats import f_oneway
from scipy.stats import ttest_ind

df = pd.read_csv('datasets/assessorSequential.csv')
df.drop(columns=['Unnamed: 0', 'PIN','Township Code','Neighborhood Code','Sale Price','Age','ZIP','Longitude','Latitude'], inplace=True)

df = df[df['Tract Median Income'].notna()]

income = df['Tract Median Income']
q33 = income.quantile(.33)
q66 = income.quantile(.66)

df['Tract Median Income'] = df['Tract Median Income'].apply(lambda x: round(x / 10000.0) * 10000.0)

df['avg'] = df.filter(like='Draw').apply(lambda x: x.mean(), axis=1)

# min_avg = df['avg'].min() 
# max_avg = df['avg'].max() 
# df['avg_norm'] = (df['avg'] - min_avg) / (max_avg - min_avg)

# df = df[df['avg'] >= 15]


df = df[['avg', 'Tract Median Income']]

df_low = df.drop(df[df['Tract Median Income'] > q33].index)
df_mid = df.drop(df[df['Tract Median Income'] <= q33].index)
df_mid.drop(df_mid[df_mid['Tract Median Income'] > q66].index, inplace=True)
df_high = df.drop(df[df['Tract Median Income'] <= q66].index)

avg_low = df_low['avg'].tolist() 
avg_med = df_mid['avg'].tolist()
avg_high = df_high['avg'].tolist() 

# one way anova for 
print('ANOVA: low vs mid vs high income: p-value=', f_oneway(avg_low, avg_med, avg_high)[1])
print('T-test: low vs high income: p-value=', ttest_ind(avg_low, avg_high, random_state=4122023)[1])
print('T-test: low vs mid income: p-value=', ttest_ind(avg_low, avg_med, random_state=4122023)[1])
print('T-test: med vs high income: p-value=', ttest_ind(avg_med, avg_high, random_state=4122023)[1])

df_new_low = df.drop(df[df['Tract Median Income'] > q66].index)
df_new_high = df.drop(df[df['Tract Median Income'] <= q66].index)

avg_new_low = df_new_low['avg'].tolist() 
avg_new_high = df_new_high['avg'].tolist() 

print('T-test: new low vs new high income: p-value', ttest_ind(avg_new_low, avg_new_high, equal_var=False, random_state=4122023)[1])

sns.boxplot(x='Tract Median Income', y='avg', data=df)
sns.set(font_scale=.7)
plt.title('Average Lead Levels vs Tract Median Income')
plt.ylabel('Average Lead Levels (ppb)')
plt.xticks(rotation=90)
plt.show()
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('relative_differences_sequential_data.csv')

df.drop(columns=['Date Sampled', 'Address', 'Unnamed: 0'], axis = 1, inplace=True)

column_names = df.columns
for col in column_names: 
    df.drop(df[df[col] > 1].index, inplace=True)

# print(df.describe())
flierprops = dict(marker='o', markersize=3)
ax = df.plot.box(flierprops=flierprops)
plt.title('Relative Difference Boxplots')
plt.xlabel('Draws')
plt.ylabel('Relative Difference')
plt.show()

# df.drop(df.iloc[:, 4:], inplace=True, axis=1)

# print(df.columns)
# sns.pairplot(df)
# plt.show()

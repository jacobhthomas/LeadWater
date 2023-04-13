import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('datasets/CleanedTimedData.csv')
df.dropna(inplace=True)
df.drop(columns=['Date Sampled','Address','2-3 Minute','5 Minute'], inplace=True)
df['First Draw'] = df['First Draw'].apply(pd.to_numeric, errors='coerce')
print(df)

chop = [.3, .4, .5, .6, .7, .8, .9, 1]
low_level= []
high_level = []

for c in chop: 
    p = df.quantile(1-c).values[0]
    chopped_df = df.drop(df[df['First Draw'] < float(p)].index)
    low_percentile = chopped_df.quantile(.90).values[0]
    high_percentile = chopped_df.quantile(.95).values[0]
    low_level.append(low_percentile)
    high_level.append(high_percentile)

print(low_level)

plt.scatter(chop, low_level)
plt.scatter(chop, high_level)
plt.grid(True)
plt.axhline(6.8, c='r')
plt.title('Lead Levels at the 90th, 95th percentile of the Top X% of data')
plt.xlabel('Top Percentage of Data')
plt.ylabel('Lead (ppb)')
plt.legend(['90th', '95th'], loc='upper right')
plt.yticks(np.arange(0, max(high_level)+1, 1))
plt.show()

# print('20th percentile of original data: ',p.values[0])

# df.drop(df[df['First Draw'] < p.values[0]].index, inplace=True)

# print(df)

# # df['First Draw'].plot(kind='box')
# # plt.show() 
# low = df.quantile(.9).values[0]
# high = df.quantile(.95).values[0]

# print('90th to 95th percentile of chopped data: ', low, '-', high)

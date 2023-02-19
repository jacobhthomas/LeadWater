import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc



df = pd.read_csv('relative_differences_sequential_data.csv')

print(df.shape)

# drop unnecessary columns
df.drop(columns=['Date Sampled', 'Address', 'Unnamed: 0'], axis = 1, inplace=True)

# drop any rows with entries > 2 to prevent skewed plots (removes about 100 rows out of 1800)
column_names = df.columns
for col in column_names: 
    df.drop(df[df[col] > 2].index, inplace=True)

# # boxplot 
# flierprops = dict(marker='o', markersize=3)
# ax = df.plot.box(flierprops=flierprops)
# plt.title('Relative Difference Boxplots')
# plt.xlabel('Draws')
# plt.ylabel('Relative Difference')

# df1_6 = df.drop(df.iloc[:, 5:], axis=1)
# df5_10 = df.drop(df.iloc[:, :5], axis=1)

# df_compare_across = df.drop(df.iloc[:, 1:2], axis = 1)
# df_compare_across.drop(df.iloc[:, 3:4], axis = 1, inplace=True)
# df_compare_across.drop(df.iloc[:, 5:6], axis = 1, inplace=True)
# df_compare_across.drop(df.iloc[:, 7:8], axis = 1, inplace=True)
# df_compare_across.drop(df.iloc[:, 9:10], axis = 1, inplace=True)


# sns.set_style("darkgrid")
# sns.pairplot(df_compare_across, plot_kws = dict(markers='o', color="green", s=3))
# sns.pairplot(df1_6, plot_kws = dict(markers='o', color="red", s=3))
# sns.pairplot(df5_10, plot_kws = dict(markers='o', color="blue", s=3))
# plt.show()

# # plt.title("Dendrogram")
# # clusters = shc.linkage(df.values, method='average')
# # shc.dendrogram(Z=clusters)
# # plt.show()


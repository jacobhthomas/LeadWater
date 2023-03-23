import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("datasets/RelativeDifferenceClusters.csv")
# df.drop(columns=['Unnamed: 0', 'HCluster'], inplace=True)
# # drop minute draws 
df = df.drop(columns=['HCluster', 'Unnamed: 0', 'Date.Sampled', 'Address'])
columns = df.columns

sns.set(font_scale=.7)
fig, axes = plt.subplots(3, 3, sharex=True, sharey = True, figsize=(16,8))
fig.suptitle('Histograms of Relative Differences of Sequential Draws')

fig.supxlabel('Relative Difference')
fig.supylabel('Frequency')

for i, col in enumerate(columns): 
    sns.histplot(data=df, x=col, ax=axes[i//3, i%3], binrange=[df[col].quantile(.05), df[col].quantile(.95)])
    axes[i//3, i%3].set_title('Draw ' + col[4] + ' to Draw ' + col[6:])
    axes[i//3, i%3].set_ylabel('')
    axes[i//3, i%3].set_xlabel('')
    axes[i//3, i%3].axvline(0, color='red')
fig.tight_layout()
plt.subplots_adjust(left=.05)
plt.show() 

# df = pd.read_csv('datasets/CleanedSequentialData.csv')
# df = df.drop(columns=['Unnamed: 0', 'Date.Sampled', 'Address','X10th.Draw',"X11th.Draw","X3.Minute","X5.Minute","X7.Minute","X10.Minute","X15.Minute","X20.Minute"])
# columns = df.columns

# sns.set(font_scale=.7)
# fig, axes = plt.subplots(3, 3, sharex=True, sharey = True, figsize=(16,8))
# fig.suptitle('Histograms of Sequential Draws')
# fig.supxlabel('parts per billion (ppb)')
# fig.supylabel('Frequency')

# for i, col in enumerate(columns): 
#     sns.histplot(data=df, x=col, ax=axes[i//3, i%3], binrange=[df[col].quantile(0), df[col].quantile(.95)])
#     axes[i//3, i%3].set_ylabel('')
#     axes[i//3, i%3].set_xlabel('')
#     axes[i//3, i%3].set_title(col[1:].replace('.', ' '))
#     axes[i//3, i%3].axvline(15, color='red')
# fig.tight_layout()
# plt.subplots_adjust(left=.05)
# plt.show() 



# x = [i for i in range(1,11)]
# avgs = p_change_df.mean(axis=0, numeric_only=True)
# medians = p_change_df.median(axis=0, numeric_only=True)

# plot averages 
# plt.scatter(x, avgs, s = 12, c='red') 
# plt.xlabel('Draw')
# plt.ylabel('Average Percent Change')
# plt.title('Average Percent Change vs Draw')
# plt.show() 

# plot medians 
# plt.scatter(x, medians, s = 12, c='red') 
# plt.xlabel('Draw')
# plt.ylabel('Median Percent Change')
# plt.title('Median Percent Change vs Draw')
# plt.show() 

# calculate pearson correlation coefficients  
corr_matrix = df.corr(method='pearson', numeric_only=True)
print(type(corr_matrix))
# corr_matrix.to_csv('percent_change_corr_matrix.csv')

# corr_matrix.style.background_gradient(cmap='RdGn')
# corr_matrix.to_csv('pearson_correlations_rd_color.csv')
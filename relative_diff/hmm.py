import pandas as pd 
import matplotlib.pyplot as plt 
from hmmlearn import hmm

df = pd.read_csv('relative_differences_sequential_data.csv')
df = df.drop(columns=['Unnamed: 0']) 

col_names = df.columns
draw_cols = col_names[2:]

# sort by date 
# df['Date.Sampled'] = pd.to_datetime(df['Date.Sampled'])
# df.sort_values(by='Date.Sampled', inplace=True)

# calculate average differences 
draws_only = df[draw_cols]
avg_dif = draws_only.mean(axis=1)
df['avg_dif'] = avg_dif

# drop outliers for visibility
df.drop(df[df['avg_dif'] > 2].index, inplace=True)

plt.plot(df['Date.Sampled'], df['avg_dif'])
plt.title('Average Relative Difference vs Date Sampled')
plt.xlabel("Date Sampled")
plt.ylabel('Average Relative Difference')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()


# X = df[['avg_dif']].values

# model=hmm.GaussianHMM(n_components=3, covariance_type='diag', n_iter=50, random_state=333)
# model.fit(X)

# Z = model.predict(X)
# states=pd.unique(Z)

# print("Unique States: ", states)
# print("\nStart probabilities:")
# print(model.startprob_)
# print("\nTransition matrix:")
# print(model.transmat_)
# print("\nGaussian distribution means:")
# print(model.means_)
# print("\nGaussian distribution covariances:")
# print(model.covars_)

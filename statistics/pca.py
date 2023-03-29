import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
  
# define standard scaler
scaler = StandardScaler()

df = pd.read_csv('datasets\RelativeDifferenceSequentialData.csv')

df_randomized = pd.read_csv('datasets\RelativeDifferencesRandomized.csv')

df.drop(columns=['Date.Sampled', 'Address', 'Unnamed: 0', 'x10x11'], axis = 1, inplace=True)

df_randomized.drop(columns=['Unnamed: 0','Date.Sampled', 'Address'], axis = 1, inplace=True)

# df = scaler.fit_transform(df)
# print(df_randomized.head())
# print(df.head)

# drop any rows with entries > 2 to prevent skewed plots (removes about 100 rows out of 1800)
column_names = df.columns
for col in column_names: 
    df.drop(df[df[col] > 2].index, inplace=True)

pca = PCA(n_components=9)
pca.fit_transform(df.values)

variance = pca.explained_variance_ratio_.cumsum() 
print(type(variance))
x = ['1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10']
plt.ylim(0,1)
plt.xlabel('Relative Difference Component')
plt.ylabel('Explained Variance')
plt.title('Variance vs Relative Difference Component')
plt.plot(x, variance, marker='o', c='black')
plt.grid(True)
plt.show()
# print('original relative differences, dropping outliers: ', pca.explained_variance_ratio_.cumsum())

# pca = PCA(n_components=9)
# pca.fit_transform(df_randomized.values)
# print('randomized relative differences: ', pca.explained_variance_ratio_.cumsum())
import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
  
# define standard scaler
scaler = StandardScaler()

df = pd.read_csv('datasets\Relative_differences_sequential_data.csv')
# transform data
df = scaler.fit_transform(df)

df_randomized = pd.read_csv('datasets\RelativeDifferencesRandomizedScaled.csv')

df.drop(columns=['Date.Sampled', 'Address', 'Unnamed: 0', 'x10x11'], axis = 1, inplace=True)

df_randomized.drop(columns=['Date.Sampled', 'Address', 'Unnamed: 0'], axis = 1, inplace=True)
# print(df_randomized.head())
# print(df.head)

# drop any rows with entries > 2 to prevent skewed plots (removes about 100 rows out of 1800)
# column_names = df.columns
# for col in column_names: 
#     df.drop(df[df[col] > 2].index, inplace=True)

pca = PCA(n_components=9)
pca.fit_transform(df.values)
print('original: ', pca.explained_variance_ratio_.cumsum())

pca = PCA(n_components=9)
pca.fit_transform(df_randomized.values)
print('randomized: ', pca.explained_variance_ratio_.cumsum())
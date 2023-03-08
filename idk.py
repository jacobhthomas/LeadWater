import pandas as pd 


df = pd.read_csv('datasets/ClusterCoordinatesSeqDrawsRawGeoData.csv')
print(df.columns) 

df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'], inplace=True)
df.to_csv('datasets/SequentialDrawGeoData.csv')
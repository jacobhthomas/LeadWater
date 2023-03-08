import pandas as pd 

df = pd.read_csv('datasets/SequentialDrawGeoData.csv')
df2 = df.drop(columns=['Unnamed: 0', 
                 'place_info'])
print(df2.columns)

df2.to_csv('datasets/ClusterCoordinatesSeqDrawsRawGeoData.csv')

# df['median'] = df.filter(like='Draw').apply(lambda x: x.median(), axis = 1)
# df['zipcode'] = df[['']]
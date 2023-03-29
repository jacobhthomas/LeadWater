import pandas as pd 
from geo_calculations import clean_addresses
import random 
import numpy as np

random.seed(1827)
df = pd.read_csv('datasets\RelativeDifferenceClusters.csv')
df = df[['Date.Sampled', 'Address', 'HCluster']]
df2 = pd.read_csv('datasets\cleaned_sequential.csv')
df2 = df2[["X1st.Draw","X2nd.Draw","X3rd.Draw","X4th.Draw","X5th.Draw","X6th.Draw","X7th.Draw","X8th.Draw","X9th.Draw","X10th.Draw","X11th.Draw"]]

df = pd.concat([df, df2], axis=1, join='inner')
print(df)
# clean the addresses attribute 
df['Address'] = df['Address'].apply(clean_addresses)

lst_longs = []
lst_lats = []

with open('LongLats.txt', 'r') as file: 
    for line in file: 
        long, lat = line.rstrip().split(',')

        lst_longs.append(long)
        lst_lats.append(lat)

df['longitude'] = lst_longs
df['latitude'] = lst_lats
df['longitude'].replace('', np.nan, inplace=True)
df['latitude'].replace('', np.nan, inplace=True)
df = df.dropna()

# DF: adds the cluster coordinates to the sequential data, but the clusters are based on the relative differences. 
df.to_csv('ClusterCoordinatesSeqDraws.csv')
import pandas as pd 
from geo_calculations import clean_addresses
import random 
import numpy as np

random.seed(1827)
df = pd.read_csv('datasets\RelativeDifferenceClusters.csv')
df = df[['Date.Sampled', 'Address', 'HCluster']]

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

df.to_csv('ClusterCoordinates.csv')
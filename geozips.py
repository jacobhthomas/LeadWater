import numpy as np
import geopandas
import pandas as pd 
import matplotlib.pyplot as plt
from shapely.geometry import Point
import random 

def color_by_val(row): 
    val = row['avg']
    if 0 <= val < 5: 
        return 1 
    elif 5 <= val < 15: 
        return 2 
    else: 
        return 3

crs = {'init': 'epsg:4326'}
random.seed(1827)
def shorten_zip(zip): 
    if len(str(zip))!= 10: 
        return np.NaN
    return zip[:5]

df = pd.read_csv('datasets/assessorSequential.csv')
df.drop(columns=['Unnamed: 0'], inplace=True)
df['ZIP'] = df['ZIP'].apply(lambda x: shorten_zip(x))
df = df[df['ZIP'].notna()]

df['avg'] = df.filter(like='Draw').apply(lambda x: x.mean(), axis=1)
df['ppb_label'] = df.apply(lambda row: color_by_val(row), axis=1)

# create new geo dataframe 
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
geo_df = geopandas.GeoDataFrame(df, crs = crs, geometry = geometry)

print(geo_df)

# read Chicago shp map 
street_map = geopandas.read_file('geodata\geo_export_c315ae68-1c3e-40e9-b2a7-69885fdcc885.shp')

# plot data on the map 
fig, ax = plt.subplots(figsize = (15,15))
# print(ax)
street_map.plot(ax = ax, alpha = .3, color = 'grey')
geo_df[geo_df['ppb_label'] == 1].plot(ax = ax, markersize = 8, color = 'navy', label = '0 <= ppb < 5', alpha=.9) 
geo_df[geo_df['ppb_label'] == 2].plot(ax = ax, markersize = 8, color = 'seagreen', label = '5 <= ppb < 15', alpha=.9)
geo_df[geo_df['ppb_label'] == 3].plot(ax = ax, markersize = 8, color = 'darkred', label = '15 <= ppb', alpha =.9)

plt.title('Sequential Data Mapped onto Chicago Street Lines: Average Lead Level')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-87.855, -87.5)
plt.xticks(rotation=90)
plt.legend(prop={'size': 8})

# plt.savefig('MedianPPBCoordinateGraph.png')

plt.show() 

# # create new geo dataframe 
# geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
# geo_df = geopandas.GeoDataFrame(df, crs = crs, geometry = geometry)

# print(geo_df)

# # read Chicago shp map 
# street_map = geopandas.read_file('geodata\geo_export_c315ae68-1c3e-40e9-b2a7-69885fdcc885.shp')

# # # plot data on the map 
# fig, ax = plt.subplots(figsize = (15,15))
# # print(ax)
# street_map.plot(ax = ax, alpha = .3, color = 'grey')
# geo_df[geo_df['HCluster'] == 1].plot(ax = ax, markersize = 12, color = 'red', label = 'Cluster 1') 
# geo_df[geo_df['HCluster'] == 2].plot(ax = ax, markersize = 12, color = 'blue', label = 'Cluster 2') 
# geo_df[geo_df['HCluster'] == 3].plot(ax = ax, markersize = 12, color = 'green', label = 'Cluster 3') 
# geo_df[geo_df['HCluster'] == 4].plot(ax = ax, markersize = 12, color = 'orange', label = 'Cluster 4') 
# geo_df[geo_df['HCluster'] == 5].plot(ax = ax, markersize = 6, color = 'purple', label = 'Cluster 5') 

# plt.title('Data Mapped onto Chicago Street Lines, Colored by Average Lead Levels')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.xlim(-87.855, -87.5)
# plt.xticks(rotation=90)
# plt.legend(prop={'size': 8})

# plt.show() 
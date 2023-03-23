import numpy as np
import geopandas
import pandas as pd 
import matplotlib.pyplot as plt
from shapely.geometry import Point
import random 

def color_by_val(row): 
    val = row['median_ppb']
    if 0 <= val <= 5: 
        return 1 
    elif 5 < val <= 10: 
        return 2 
    elif 10 < val <= 15: 
        return 3 
    elif 15 < val <= 25: 
        return 4 
    else: 
        return 5 

crs = {'init': 'epsg:4326'}
random.seed(1827)

df = pd.read_csv('datasets\ClusterCoordinatesSeqDraws.csv')

# df['max_ppb'] = df[["X1st.Draw","X2nd.Draw","X3rd.Draw","X4th.Draw","X5th.Draw","X6th.Draw","X7th.Draw","X8th.Draw","X9th.Draw","X10th.Draw","X11th.Draw"]].max(axis=1)
df['median_ppb'] = df[["X1st.Draw","X2nd.Draw","X3rd.Draw","X4th.Draw","X5th.Draw","X6th.Draw","X7th.Draw","X8th.Draw","X9th.Draw","X10th.Draw","X11th.Draw"]].median(axis=1)
df['ppb_label'] = df.apply(lambda row: color_by_val(row), axis=1)

# create new geo dataframe 
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
geo_df = geopandas.GeoDataFrame(df, crs = crs, geometry = geometry)

print(geo_df)

# read Chicago shp map 
street_map = geopandas.read_file('geodata\geo_export_c315ae68-1c3e-40e9-b2a7-69885fdcc885.shp')

# plot data on the map 
fig, ax = plt.subplots(figsize = (15,15))
# print(ax)
street_map.plot(ax = ax, alpha = .3, color = 'grey')
geo_df[geo_df['ppb_label'] == 1].plot(ax = ax, markersize = 12, color = 'red', label = '0 <= ppb <= 5') 
geo_df[geo_df['ppb_label'] == 2].plot(ax = ax, markersize = 12, color = 'blue', label = '5 < ppb <=10')
geo_df[geo_df['ppb_label'] == 3].plot(ax = ax, markersize = 12, color = 'green', label = '10 < ppb <= 15')
geo_df[geo_df['ppb_label'] == 4].plot(ax = ax, markersize = 12, color = 'orange', label = '15 < ppb <=25')
geo_df[geo_df['ppb_label'] == 5].plot(ax = ax, markersize = 6, color = 'purple', label = '25 < ppb')

plt.title('Sequential Data Mapped onto Chicago Street Lines: Median ppb')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-87.855, -87.5)
plt.xticks(rotation=90)
plt.legend(prop={'size': 8})

plt.savefig('MedianPPBCoordinateGraph.png')

plt.show() 

# # create new geo dataframe 
# geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
# geo_df = geopandas.GeoDataFrame(df, crs = crs, geometry = geometry)

# print(geo_df)

# # read Chicago shp map 
# street_map = geopandas.read_file('geodata\geo_export_c315ae68-1c3e-40e9-b2a7-69885fdcc885.shp')

# # plot data on the map 
fig, ax = plt.subplots(figsize = (15,15))
# print(ax)
street_map.plot(ax = ax, alpha = .3, color = 'grey')
geo_df[geo_df['HCluster'] == 1].plot(ax = ax, markersize = 12, color = 'red', label = 'Cluster 1') 
geo_df[geo_df['HCluster'] == 2].plot(ax = ax, markersize = 12, color = 'blue', label = 'Cluster 2') 
geo_df[geo_df['HCluster'] == 3].plot(ax = ax, markersize = 12, color = 'green', label = 'Cluster 3') 
geo_df[geo_df['HCluster'] == 4].plot(ax = ax, markersize = 12, color = 'orange', label = 'Cluster 4') 
geo_df[geo_df['HCluster'] == 5].plot(ax = ax, markersize = 6, color = 'purple', label = 'Cluster 5') 

plt.title('Data Mapped onto Chicago Street Lines, Colored by Clustering on Relative Differences')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(-87.855, -87.5)
plt.xticks(rotation=90)
plt.legend(prop={'size': 8})

plt.savefig('ClusterCoordinateGraph.png')

plt.show() 
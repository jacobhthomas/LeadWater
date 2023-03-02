import numpy as np
import geopandas
import pandas as pd 
import matplotlib.pyplot as plt
from shapely.geometry import Point
import random 

crs = {'init': 'epsg:4326'}
random.seed(1827)

df = pd.read_csv('datasets\ClusterCoordinatesSeqDraws.csv')

df['max_ppb'] = df[["X1st.Draw","X2nd.Draw","X3rd.Draw","X4th.Draw","X5th.Draw","X6th.Draw","X7th.Draw","X8th.Draw","X9th.Draw","X10th.Draw","X11th.Draw"]].max(axis=1)

print(max(df['max_ppb']))
print(min(df['max_ppb']))
# # create new geo dataframe 
# geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
# geo_df = geopandas.GeoDataFrame(df, crs = crs, geometry = geometry)

# print(geo_df)

# # read Chicago shp map 
# street_map = geopandas.read_file('geodata\geo_export_c315ae68-1c3e-40e9-b2a7-69885fdcc885.shp')

# # plot data on the map 
# fig, ax = plt.subplots(figsize = (15,15))
# # print(ax)
# street_map.plot(ax = ax, alpha = .3, color = 'grey')
# geo_df[geo_df['HCluster'] == 1].plot(ax = ax, markersize = 12, color = 'red', marker ='x', label = 'Cluster 1') 
# geo_df[geo_df['HCluster'] == 2].plot(ax = ax, markersize = 12, color = 'blue', marker = '.', label = 'Cluster 2') 
# geo_df[geo_df['HCluster'] == 3].plot(ax = ax, markersize = 12, color = 'green', marker = '^', label = 'Cluster 3') 
# geo_df[geo_df['HCluster'] == 4].plot(ax = ax, markersize = 12, color = 'orange', marker = '*', label = 'Cluster 4') 
# geo_df[geo_df['HCluster'] == 5].plot(ax = ax, markersize = 6, color = 'purple', marker = 's', label = 'Cluster 5') 

# plt.title('Sequential Data Mapped onto Chicago Street Lines')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.xlim(-87.855, -87.5)
# plt.xticks(rotation=90)
# plt.legend(prop={'size': 10})

# plt.savefig('ClusterCoordinateGraph.png')

# plt.show() 
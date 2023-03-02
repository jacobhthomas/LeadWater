import pandas as pd 
import random
import numpy as np
import geopandas
import csv
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from shapely.geometry import Point

# generate random integer of length N 
def randN(N):   
        
	min = pow(10, N-1)
	max = pow(10, N) - 1

	return str(random.randint(min, max))

# clean and fill in data address strings 
def clean_addresses(address): 

    lst = list(address.split())
    
    # remove Xs and asteriks 
    nums_random = lst[0].count('X')
    lst[0] = lst[0].strip('X')
    lst[-1] = lst[-1].strip('*')
    
    # fill in missing address numbers randomly 
    if nums_random > 0:
        add_block_num = randN(nums_random)
        lst[0] += str(add_block_num)

    new_address = ' '.join(lst) + ', Chicago, IL'

    return new_address

# find long, lat coordinates for data addresses 
def find_coordinates(addresses): 

    with open('LongLats2.txt', 'w', newline='\n') as file: 
        
        writer = csv.writer(file)
     
        locator = Nominatim (user_agent = 'my_request')

        for i, address in enumerate(addresses): 

            print(i)

            getLoc = locator.geocode(address) 

            if getLoc: 
                long = getLoc.longitude
                lat = getLoc.latitude 
            else: 
                 long = ""
                 lat = ""
            
            writer.writerow([long, lat])

# -----------------# 

crs = {'init': 'epsg:4326'}
random.seed(1827)

df = pd.read_csv('datasets\RelativeDifferenceClusters.csv')
df = df[['Address']]

# clean the addresses attribute 
df['Address'] = df['Address'].apply(clean_addresses)


# compute coordinates for each instance 
# find_coordinates(df['Address'].values)

# drop any data instances we couldn't find coordinates for 
# df.dropna(inplace=True)

# df.to_csv('ClustersLongLat.csv')


# # create new geo dataframe 
# geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
# geo_df = geopandas.GeoDataFrame(df, crs = crs, geometry = geometry)

# print(geo_df)

# # read Chicago shp map 
# # street_map = geopandas.read_file('geodata\geo_export_c315ae68-1c3e-40e9-b2a7-69885fdcc885.shp')

# # plot data on the map 
# fig, ax = plt.subplots(figsize = (15,15))
# print(ax)
# # street_map.plot(ax = ax, color = 'grey')
# geo_df[geo_df['HCluster'] == 1].plot(ax = ax, markersize = 8, color = 'red', label = '1') 
# geo_df[geo_df['HCluster'] == 2].plot(ax = ax, markersize = 8, color = 'orange', label = '2') 
# geo_df[geo_df['HCluster'] == 3].plot(ax = ax, markersize = 8, color = 'green', label = '3') 
# geo_df[geo_df['HCluster'] == 4].plot(ax = ax, markersize = 8, color = 'blue', label = '4') 
# geo_df[geo_df['HCluster'] == 5].plot(ax = ax, markersize = 8, color = 'purple', label = '5') 
# plt.legend(prop={'size': 10})

# plt.show() 
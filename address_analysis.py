import pandas as pd 
import random
import numpy as np
import geopandas
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
      
    locator = Nominatim (user_agent = 'my_request')
    lst_longs = []
    lst_lats = []

    for address in addresses: 
        getLoc = locator.geocode(address) 
        lst_longs.append(getLoc.longitude)
        lst_lats.append(getLoc.latitude)
    
    return lst_longs, lst_lats

# -----------------# 

crs = {'init': 'epsg:4326'}
random.seed(1827)

df = pd.read_csv('relative_differences_sequential_data.csv')
df = df.drop(columns=['Unnamed: 0']) 

# clean the addresses attribute 
df['Address'] = df['Address'].apply(clean_addresses)

sample = df.head(5)

# compute coordinates for each instance 
sample['longitude'], sample['latitude'] = find_coordinates(sample['Address'].values)
print(sample)

# create new geo dataframe 
geometry = [Point(xy) for xy in zip(sample['longitude'], sample['latitude'])]
geo_df = geopandas.GeoDataFrame(sample, crs = crs, geometry = geometry)

print(geo_df)

geo_df['type'] = [0, 1, 1, 1, 0]

# read Chicago shp map 
street_map = geopandas.read_file('geodata\geo_export_c315ae68-1c3e-40e9-b2a7-69885fdcc885.shp')

# plot data on the map 
fig, ax = plt.subplots(figsize = (15,15))
street_map.plot(ax = ax, alpha = .4, color = 'grey')
geo_df[geo_df['type'] == 0].plot(ax = ax, markersize = 20, color = 'red', marker = 'o')
geo_df[geo_df['type'] == 1].plot(ax = ax, markersize = 20, color = 'blue', marker = 'x')
# plt.legend(prop={'size': 15})

plt.show() 
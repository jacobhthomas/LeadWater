import pandas as pd 
import geopy 
from geopy.geocoders import Nominatim
import numpy as np 


def get_zipcode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    raw_address = location.raw['address']
    place_id = location.raw['place_id']
    print(df['Unnamed: 0'])
    return ([raw_address, place_id])

df = pd.read_csv('datasets/ClusterCoordinatesSeqDraws.csv')

locator = Nominatim (user_agent = 'my_request', timeout=3) 

df['place_info'] = df.apply(get_zipcode, axis=1, geolocator=locator, lat_field='latitude', lon_field='longitude')
df2 = pd.DataFrame(df)
df2[['raw_address','place_id']] = pd.DataFrame(df2.place_info.tolist(), index = df2.index)

df2.to_csv('datasets/ClusterCoordinatesSeqDrawsRawGeoData.csv')
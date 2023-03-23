import pandas as pd 
import numpy as np
from scipy.stats import chi2_contingency

def get_address_component(df, component): 
    address_info = eval(df['raw_address'])
    if component in address_info: 
        return address_info[component]
    else: 
        return 'NaN'

df = pd.read_csv('datasets/SeqDrawGeoData.csv')

# extract zip code 
df['zip'] = df.apply(get_address_component, axis=1, component='postcode')
df.drop(columns='X11th.Draw', inplace=True)
df = df[df.zip != '46394']

df['municipality'] = df.apply(get_address_component, axis = 1, component = 'municipality')
# drop zip from indiana 

df['suburb'] = df.apply(get_address_component, axis = 1, component = 'suburb')

# calculate median 
df['median'] = df.filter(like='Draw').apply(lambda x: x.median(), axis=1)
# print(df)

df = df[['Date.Sampled', 'Address', 'HCluster', 'zip', 'municipality', 'suburb', 'median']]

# calculate intervals 
df['interval'] = ['ppb < 5' if (x < 5) else '5 <= ppb < 15' if (x < 15) else '15 <= ppb' for x in df['median']]

zips = df.zip.unique()
# print(len(zips))

crosstab_zip = pd.crosstab(df['zip'],
                            df['interval'], 
                               margins = False)
crosstab_muni = pd.crosstab(df['municipality'], df['interval'], margins=False)
crosstab_muni = crosstab_muni.drop('NaN')
crosstab_suburb = pd.crosstab(df['suburb'], df['interval'], margins=False)
crosstab_suburb = crosstab_suburb.drop('NaN')
print(crosstab_zip)
print(crosstab_muni)
print(crosstab_suburb)

alpha = .05 
print('alpha: ', alpha)
stat, p, dof, expected = chi2_contingency(crosstab_zip)
print('ZIP vs Interval: p value = ', p, ', dof = ', dof)
stat, p, dof, expected = chi2_contingency(crosstab_muni)
print('Munipality vs Interval: p value = ', p, ', dof = ', dof)
stat, p, dof, expected = chi2_contingency(crosstab_suburb)
print('Suburb vs Interval: p value = ', p, ', dof = ', dof)
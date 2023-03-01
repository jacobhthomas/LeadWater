import pandas as pd 
import random
import geopandas
import geopy

def randN(N):
	min = pow(10, N-1)
	max = pow(10, N) - 1
	return str(random.randint(min, max))

def clean_addresses(address): 

    lst = list(address.split())
    
    nums_random = lst[0].count('X')
    
    lst[0] = lst[0].strip('X')
    
    # randomize the missing numbers? 
    # if nums_random > 0:
    #     add_block_num = randN(nums_random)
    #     lst[0] += str(add_block_num)

    lst[-1] = lst[-1].strip('*')
    lst[1] = CARDINAL_DICT[lst[1]]

    new_address = ' '.join(lst) + ', Chicago, IL'
    return new_address

# -----------------# 

df = pd.read_csv('relative_differences_sequential_data.csv')

df = df.drop(columns=['Unnamed: 0']) 

CARDINAL_DICT = {'W': 'West', 'N': 'North', 'E': 'East', 'S': 'South'}

df['Address'] = df['Address'].apply(clean_addresses)

print(df.head)
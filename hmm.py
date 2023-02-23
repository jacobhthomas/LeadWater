import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import hmm 
import matplotlib as mpl 
import matplotlib.cm as cm 

df = pd.read_csv('relative_differences_sequential_data.csv')
df = df.drop(columns=['Unnamed: 0']) 
print(df.columns)
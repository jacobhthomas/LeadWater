import numpy as np
import pandas as pd


def df_cleaned(df):
    print(df.shape)
    df = df.drop(0) 
    df = df.drop("Index",axis=1)
    df['Date.Sampled'] = pd.to_datetime(df['Date.Sampled'])
    for i in range(3,len(col_name)):
        df[col_name[i]] = df[col_name[i]].apply(pd.to_numeric)
    df.drop(df.columns[[13,14,15,16,17,18]],axis=1,inplace=True) 
    col_new = df.columns
    draw_cols = col_new[2:]

    for i in range(len(draw_cols)):
        df = df[df[draw_cols[i]].notnull()]
    return df

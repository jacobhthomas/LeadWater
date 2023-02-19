import pandas as pd 

df = pd.read_csv("sequential.csv")

# drop minute draws 
df = df.drop(columns=['3 Minute' , '5 Minute', '7 Minute', '10 Minute', '15 Minute', '20 Minute'])
draw_cols = list(df.columns)[2:]

# replace string vals 
replace_map = {'<1.00': .5, '1': .5, '<.5': .5}
df[draw_cols] = df[draw_cols].replace(replace_map)
df[draw_cols] = df[draw_cols].apply(pd.to_numeric, errors='coerce')

# make copy of dataframe
relative_differences_df = df.copy()

# calculate percent changes 
for i in range(len(draw_cols)-1): 
    relative_differences_df[draw_cols[i]] = (relative_differences_df[draw_cols[i+1]] - relative_differences_df[draw_cols[i]]) / relative_differences_df[draw_cols[i]]

# drop last row 
relative_differences_df = relative_differences_df.drop(columns=['11th Draw'])

# rename columns 
relative_differences_df = relative_differences_df.rename(columns={'1st Draw': 'x1x2','2nd Draw': 'x2x3','3rd Draw': 'x3x4','4th Draw': 'x4x5','5th Draw': 'x5x6',
                                        '6th Draw': 'x6x7','7th Draw': 'x7x8','8th Draw': 'x8x9','9th Draw': 'x9x10','10th Draw': 'x10x11',})

print(relative_differences_df.head())
relative_differences_df.to_csv('relative_differences_sequential_data.csv')

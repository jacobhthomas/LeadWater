import pandas as pd 

df = pd.read_csv("cleaned_sequential.csv")


# drop minute draws 
df = df.drop(columns=['Unnamed: 0', 'X3.Minute','X5.Minute', 'X7.Minute', 'X10.Minute', 'X15.Minute', 'X20.Minute'])

draw_cols = list(df.columns)[2:]

copy = df

# # replace string vals 
replace_map = {'<1.00': .5, '1': .5, '<.5': .5}
df[draw_cols] = df[draw_cols].replace(replace_map)
df[draw_cols] = df[draw_cols].apply(pd.to_numeric, errors='coerce')

# drop NaN values 
df.dropna(inplace=True)

# # make copy of dataframe
relative_differences_df = df.copy()

# # calculate percent changes 
for i in range(len(draw_cols)-1): 
    relative_differences_df[draw_cols[i]] = (relative_differences_df[draw_cols[i+1]] - relative_differences_df[draw_cols[i]]) / relative_differences_df[draw_cols[i]]

# drop last row 
relative_differences_df.drop(columns=['X11th.Draw'], inplace=True)

# rename columns 
relative_differences_df = relative_differences_df.rename(columns={'X1st.Draw': 'x1x2','X2nd.Draw': 'x2x3','X3rd.Draw': 'x3x4','X4th.Draw': 'x4x5','X5th.Draw': 'x5x6',
                                        'X6th.Draw': 'x6x7','X7th.Draw': 'x7x8','X8th.Draw': 'x8x9','X9th.Draw': 'x9x10','X10th.Draw': 'x10x11',})

# convert to date-time format
relative_differences_df['Date.Sampled'] = pd.to_datetime(relative_differences_df['Date.Sampled'])

relative_differences_df.to_csv('relative_differences_sequential_data.csv')

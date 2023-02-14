import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("sequential.csv")

# drop minute draws 
df = df.drop(columns=['3 Minute' , '5 Minute', '7 Minute', '10 Minute', '15 Minute', '20 Minute'])
draw_cols = list(df.columns)[2:]

# replace string vals 
replace_map = {'<1.00': .5, '1': .5, '<.5': .5}
df[draw_cols] = df[draw_cols].replace(replace_map)
df[draw_cols] = df[draw_cols].apply(pd.to_numeric, errors='coerce')

# make copy of dataframe
p_change_df = df.copy()

# calculate percent changes 
for i in range(len(draw_cols)-1): 
    p_change_df[draw_cols[i]] = (p_change_df[draw_cols[i+1]] - p_change_df[draw_cols[i]]) / p_change_df[draw_cols[i]]

# drop last row 
p_change_df = p_change_df.drop(columns=['11th Draw'])
p_change_draw_cols = draw_cols[:-1]

# plot each column as a histogram, taking the middle 90% of vals 
# for col in p_change_draw_cols: 
#     p_change_df.hist(column=col, range=[p_change_df[col].quantile(.05), p_change_df[col].quantile(.95)])
    # plt.show() 

x = [i for i in range(1,11)]
avgs = p_change_df.mean(axis=0, numeric_only=True)
medians = p_change_df.median(axis=0, numeric_only=True)

# plot averages 
# plt.scatter(x, avgs, s = 12, c='red') 
# plt.xlabel('Draw')
# plt.ylabel('Average Percent Change')
# plt.title('Average Percent Change vs Draw')
# plt.show() 

# plot medians 
# plt.scatter(x, medians, s = 12, c='red') 
# plt.xlabel('Draw')
# plt.ylabel('Median Percent Change')
# plt.title('Median Percent Change vs Draw')
# plt.show() 

# calculate pearson correlation coefficients  
corr_matrix = p_change_df.corr(method='pearson', numeric_only=True)
corr_matrix.to_csv('percent_change_corr_matrix.csv')




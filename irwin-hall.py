import numpy as np
import pandas as pd 
import math
from matplotlib import pyplot as plt
import scipy.stats as stats

# Adapted from https://en.wikipedia.org/wiki/Irwin%E2%80%93Hall_distribution
def IrwinHallCDF(n, x, approx="None"):
  # For n<=20, the CDF is numerically stable.
  # For n >20, set approx="Normal" to get the normal approximation to the CDF
  #     Exact standardized CDF will be within .0015 of normal approximation CDF
  if n>20 and approx=="None":
    print("Numerically unstable above n=20.")
    return(None)
  
  # To convert to approximate normal statistic, subtract mean n/2 and
  #   divide by sqrt of variance; a single uniform[0,1] has variance 1/12
  #   and variance is additive for independent random variables
  if approx=="Normal":
    return(stats.norm.cdf((x-n/2)*math.sqrt(12/n)))

  else:  
    sum = np.float128(0)
    a = np.array(
        [(-1)**k * (1/(np.float128(math.factorial(k))*np.float128(math.factorial(n-k))))*
        (np.float128(x)-k)**n for k in range(0,math.floor(x)+1)], 
        dtype=np.float128)
    return(np.sum(a, dtype=np.float128))

# average ppb above a certain threshold 
# income quantile is lower than the mean 
def one_side_test_low(ppb_threshold, df): 
    
    df_above_thresh=df[df['avg']>=ppb_threshold]

    # n = number of points of interest 
    # x = sum of quantiles of points of interest
    n = len(df_above_thresh.index)
    x = sum(df_above_thresh['quantile'])
    print(ppb_threshold, n)

    # return test statistic 
    return IrwinHallCDF(n=n, x=x, approx="Normal")

# average ppb is below a certain threshold 
# income quantile is higher than the mean 
def one_side_test_high(ppb_threshold, df): 
    
    df_above_thresh=df[df['avg']<=ppb_threshold]
    

    # n = number of points of interest 
    # x = sum of quantiles of points of interest
    n = len(df_above_thresh.index)
    x = sum(df_above_thresh['quantile'])

    # return test statistic 
    return (1-IrwinHallCDF(n=n, x=x, approx="Normal")) 


df = pd.read_csv('datasets/assessorSequential.csv')
df.drop(columns=['Unnamed: 0', 'PIN','Township Code', 'Sale Price', 'Neighborhood Code','Age','ZIP','Longitude','Latitude'], inplace=True)

df = df[df['Tract Median Income'].notna()]

df['avg'] = df.filter(like='Draw').apply(lambda x: x.mean(), axis=1)

# nQuantiles = total data points 
nQuantiles = len(df.index)

df = df[['Tract Median Income', 'avg']]
df.sort_values(by=['Tract Median Income'], inplace=True)



# df14 = df[df['avg'] < 15]
# df14 = df14[df14['avg'] >= 14]
# df15 = df[df['avg'] < 16]
# df15 = df15[df15['avg'] >= 15]
# df16 = df[df['avg'] < 17]
# df16 = df16[df16['avg'] >= 16]
# df17 = df[df['avg'] < 18]
# df17 = df17[df17['avg'] >= 17]
# print(df14, df15, df16, df17)

# plt.scatter(df14['Tract Median Income'], df14['avg'], c = 'r')
# plt.scatter(df15['Tract Median Income'], df15['avg'], c = 'black')
# plt.scatter(df16['Tract Median Income'], df16['avg'], c = 'g')
# plt.scatter(df17['Tract Median Income'], df17['avg'], c = 'blue')
# # plt.legend()
# plt.show() 

# calculate quantiles 
quantiles = np.linspace(float(1/(2*nQuantiles)), 1-float(1/(2*nQuantiles)), nQuantiles)
df['quantile'] = quantiles

thresholds = [x for x in range(5,25)]

one_side_low = [] 
one_side_high = [] 
for ppb in thresholds:  
  one_side_low.append(one_side_test_low(ppb,df))
  one_side_high.append(one_side_test_high(ppb,df))

print(one_side_low)
print(one_side_high)

# p_vals_scaled = [np.log(x) for x in one_side_low]

plt.scatter(thresholds, one_side_low, s=13)
plt.title('One-Sided Test Statistic: Irwin-Hall Distribution')
plt.xlabel('ppb Threshold')
plt.ylabel('log(p-value)')
plt.grid(True)
plt.axhline(0.05, c='r')
plt.xticks(thresholds)
plt.yscale("log")
plt.show() 

# plot for math newbies
plt.scatter(thresholds, one_side_low, s=20)
plt.title('Irwin-Hall Distribution Test Statistic')
plt.xlabel('lead level threshold')
plt.ylabel('statistical significance')
plt.grid(True)
plt.axhline(0.05, c='r')
plt.xticks(thresholds)
plt.yscale("log")
plt.show() 




# print(df_tests)
# # # ds = pd.Series([run_test(15,df, nQuantiles) for _ in range(3)])
# # df_tests.boxplot()
# # plt.title('One-Sided Test Statistic: Irwin-Hall Distribution')
# # plt.ylabel('p-value')
# # plt.xlabel('ppb Threshold')
# # plt.show()
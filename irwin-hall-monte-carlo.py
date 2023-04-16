import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import random

# Monte Carlo estimate for the Irwin-Hall CDF function for n random variables
# compared to x: Pr(X1+...+Xn <= x)
# It is a good idea to repeat this experiment mutiple times to get a sense of
# the error.

# Adapted from https://en.wikipedia.org/wiki/Irwin%E2%80%93Hall_distribution
def IrwinHallMonteCarloCDF(n, x, nQuantiles=1000, nSamples=10000):
  # nQuantiles: Use the total number of data points in your sample if known
  # n: use the number of "special" data points in your sample
  # x: use the sum of quantiles of "special" points in your sample
  # Quantiles are [1/(2*nQuantiles), 3/(2*nQuantiles), 5/(2*nQuantiles),1-1/(2*nQuanties)] for both all points and special
  
  # The returned value is the approximate value of P(X1+...+Xn <= x) 
  quantiles = tuple(np.linspace(float(1/(2*nQuantiles)), 1-float(1/(2*nQuantiles)), nQuantiles))
  sampleSums = [np.sum(random.sample(quantiles, n)) for _ in range(0,nSamples)]
  return((np.sum(list(map(lambda _: 1 if (_<=x) else 0, sampleSums)))/(float(nSamples))))

def run_test(ppb_threshold, df, nQuantiles): 
    
    df_above_thresh=df[df['avg']>=ppb_threshold]

    # n = number of points of interest 
    # x = sum of quantiles of poins of interest
    n = len(df_above_thresh.index)
    x = sum(df_above_thresh['quantile'])
    print(n, x) 

    # return test statistic 
    return IrwinHallMonteCarloCDF(n=n, x=x, nQuantiles=nQuantiles)


df = pd.read_csv('datasets/assessorSequential.csv')
df.drop(columns=['Unnamed: 0', 'PIN','Township Code', 'Sale Price', 'Neighborhood Code','Age','ZIP','Longitude','Latitude'], inplace=True)

df = df[df['Tract Median Income'].notna()]

df['avg'] = df.filter(like='Draw').apply(lambda x: x.mean(), axis=1)

# nQuantiles = total data points 
nQuantiles = len(df.index)

# normalize average ppb levels 
# min_avg = df['avg'].min() 
# max_avg = df['avg'].max() 
# df['avg_norm'] = (df['avg'] - min_avg) / (max_avg - min_avg)

df = df[['Tract Median Income', 'avg']]
df.sort_values(by=['Tract Median Income'], inplace=True)

# calculate quantiles 
quantiles = np.linspace(float(1/(2*nQuantiles)), 1-float(1/(2*nQuantiles)), nQuantiles)
df['quantile'] = quantiles

print(df)

df_tests = pd.DataFrame() 
thresholds = [5, 10]
for ppb in thresholds: 
  df_tests[str(ppb)] = pd.Series([run_test(ppb, df, nQuantiles) for _ in range(2)])

print(df_tests)
# ds = pd.Series([run_test(15,df, nQuantiles) for _ in range(3)])
df_tests['5'].plot.box()
plt.title('One-Sided Test Statistic: Irwin-Hall Distribution')
plt.ylabel('p-value')
plt.xlabel('ppb Threshold')
plt.show()
# plt.ylabel('p-value')
# plt.xlabel()
# plt.show()
# pd.DataFrame(ds).boxplot()
# plt.show()

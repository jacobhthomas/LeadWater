import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('datasets/CleanedSequentialData.csv')
df.drop(columns=['Unnamed: 0', 'X3.Minute','X5.Minute', 'X7.Minute', 'X10.Minute', 'X15.Minute', 'X20.Minute'], inplace=True)
avg = df.mean(axis=1, numeric_only=True)
df['avg'] = avg
df = df.dropna()

# print(df.describe())
cols = df.columns 
print(cols)

for col in ['X1st.Draw', 'X2nd.Draw', 'X3rd.Draw',
       'X4th.Draw', 'X5th.Draw', 'X6th.Draw', 'X7th.Draw', 'X8th.Draw',
       'X9th.Draw', 'X10th.Draw', 'X11th.Draw', 'avg']: 
    df.drop(df[df[col] > 100].index, inplace=True)

y = df['avg'].values.reshape(-1, 1)

model = LinearRegression() 
r_sq = []
intercepts = [] 
coefs = [] 
for col in cols[2:-1]: 
    x = df[col].values.reshape(-1,1)
    model.fit(x,y)

    r_sq.append(model.score(x, y))
    intercepts.append(model.intercept_)
    coefs.append(model.coef_)

    y_pred = model.intercept_ + model.coef_ * x 

    pred_y_name = col + '_predict'
    df[pred_y_name] = y_pred 

print(df.head)


sns.set(font_scale=.7)

fig, axes = plt.subplots(3,3, sharex=True, sharey = True, figsize = (15,9))

fig.suptitle('Linear Trend between Sequential Draws and Average Draw')
fig.supxlabel('Sequential Draw')
fig.supylabel('Average Draw')
for i, col in enumerate(cols[2:11]): 
    # sns.lineplot(data = df, x = col, y = col + '_predict', ax = axes[i//3, i%3])
    sns.scatterplot(data = df, x = col, y = 'avg', ax = axes[i//3, i%3], s=5, c = 'black')
    sns.lineplot(x=col, y=col + '_predict', data=df, ax = axes[i//3, i%3])
    axes[i//3, i%3].set_title(col + ':  ' + 'R-Sq= ' + str(round(r_sq[i], 4)) + 
                              ', y = ' + str(np.round(coefs[i][0][0], 4)) + 'x + ' + str(np.round(intercepts[i][0], 4)))
    axes[i//3, i%3].set_ylabel('')
    axes[i//3, i%3].set_xlabel('')
    print(i)

fig.tight_layout()
plt.subplots_adjust(left=.05)

plt.show() 

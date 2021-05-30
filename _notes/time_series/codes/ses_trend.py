import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('WWWusage.csv')
print(df.columns) # time, value

# get the numpy array
x = df['value'].values

xhat = np.zeros((x.shape[0] + 10,1))
l = np.zeros(x.shape)
b = np.zeros(x.shape)

# model parameters
alpha = 0.9
beta = 0.9

# set the initial values, typically ther are also found through optimization
l[0] = x[0]
xhat[0] = x[0]
b[0] = x[1] - x[0]

for i in range(1, x.shape[0]):
    l[i] = alpha * x[i] + (1-alpha) * (l[i-1] + b[i-1])
    b[i] = beta * (l[i] - l[i-1]) + (1-beta) * b[i-1]
    xhat[i] = l[i] + 1*b[i]

# forecast
for i in range(10):
    xhat[x.shape[0] + i] = l[-1] + (i+1)*b[-1]

fig, axs = plt.subplots(3,1, figsize=(10,10), sharex=True)

axs[0].set_title('Time Series')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Count')
axs[0].plot(x, color='blue', label='Original')
axs[0].plot(xhat, color='black', label='Forecast')
axs[0].legend()

axs[1].set_title('Level')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Count')
axs[1].plot(l)

axs[2].set_title('Trend')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Change')
axs[2].plot(b)

plt.tight_layout()
fig.savefig('time.png')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('elecdaily.csv')
print(df.columns) # Demand, Workday, Temperature

# get the numpy array
x = df['Demand'].values

xhat = np.zeros((x.shape[0] + 10,1))
l = np.zeros(x.shape)
b = np.zeros(x.shape)
s = np.zeros(x.shape)
m = 7 # weekly seasonality

# model parameters
alpha = 0.1
beta = 0.8
gamma = 0.6

# set the initial values, typically ther are also found through optimization
for i in range(m):
    l[i] = np.mean(x[:m])
    xhat[i] = x[i]
    b[i] = x[i+1] - x[i]
    s[i] = x[i] - l[i] - b[i]

# we use an additive model here
for i in range(m, x.shape[0]):
    l[i] = alpha * (x[i] - s[i-m]) + (1-alpha) * (l[i-1] + b[i-1])
    b[i] = beta * (l[i] - l[i-1]) + (1-beta) * b[i-1]
    s[i] = gamma * (x[i] - l[i-1] - b[i-1]) + (1-gamma)*s[i-m]
    xhat[i] = l[i] + 1*b[i] + s[i-m]

# forecast
for i in range(10):
    try:
        xhat[x.shape[0] + i] = l[-1] + (i+1)*b[-1] + s[x.shape[0]+i-m]
    except IndexError:
        xhat[x.shape[0] + i] = l[-1] + (i+1)*b[-1] + s[x.shape[0]+i-2*m]

fig, axs = plt.subplots(4,1, figsize=(10,13), sharex=True)

axs[0].set_title('Time Series')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Demand')
axs[0].plot(x, color='blue', label='Original')
axs[0].plot(xhat, color='black', label='Forecast')
axs[0].legend()

axs[1].set_title('Level')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Demand')
axs[1].plot(l)

axs[2].set_title('Trend')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Change')
axs[2].plot(b)

axs[3].set_title('Seasonality')
axs[3].set_xlabel('Time')
axs[3].set_ylabel('Seasonal Component')
axs[3].plot(s)

plt.tight_layout()
fig.savefig('time.png')

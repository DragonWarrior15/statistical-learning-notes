import numpy as np
import matplotlib.pyplot as plt

# we will consider a time series and plot its 
# sample acf and pacf functions
# x_{t} = 1.5x_{t-12} + -0.75x_{t-24} + w_{t} + 0.8w_{t-12}
# where w is white noise with 0 mean and constant variance

n = 1000 # no of points to simulate
w = np.random.randn(n)
x = np.zeros(n)
for i in range(24,n):
    x[i] = 1.5*x[i-12] - 0.75*x[i-24] + w[i] + 0.8*w[i-12]
x = x[12:]
n -= 12
# all following calculations are concerened with positive lags
"""
estimated acf can be calculated using the formula
\hat{\gamma}(h) = (1/n) \sum_{i=1}^{n-h}x_{i}x_{i+h}
and the function is symmetric around 0
"""
lags = 48
acf_sample = np.zeros(lags)
# calculate gamma for positive lags only
for h in range(lags):
    acf_sample[h] = (1.0/n) * np.dot(x[0:n-h], x[h:n])

# convert to rho
rho_0 = acf_sample[0]
for i in range(lags):
    acf_sample[i] /= rho_0


"""
sample pacf can be obtained by regressing the time steps in
consideration on all the intermediate time steps
PACF(x_{t}, x_{t+h}) = Cov(x_{t} - \hat{x}_{t}, x_{t+h} - \hat{x}_{t+h})
\hat{x}_{t} = linear combination of (x_{t+1}, x_{t+2}, .., x_{t+h-1})
"""
pacf_sample = np.zeros(lags)
# calculate gamma for positive lags only
for h in range(lags):
    # for lag 0 and 1, the value is same as acf and already set above
    if(h > 1):
        # least squares solution to y = X \beta is 
        # \beta = (X.T X)^{-1} X.T y
        X = np.zeros((n-h,h-1))
        for i in range(1,h):
            X[:,i-1] = x[i:n-h+i]
        x0 = x[0:n-h].reshape((-1,1))
        xh = x[h:].reshape((-1,1))
        hatx0 = x0 - np.matmul(X, np.matmul(np.linalg.inv(np.matmul(X.T,X)), np.matmul(X.T, x0)))
        hatxh = xh - np.matmul(X, np.matmul(np.linalg.inv(np.matmul(X.T,X)), np.matmul(X.T, xh)))
        pacf_sample[h] = ((1.0/n) * np.matmul(hatx0.T, hatxh))/(np.sqrt(np.var(hatx0) * np.var(hatxh)))
    else:
        # pacf will be same as acf since no conditional terms involved
        pacf_sample[h] = acf_sample[h]


fig, axs = plt.subplots(3,1, figsize=(12,12))
# plot the time series
axs[0].plot(list(range(1,n+1)), x, color='blue')
axs[0].set_title('Time Series x(t) = 1.5x(t-12) - 0.75x(t-24) + w(t) + 0.8w(t-12)')
axs[0].set_xlabel('t')
axs[0].set_ylabel('x(t)')

# plot the sample acf
# axs[1].set_ylim((0,1))
axs[1].axhline(0, xmin=0, xmax=lags, color='black')
for i in range(lags):
    axs[1].plot([i,i], [0,acf_sample[i]], color='blue')
axs[1].scatter(list(range(lags)), acf_sample, color='black')
# noise lines
axs[1].axhline(0.2, xmin=0, xmax=lags, color='navy', linestyle='--')
axs[1].axhline(-0.2, xmin=0, xmax=lags, color='navy', linestyle='--')
# title etc
axs[1].set_title('Estimated ACF')
axs[1].set_xlabel('Lag')
axs[1].set_ylabel('ACF')

# plot the sample pacf
# axs[1].set_ylim((0,1))
axs[2].axhline(0, xmin=0, xmax=lags, color='black')
for i in range(lags):
    axs[2].plot([i,i], [0,pacf_sample[i]], color='blue')
axs[2].scatter(list(range(lags)), pacf_sample, color='black')
# noise lines
axs[2].axhline(0.2, xmin=0, xmax=lags, color='navy', linestyle='--')
axs[2].axhline(-0.2, xmin=0, xmax=lags, color='navy', linestyle='--')
# title etc
axs[2].set_title('Estimated PACF')
axs[2].set_xlabel('Lag')
axs[2].set_ylabel('PACF')

plt.tight_layout()
# plt.show()
fig.savefig('time.png')

import numpy as np
import matplotlib.pyplot as plt

# we will consider a time series and plot its theoretical
# and sample acf functions
# x_{t} = 0.8w_{t} + 0.5w_{t-1} + 0.2w_{t-2}
# where w is white noise with 0 mean and constant variance

n = 1000 # no of points to simulate
w = np.random.randn(n)
x = 0.8*w[2:n] + 0.5*w[1:n-1] + 0.2*w[0:n-2]

# all following calculations are concerened with 21 lags
# 10 on either side of 0
"""
the theoretical acf is
gamma(0) = 1.5, gamma(+-1) = 0.4, gamma(+-2) = 0.16
all other lags have 0 acf
"""
acf_actual_x = np.arange(-10,11)
acf_actual_y = np.zeros(21)
acf_actual_y[10] = 0.93
acf_actual_y[9] = acf_actual_y[11] = 0.4
acf_actual_y[8] = acf_actual_y[12] = 0.16

"""
estimated acf can be calculated using the formula
\hat{\gamma}(h) = (1/n) \sum_{i=1}^{n-h}x_{i}x_{i+h}
and the function is symmetric around 0
"""

acf_est_y = np.zeros(21)
n = n - 2
# positive lags
for i in range(21):
    h = i - 10
    if(h >= 0):
        acf_est_y[i] = (1.0/n) * np.dot(x[0:n-h], x[h:n])
        acf_est_y[10-h] = acf_est_y[i]

fig, axs = plt.subplots(3,1, figsize=(16,10))
# plot the time series
axs[0].plot(list(range(1,n+1)), x)
axs[0].set_title('Time Series x(t) = 0.8w(t) + 0.5w(t-1) + 0.2w(t-2)')
axs[0].set_xlabel('t')
axs[0].set_ylabel('x(t)')

# plot the actual acf
axs[1].set_ylim((0,1))
for i in range(8,13):
    axs[1].axvline(acf_actual_x[i], ymin=0, ymax=acf_actual_y[i])
axs[1].scatter(acf_actual_x, acf_actual_y, color='black')
axs[1].set_title('Theoretical ACF')
axs[1].set_xlabel('Lag')
axs[1].set_ylabel('ACF')

# plot the estimated acf
axs[2].set_ylim((0,1))
for i in range(21):
    axs[2].axvline(acf_actual_x[i], ymin=0, ymax=acf_est_y[i])
axs[2].scatter(acf_actual_x, acf_est_y, color='black')
axs[2].set_title('Estimated ACF')
axs[2].set_xlabel('Lag')
axs[2].set_ylabel('ACF')

plt.tight_layout()
# plt.show()
fig.savefig('time.png')

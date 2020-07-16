import numpy as np
import matplotlib.pyplot as plt

n = 1000 # no of points to simulate
w = np.random.randn(n)
x = np.zeros(n)
y = np.zeros(n)
for i in range(3,n):
    x[i] = 2.5*x[i-1] - 2.25*x[i-2] + 0.75*x[i-3] + w[i] + 0.8*w[i-1] + 0.1*w[i-2]
    # y[i] = 1.5*y[i-1] - 0.75*y[i-2] + w[i] + 0.8*w[i-1] + 0.1*w[i-2]
    y[i] = x[i] - x[i-1]
x = x[3:]
y = y[3:]
n -= 3

fig, axs = plt.subplots(2,1, figsize=(10,8))
# plot the time series
axs[0].plot(list(range(1,n+1)), x, color='blue')
axs[0].set_title('Time Series x(t) = 2.5x(t-1) - 2.25x(t-2) + 0.75x(t-3) + w(t) + 0.8w(t-1) + 0.1w(t-2), non-stationary')
axs[0].set_xlabel('t')
axs[0].set_ylabel('x(t)')
# differenced series
axs[1].plot(list(range(1,n+1)), y, color='blue')
axs[1].set_title('Time Series y(t) = x(t) - x(t-1)')
axs[1].set_xlabel('t')
axs[1].set_ylabel('y(t)')

plt.tight_layout()
# plt.show()
fig.savefig('time.png')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
s = 2 * np.sin(x) + np.random.randn(x.shape[0])


fig, axs = plt.subplots(1, 1, figsize=(10,10))
axs.scatter(x, s, label='original series')

beta = [0.99, 0.9]
colors = ['red', 'black']
v = np.zeros((x.shape[0], len(beta)))
for j in range(len(beta)):
    for i in range(x.shape[0]):
        if(i == 0):
            v[0][j] = beta[j] * 0 + (1-beta[j]) * s[0]
        else:
            v[i][j] = beta[j] * v[i-1][j] + (1-beta[j]) * s[i]
    
    axs.plot(x, v[:,j], color=colors[j], lw=2, 
            label='exp average series ({:.2f})'.format(beta[j]))

axs.set_xlabel('t')
axs.set_ylabel('s')
axs.set_title('Exponential Moving Average')
plt.legend()
plt.savefig('temp.png', dpi=150)

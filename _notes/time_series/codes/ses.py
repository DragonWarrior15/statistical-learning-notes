import matplotlib.pyplot as plt
# the monthly sales time series
x = [266.0,145.9,183.1,119.3,180.3,168.5,231.8,224.5,192.8,
    122.9,336.5,185.9,194.3,149.5,210.1,273.3,191.4,287.0,
    226.0,303.6,289.9,421.6,264.5,342.3,339.7,440.4,315.9,
    439.3,401.3,437.4,575.5,407.6,682.0,475.3,581.3,646.9]

fig, axs = plt.subplots(1,2,figsize=(16,8))
axs[0].plot(x, color='black', label='original series')

colors = ['blue']*4 + ['red']*4 + ['black']*2
ls = ['-', '--', ':', '-.'] * 2 + [':', '--']
sse_list = []
for i in range(1,11):
    alpha = i/10.0
    # get the predictions
    xhat = [0]*len(x)
    xhat[0] = x[0]
    xhat[1] = x[0]
    for j in range(2,len(x)):
        xhat[j] = alpha * x[j-1] + (1-alpha) * xhat[j-1]
    # plot
    if(i%2==0):
        axs[0].plot(xhat, color=colors[i-1], ls=ls[i-1], label=str(round(alpha, 1)))
    # get sse
    sse = 0
    for j in range(len(x)):
        sse += (xhat[j] - x[j])**2
    sse /= len(x)
    sse_list.append(sse)

axs[0].legend()
axs[0].set_title('Predicted Time Series for different values of alpha')
axs[0].set_xlabel('Time Index')
axs[0].set_ylabel('x')

axs[1].scatter([i/10.0 for i in range(1,11)], sse_list, color='blue')
axs[1].set_title('SSE vs alpha')
axs[1].set_ylabel('SSE')
axs[1].set_xlabel('alpha')

plt.tight_layout()
fig.savefig('time.png')

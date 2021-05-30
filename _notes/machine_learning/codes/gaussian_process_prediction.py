# prediction using a gaussian process
import numpy as np
import matplotlib.pyplot as plt

# define the kernel (rbf)
sigma2 = 2 # variance of a data point
def K(x1,x2,l=1):
    return sigma2*np.exp(-((x1-x2)**2)/(2*(l**2)))

# define the observed data
n = 3 # number of observed points
x = np.linspace(0,5,n)
y = np.random.normal(0,sigma2,size=n) # add some noise for some variability
S = np.zeros((n, n)) # the covariance matrix
for i in range(n):
    for j in range(i,n):
        S[i][j] = S[j][i] = K(x[i], x[j]) # cov matrix is symmetric

# make the predictions
n1 = 100 # no of points to predict on
x1 = np.zeros(n1+n) # we will add the observed points for visualization
x1[:n1] = np.linspace(-2,7,n1)
x1[n1:] = x
n1 += n
x1 = np.sort(x1)
y1 = np.zeros((n1, 3)) # col 0 stores the mean prediction, 1 lower ci, 2 upper ci
for i in range(n1):
    k = np.ones(n) # define the vector k that will have n kernel values
    for j in range(n):
        k[j] = K(x1[i], x[j])
    # calculate the mean using k^T S^-1 f
    y1[i][0] = np.matmul(np.matmul(k.T, np.linalg.inv(S)),y)
    # calculate the variance using K(0) - k^T S^-1 k
    sigma = K(1,1) - np.matmul(np.matmul(k.T, np.linalg.inv(S)),k)
    y1[i][1] = y1[i][0] -2 * sigma
    y1[i][2] = y1[i][0] +2 * sigma

# setup the plot, add the mean curve
plt.plot(x1, y1[:,0], label='mean')
# add the observed points
plt.scatter(x,y, color='black', label='known data')
# add the confidence interval
plt.fill_between(x1, y1[:,1], y1[:,2], color='b', alpha=.1, label='95% CI')
plt.legend()
# show the plot
plt.show()

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm

# set the seed
np.random.seed(42)

# create dummy data with different degrees of correlations
for correlation_val in np.arange(0.9, 1.0, 0.01):
    print(correlation_val)
    # generate a multinomial gaussian with above covariance
    cov_matrix = np.array([[1.0, correlation_val], [correlation_val, 1.0]])
    # generate some points
    n_points = 1000
    if(correlation_val < 1):
        X = np.random.multivariate_normal(mean=np.array([0,0]), 
                                             cov=cov_matrix,
                                             size=n_points)
    else:
        X = np.tile(np.random.normal(size=(n_points, 1)), reps=2)

    X = np.tile(np.random.normal(size=(n_points, 1)), reps=2)
    X[:, 1] = X[:, 0] * 3 + np.random.normal(scale=1-correlation_val, size=(n_points,))
    print('correlation between Xs is', np.corrcoef(X[:, 0], X[:, 1]))
    # plt.scatter(X[:, 0], X[:, 1])
    # plt.show()

    # create y as some function of X plus noise
    y = np.matmul(X, np.array([[11], [5]])) + np.random.normal(scale=0.6, size=(n_points, 1)) + 3

    # fit the model using sklearn linear regression
    model = LinearRegression()
    model.fit(X, y)
    print('coefficients from iterative solver', model.coef_, model.intercept_)

    # fit the model with statsmodels
    X1 = sm.add_constant(X)
    model = sm.OLS(y, X1)
    results = model.fit()
    print(results.summary())

    # get the coefficients using a closed form solution
    X = np.hstack([X, np.ones((1000, 1))])
    print('coefficients from closed form solution', 
        np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), y))

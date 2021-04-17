import numpy as np
import matplotlib.pyplot as plt

def data_prep(N = 100, r = 1, noise=0.0):
    """points inside radius = 1 are classified as class 1
    while points outside will be class 0, noise will control some
    intermixing of the classes"""
    X = 4 * r * np.random.random((N, 2)) - 2 * r
    Y = np.zeros(N)
    _filter = np.power(X, 2).sum(axis=1) < r**2
    Y[_filter] = 1
    # tweak the classes randomly according to noise
    _noise = np.random.random(N)
    # invert the class in the radius +- noise region
    _filter = (np.power(X, 2).sum(axis=1) < (r*(1+_noise))**2) * \
                (np.power(X, 2).sum(axis=1) > (r*(1-_noise))**2)
    Y[(_noise < noise) * _filter] = 1 - Y[(_noise < noise) * _filter]
    # return X and Y
    return X, Y

_radius = 2
N = 1000
_noise = 0.2
X, Y = data_prep(N=N, r=_radius, noise=_noise)
_colors = ['red' if Y[i] == 1 else 'blue' for i in range(Y.shape[0])]

# plot the input data
fig, axs = plt.subplots(1, 1, figsize=(10,10))
axs.scatter(X[:,0], X[:,1], c=_colors)
axs.set_xlabel('x')
axs.set_ylabel('y')
axs.set_xlim(-2 * _radius, 2 * _radius)
axs.set_ylim(-2 * _radius, 2 * _radius)
axs.set_title('Plot of Input Data (Noise={:.2f})'.format(_noise))
fig.savefig('backprop_input.png', dpi=150)


# initialize the dimensions
dim_in = 2
dim_1 = 4
dim_2 = 2
dim_3 = 1
# initialize the weights
W1 = np.random.randn(dim_in, dim_1)
W2 = np.random.randn(dim_1, dim_2)
W3 = np.random.randn(dim_2, dim_3)
b1 = np.random.randn(dim_1)
b2 = np.random.randn(dim_2)
b3 = np.random.randn(dim_3)

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1/(1 + np.exp(-1 * x))

def forward(X, W1, W2, W3, b1, b2, b3):
    _cache = {'X':X}
    X = np.matmul(X, W1) + b1
    _cache['X1'] = X.copy()
    X = relu(X)
    _cache['X1r'] = X.copy()
    X = np.matmul(X, W2) + b2
    _cache['X2'] = X.copy()
    X = relu(X)
    _cache['X2r'] = X.copy()
    X = np.matmul(X, W3) + b3
    _cache['X3'] = X.copy()
    X = sigmoid(X)
    _cache['yhat'] = X.copy()
    return X, _cache

def loss(y_true, y_pred):
    y_pred = y_pred.reshape((-1,))
    y = np.multiply(y_true, np.log(y_pred)) + \
                    np.multiply(1 - y_true, np.log(1 - y_pred))
    return -np.mean(y)

def backward(y_true, _cache, learning_rate, W1, W2, W3, b1, b2, b3):
    y_true = y_true.reshape((-1,1))
    N = y_true.shape[0]
    lr=learning_rate
    y_pred = _cache['yhat']
    # derivative of loss wrt y predicted
    dL_dyhat = -(1.0/N) * (((y_true)/(y_pred)) - ((1 - y_true)/(1 - y_pred)))
    # derivative of loss wrt X3
    dL_dX3 = np.multiply(dL_dyhat, np.multiply(y_pred, (1 - y_pred)))
    # derivative of loss wrt W3
    dL_dW3 = np.matmul(_cache['X2r'].T, dL_dX3)
    # derivative of loss wrt b3
    dL_db3 = np.matmul(np.ones(N).T, dL_dX3)
    # derivative of loss wrt X2r
    dL_dX2r = np.matmul(dL_dX3, W3.T)
    # derivative of loss wrt relu
    dL_dX2 = np.multiply(dL_dX2r, _cache['X2'] > 0)
    # derivative of loss wrt W2
    dL_dW2 = np.matmul(_cache['X1r'].T, dL_dX2)
    # derivative of loss wrt b2
    dL_db2 = np.matmul(np.ones(N).T, dL_dX2)
    # derivative of loss wrt X1r
    dL_dX1r = np.matmul(dL_dX2, W2.T)
    # derivative of loss wrt X1
    dL_dX1 = np.multiply(dL_dX1r, _cache['X1'] > 0)
    # derivative of loss wrt W1
    dL_dW1 = np.matmul(_cache['X'].T, dL_dX1)
    # derivative of loss wrt b1
    dL_db1 = np.matmul(np.ones(N).T, dL_dX1)
    # begin updating the weights
    b3 -= lr * dL_db3
    b2 -= lr * dL_db2
    b1 -= lr * dL_db1
    W3 -= lr * dL_dW3
    W2 -= lr * dL_dW2
    W1 -= lr * dL_dW1
    # return the updated weights
    return W1, W2, W3, b1, b2, b3

# train the model
batch_size = 100
for iteration in range(501):
    # for every batch, do the update
    for idx in range(N//batch_size):
        _X = X[batch_size*idx:batch_size*(idx+1)]
        _Y = Y[batch_size*idx:batch_size*(idx+1)]
        y_pred, _cache = forward(_X, W1, W2, W3, b1, b2, b3)
        l = loss(_Y, y_pred)
        W1, W2, W3, b1, b2, b3 = backward(_Y, _cache, 0.03, W1, W2, W3, b1, b2, b3)
    if(iteration % 10 == 0):
        print("Iteration: {:4d} Loss: {:.5f}".format(iteration, l))

# plot the contour data
xg = np.linspace(-2 * _radius, 2 * _radius, 200)
# create the 2d grid to make predictions
xg, yg = np.meshgrid(xg, xg)
level_pred, _ = forward(np.hstack([xg.reshape(-1,1), yg.reshape(-1,1)]),\
                     W1, W2, W3, b1, b2, b3)
level_pred = level_pred.reshape(xg.shape)
fig, axs = plt.subplots(1, 1, figsize=(10,10))
axs.contourf(xg, yg, level_pred, cmap="RdBu_r", alpha=0.5)
axs.scatter(X[:,0], X[:,1], c=_colors)
axs.set_xlabel('x')
axs.set_ylabel('y')
axs.set_xlim(-2 * _radius, 2 * _radius)
axs.set_ylim(-2 * _radius, 2 * _radius)
axs.set_title('Plot of Neural Network Contours')
fig.savefig('backprop_output.png', dpi=150)

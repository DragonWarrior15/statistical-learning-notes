import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
import pickle

np.random.seed(1000)

def data_prep(N = 100, noise=0.0):
    """a periodic wave with some noise"""
    _r = 20
    _x = np.arange(0, _r*np.pi, _r*np.pi/N).reshape(-1,1)
    # output is trend + seasonality + noise
    X = 0.0*_x + 0.5*np.sin(_x) + 0.5*np.cos(_x) + np.random.normal(scale=noise, size=_x.shape)
    # do not return Y as that will depend on the architecture
    # and can be created later
    return _x, X

N = 1000
_noise = 0.1
_x, X = data_prep(N=N, noise=_noise)

# plot the input data
fig, axs = plt.subplots(1, 1, figsize=(10,10))
axs.plot(_x, X)
axs.set_xlabel('t')
axs.set_ylabel('x')
# axs.set_xlim(-2 * _radius, 2 * _radius)
# axs.set_ylim(-2 * _radius, 2 * _radius)
axs.set_title('Plot of Input Data (Noise={:.2f})'.format(_noise))
fig.savefig('bptt_input.png', dpi=150)

# initialize the dimensions
dim_dict = {
    'in' : 1, # dimension of input vector
    't_in' : 8, # input time steps
    'h' : 8, # hidden state dimensions
    'out' : 1, # dimension of output vector
    't_out' : 1, # no of time steps to use in loss calculation    
}

# initialize the weights, Xavier initialization since tanh
# Wxh = np.random.randn(dim_dict['in'], dim_dict['h']) \
                # * np.sqrt(2/(dim_dict['in']+ dim_dict['h']))
# Whh = np.random.randn(dim_dict['h'], dim_dict['h']) \
                # * np.sqrt(2/(dim_dict['h']+ dim_dict['h']))
# Why = np.random.randn(dim_dict['h'], dim_dict['out'])
# bh = np.random.randn(dim_dict['h'])
# by = np.random.randn(dim_dict['out'])

# Xavier uniform weights initialization
Wxh = np.random.uniform(low=-np.sqrt(6/(dim_dict['in']+ dim_dict['h'])),
                        high=np.sqrt(6/(dim_dict['in']+ dim_dict['h'])),
                        size=(dim_dict['in'], dim_dict['h']))
Whh = np.random.uniform(low=-np.sqrt(6/(dim_dict['h']+ dim_dict['h'])),
                        high=np.sqrt(6/(dim_dict['h']+ dim_dict['h'])),
                        size=(dim_dict['h'], dim_dict['h']))
Why = np.random.uniform(low=-np.sqrt(6/(dim_dict['h']+ dim_dict['out'])),
                        high=np.sqrt(6/(dim_dict['h']+ dim_dict['out'])),
                        size=(dim_dict['h'], dim_dict['out']))
bh = np.zeros(dim_dict['h'])
by = np.zeros(dim_dict['out'])

def tanh(x):
    return np.tanh(x)

def forward(X, Wxh, Whh, Why, bh, by, dim_dict):
    # X should be of shape N x t_in x in
    N = X.shape[0]
    _cache = {
        'X':X,
        'a':[],
        'h':[],
        'yhat':[]
    }
    a, h, yhat = 0, 0, 0
    # loop through all the timesteps
    for t in range(dim_dict['t_in']):
        if(t == 0):
            a = np.matmul(X[:, t, :], Wxh) + \
                    np.matmul(np.zeros((N, dim_dict['h'])), Whh) + bh
        else:
            a = np.matmul(X[:, t, :], Wxh) + np.matmul(_cache['h'][-1], Whh) + bh
        _cache['a'].append(a)
        h = tanh(a)
        _cache['h'].append(h)
        yhat = np.matmul(h, Why) + by
        _cache['yhat'].append(yhat)
    # prepare pred only for indices that are going to be part of output
    y_pred = np.zeros((N, dim_dict['t_out'], dim_dict['out']))
    for i, t in enumerate(range(-dim_dict['t_out'], 0, 1)):
        y_pred[:, i, :] = _cache['yhat'][t]
    # return
    return y_pred, _cache

def loss(y_true, y_pred):
    # use mean squared error across time steps
    return 0.5 * np.mean(np.power(y_true - y_pred, 2).sum(axis=1))

def backward(y_true, _cache, learning_rate, Wxh, Whh, Why, bh, by, dim_dict):
    N = _cache['X'].shape[0]
    lr=learning_rate
    # derivative of loss wrt y predicted
    # if the shape of y_true and yhat is not same,
    # adjust ytrue while calculating gradient so that
    # the gradient is zero where ytrue may not be available (if t out < tin)
    dL_dyhat = []
    for t in range(dim_dict['t_in']):
        if(t == 0 or t < dim_dict['t_in'] - dim_dict['t_out']):
            # 0th index is anyways ignored, otherwise
            # the yhat at this time step is not used for loss calculation
            dL_dyhat.append(np.zeros(_cache['yhat'][t].shape))
        else:
            dL_dyhat.append((1/N) * (_cache['yhat'][t] - \
                                y_true[:, t -(dim_dict['t_in']- dim_dict['t_out'])]))

    # derivative of loss wrt Why
    dL_dWhy = np.zeros(Why.shape)
    for t in range(dim_dict['t_in']):
        dL_dWhy += np.matmul(_cache['h'][t].T, dL_dyhat[t])
    dL_dWhy *= (1/dim_dict['t_out'])

    # derivative of loss wrt by
    dL_dby = np.zeros(by.shape)
    for t in range(dim_dict['t_in']):
        dL_dby += np.matmul(np.ones(N).T, dL_dyhat[t])
    dL_dby *= (1/dim_dict['t_out'])

    # derivative of loss with respect to the hidden states
    # and activations depend on one another and will be solved
    # from the right (highest time index) to help with the recursion
    # dl/dht = dL/dyhatt Why.T + dL/dat+1 Whh.T
    # dL/dat = dL/dht dht/dat = dL/dht * (1 - ht^2)
    dL_dh = [0] * (dim_dict['t_in'])
    dL_da = dL_dh.copy()
    for t in range(dim_dict['t_in']-1, -1, -1):
        if(t == dim_dict['t_in']-1):
            # the highest t calculation
            dL_dh[t] = np.matmul(dL_dyhat[t], Why.T)
        else:
            dL_dh[t] = np.matmul(dL_dyhat[t], Why.T) + \
                            np.matmul(dL_da[t + 1], Whh.T)

        dL_da[t] = np.multiply(dL_dh[t], (1 - np.power(_cache['h'][t], 2)))

    # derivative of loss wrt Wxh, Whh, bh
    # simply use that fact that L is dependent on all at,
    # and dat/dWxh is simple to compute due to it being a dense layer
    dL_dWxh = np.zeros(Wxh.shape)
    dL_dWhh = np.zeros(Whh.shape)
    dL_dbh  = np.zeros(bh.shape)
    for t in range(len(dL_da)):
        dL_dWxh += np.matmul(_cache['X'][:, t, :].T, dL_da[t])
        dL_dWhh += np.matmul(_cache['h'][t].T, dL_da[t])
        dL_dbh += np.matmul(np.ones(N).T, dL_da[t])

    # begin updating the weights
    Wxh -= lr * np.clip(dL_dWxh, a_min=-10, a_max=10)
    Whh -= lr * np.clip(dL_dWhh, a_min=-10, a_max=10)
    Why -= lr * np.clip(dL_dWhy, a_min=-10, a_max=10)
    bh  -= lr * np.clip(dL_dbh, a_min=-10, a_max=10)
    by  -= lr * np.clip(dL_dby, a_min=-10, a_max=10)
    # return the updated weights
    return Wxh, Whh, Why, bh, by

def prepare_model_seq_data(X):
    # rearrange the input data to make it in sequence format N x timesteps x dim
    N = X.shape[0]
    X_model = np.zeros((N - dim_dict['t_in']+1 - dim_dict['t_out'],
                        dim_dict['t_in'], dim_dict['in']))
    # correctly fill shifted versions of input
    for t in range(dim_dict['t_in']):
        X_model[:, t, :] = X[t:t+X_model.shape[0]]

    Y_model = np.zeros((X_model.shape[0],
                        dim_dict['t_out'], dim_dict['out']))
    for t in range(dim_dict['t_out']):
        Y_model[:, t, :] = X[dim_dict['t_in']+t:X_model.shape[0]+dim_dict['t_in']+t]

    return X_model, Y_model

X_model, Y_model = prepare_model_seq_data(X)

# train the model
batch_size = 100
for iteration in range(500):
    # shuffle before putting into model
    idxs = np.arange(X_model.shape[0])
    np.random.shuffle(idxs)
    # for every batch, do the update
    for idx in range(N//batch_size):
        _X = X_model[idxs[batch_size*idx:batch_size*(idx+1)]]
        _Y = Y_model[idxs[batch_size*idx:batch_size*(idx+1)]]
        # forward and backward passes
        y_pred, _cache = forward(_X, Wxh, Whh, Why, bh, by, dim_dict)
        l = loss(_Y, y_pred)
        Wxh, Whh, Why, bh, by = backward(_Y, _cache, 1e-5, 
                                    Wxh, Whh, Why, bh, by, dim_dict)
    if(iteration % 100 == 0):
        print("Iteration: {:4d} Loss: {:.5f}".format(iteration, l))


Y_pred, _ = forward(X_model, Wxh, Whh, Why, bh, by, dim_dict)

pd.DataFrame(np.hstack([X_model.reshape(-1, dim_dict['t_in']), 
                Y_model.reshape(-1, dim_dict['t_out']),
                Y_pred.reshape(-1, dim_dict['t_out'])])).to_csv('temp.csv')


# plot the series
fig, axs = plt.subplots(1, 1, figsize=(16,10))
_x = _x[dim_dict['t_in']:dim_dict['t_in']+Y_model.shape[0]]
axs.plot(_x, Y_model.reshape(-1,1), label='true')
axs.plot(_x, Y_pred.reshape(-1,1), label='predicted')
plt.legend()
axs.set_xlabel('x')
axs.set_ylabel('y')
axs.set_title('Simple RNN training example')
fig.savefig('bptt_output.png', dpi=150)

"""
Iteration:    0 Loss: 0.01198
Iteration:  100 Loss: 0.01142
Iteration:  200 Loss: 0.00858
Iteration:  300 Loss: 0.00999
Iteration:  400 Loss: 0.00863
"""

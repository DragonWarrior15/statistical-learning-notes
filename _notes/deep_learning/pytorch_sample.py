import torch
import numpy as np

n = 5000
x = np.ones((n,2))
x[:,0] = 100 * np.random.rand(n)
y = np.matmul(x, np.array([[10],[20]])) + np.random.randn(n).reshape(-1,1)

X = torch.tensor(x)
Y = torch.tensor(y)

def loss(y_true, y_pred):
    return torch.mean(torch.pow(y_true - y_pred, 2))

params = torch.tensor([[1.0], [0.0]], requires_grad=True, dtype=torch.float64)

optimizer = torch.optim.SGD([params], lr=1e-5)

for i in range(500):
    optimizer.zero_grad()
    train_loss = loss(Y, torch.matmul(X, params))
    train_loss.backward()
    optimizer.step()
    # print(params.grad)
    if(i%20==0):
        print('Epoch %4d loss %.5f' % (i, float(train_loss)))


---
title: "Gradients for Common Loss Functions"
---

# Gradients for Common Loss Functions

## Mean Square Loss

### Single Data Point

The predictions and loss are given by
\begin{align}
    x &\in \mathbb{R}^{p}, \; W \in \mathbb{R}^{p}, \; b \in \mathbb{R}\newline
    \hat{y} &= x^{T}W + b\newline
    L &= \frac{1}{2}(y - \hat{y})^{2}\end{align}
Taking the derivatives,
\begin{align}
    \frac{dL}{d\hat{y}} &= -(y - \hat{y})\newline
    \frac{d\hat{y}}{dW} &= \big( x_{1}, x_{2}, \ldots, x_{p} \big)^{T} = x\newline
    \frac{dL}{dW} &= \frac{dL}{d\hat{y}} \frac{d\hat{y}}{d}\newline
    &= (\hat{y} - y) x\end{align}

### Multiple Data Points

Now, we have a matrix $X$ ($N$ data points) instead of a vector $x$
\begin{align}
    X &\in \mathbb{R}^{N \times p}, \; W \in \mathbb{R}^{p}, \; b \in \mathbb{R}\newline
    \hat{y} &= XW + b\newline
    L &= \frac{1}{2N}\lVert (y - \hat{y}) \rVert^{2}
    = \frac{1}{2N}(y - \hat{y})^{T}(y - \hat{y})\newline\end{align}
Note that $b$ will be broadcasted across $XW$ when used. Another possibility is to include a columns of ones in the matrix and remove the additional bias term altogether. Taking the derivatives
\begin{align}
    \frac{dL}{d\hat{y}} &= \big( \frac{dL}{d\hat{y}\_1}, \frac{dL}{d\hat{y}\_2}, \ldots, \frac{dL}{d\hat{y}\_N} \big)^{T}\newline
    L &= \frac{1}{2N}\lVert (y - \hat{y}) \rVert^{2} = \frac{1}{2N} \sum_{i=1}^{N} (y_{i} - \hat{y}\_{i})^{2}\newline
    \frac{dL}{d\hat{y}\_{i}} &= \frac{1}{2N} \times 2(y_{i} - \hat{y}\_{i})(-1)
    = \frac{1}{N}(\hat{y}\_{i} - y_{i})\newline
    \frac{dL}{d\hat{y}} &= \frac{1}{N}(\hat{y} - y) \quad \text{dimensions}\; N \times 1\newline\end{align}
Now let's consider the derivative of $\hat{y}$ with $W$
\begin{align}
    \frac{d\hat{y}}{dW} &= \begin{bmatrix}
        \frac{d\hat{y}\_{1}}{dW_{1}}, &\cdots &\frac{d\hat{y}\_{1}}{dW_{p}}\newline
        \vdots &\ddots &\vdots\newline
        \frac{d\hat{y}\_{N}}{dW_{1}}, &\cdots &\frac{d\hat{y}\_{N}}{dW_{p}}\newline
    \end{bmatrix}\newline
    \frac{d\hat{y}\_{j}}{dW_{i}} &= \frac{d}{dW_{i}}\sum_{k=1}^{p}X_{jk}W_{k}\newline
    &= X_{ji}\newline
    \frac{d\hat{y}}{dW} &= X\newline
    \frac{dL}{dW} &= \frac{dL}{d\hat{y}} \frac{d\hat{y}}{dW}
    = \frac{1}{N}X^{T}(\hat{y} - y) \quad \text{dimensions}\; p \times 1\newline\end{align}

## Binary Cross Entropy/LogLoss

### Single Data Point

Suppose we get the prediction $\hat{y}$ from our model corresponding to the probability $P(y=1|X)$, for true label $y$. The logloss is defined by
\begin{align}
    L = -(ylog(\hat{y}) + (1-y)log(1-\hat{y})\end{align}
The gradient becomes
\begin{align}
    \frac{dL}{d\hat{y}} &= -\frac{d}{d\hat{y}} (ylog(\hat{y}) + (1-y)log(1-\hat{y})\newline
    &= -(\frac{y}{\hat{y}} - \frac{1-y}{1 - \hat{y}})\end{align}

### Multiple Data Points

Instead of a single prediction, now $\hat{y} \in \mathbb{R}^{N}$. The same is true for $y$. The Loss is calculated as
\begin{align}
    L = -\frac{1}{N} \big( y^{T}log(\hat{y}) + (1-y)^{T}log(1-\hat{y})) \big)\end{align}
where $L \in \mathbb{R}$ and log operations are applied element-wise. The gradient with $\hat{y}$ becomes
\begin{align}
    \frac{dL}{d\hat{y}} &= -\frac{1}{N}\big( \frac{dL}{d\hat{y}\_{1}}, \ldots, \frac{dL}{d\hat{y}\_{N}} \big)\newline
    \frac{dL}{d\hat{y}\_{i}} &= -\frac{1}{N} \bigg( \frac{y_{i}}{\hat{y}\_{i}} - \frac{1-y_{i}}{1-\hat{y}\_{i}} \bigg)\newline
    \frac{dL}{d\hat{y}} &= -\frac{1}{N} \big( \frac{y}{\hat{y}} - \frac{1-y}{1-\hat{y}} \big)\end{align}
where the division operations are element wise.

## Cross Entropy Loss

### Single Data Point

Suppose in the output $\hat{y}$, we have $k$ dimensions which represent a valid probability distribution (i.e., the entries sum upto 1). This can be achieved by applying the softmax activation on the outputs of the model. The loss is defined as
\begin{align}
    L = -\sum_{i=1}^{k}y_{i}log(\hat{y}\_{i})\end{align}
and the gradient becomes
\begin{align}
    \frac{dL}{d\hat{y}} = -\bigg(\frac{dL}{d\hat{y}\_{1}}, \ldots, \frac{dL}{d\hat{y}\_{k}} \bigg)^{T}
    =-\bigg(\frac{y_{1}}{\hat{y}\_{1}}, \ldots, \frac{y_{k}}{\hat{y}\_{k}} \bigg)^{T}
    = -\bigg(\frac{y}{\hat{y}} \bigg)\end{align}
where the division operation is element-wise. This gradient is a case of scalar by vector since $\hat{y}$ is a $k$-dimensional output.

### Multiple Data Points

The output is now a $N \times k$ sized matrix. The loss will consist of two operations, first sum along the second dimension, and then average along the remaining dimension.
\begin{align}
    L = -\frac{1}{N} \sum_{i=1}^{N} \sum_{j=1}^{k} y_{ij}log(\hat{y}\_{ij})\end{align}
where $y$ is a one-hot encoded matrix. The gradient is a $N \times p$ matrix given by
\begin{align}
    \frac{dL}{d\hat{y}\_{ij}} &= -\frac{1}{N} \frac{d}{d\hat{y}\_{ij}} \sum_{i=1}^{N} \sum_{j=1}^{k} y_{ij}log(\hat{y}\_{ij})
    = -\frac{1}{N} \frac{y_{ij}}{\hat{y}\_{ij}}\newline
    \frac{dL}{d\hat{y}} &= -\frac{1}{N} \frac{y}{\hat{y}}\end{align}
where the division is an element-wise operation.

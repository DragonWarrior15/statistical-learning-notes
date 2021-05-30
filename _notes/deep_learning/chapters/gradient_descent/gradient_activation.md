---
title: "Gradients for Common Activation Functions"
---

# Gradients for Common Activation Functions

## Sigmoid

### Single Data Point

Let $z$ be the output of model, and $p$ be obtained after the sigmoid operation
\begin{align}
    p &= \sigma(z) = \frac{1}{1 + exp(-z)}\newline
    \frac{dp}{dz} &= \frac{(1 + exp(-z))(0) - (1)(-exp(-z))}{(1 + exp(-z))^{2}} = \frac{1}{1 + exp(-z)} \bigg(1 - \frac{1}{1 + exp(-z)} \bigg)\newline
    &= p(1-p)\end{align}

### Multiple Data Points

Let $z,p \in \mathbb{R}^{n}$. Since this is an element-wise transformation, we leverage the Vector Jacobian Product (VJP)
\begin{align}
    \frac{dL}{dz} &= \frac{dL}{dp}\odot p\odot (1-p)\end{align}

## Softmax

### Single Data Point

Let $z \in \mathbb{R}^{k}$ be the $k$ outputs from the last layer of a neural network. To convert these real numbers to probabilities, we use the softmax function
\begin{align}
    s &= \bigg( \frac{exp(z_{1})}{\sum_{i=1}^{k}\exp(z_{i})}, \frac{exp(z_{2})}{\sum_{i=1}^{k}\exp(z_{i})}, \ldots, \frac{exp(z_{k})}{\sum_{i=1}^{k}\exp(z_{i})} \bigg)^{T}\end{align}
where $s$ and $z$ are vectors with the same dimensions. Thus the derivative will be a matrix
\begin{align}
    \frac{ds}{dz} &= \begin{bmatrix}
        \frac{\partial s_{1}}{\partial x_{1}}, &\cdots &\frac{\partial s_{1}}{\partial x_{k}}\newline
        \vdots &\ddots &\vdots\newline
        \frac{\partial s_{k}}{\partial x_{1}}, &\cdots &\frac{\partial s_{k}}{\partial x_{k}}\newline
    \end{bmatrix}\newline
    \frac{ds_{j}}{dz_{i}} &= \frac{d}{dz_{i}} \frac{exp(z_{j})}{\sum_{i=1}^{k}\exp(z_{i})}
    = \frac{-exp(z_{j})exp(z_{i})}{\big( \sum_{i=1}^{k}\exp(z_{i}) \big)^{2}}\newline
    &= -s_{j}s_{i}\newline
    \frac{ds_{i}}{dz_{i}} &= \frac{d}{dz_{i}} \frac{exp(z_{i})}{\sum_{i=1}^{k}\exp(z_{i})}
    = \frac{(\sum_{i=1}^{k}\exp(z_{i}))exp(z_{i}) - exp(z_{i})(exp(z_{i}))}{\big( \sum_{i=1}^{k}\exp(z_{i}) \big)^{2}}\newline
    &= \frac{exp(z_{i})}{\sum_{i=1}^{k}\exp(z_{i})} \bigg(1 -  \frac{exp(z_{i})}{\sum_{i=1}^{k}\exp(z_{i})}\bigg)\newline
    &= s_{i}(1 - s_{i}) = s_{i} - s_{i}^{2}\newline
\end{align}
Thus the off diagonal entries are simply products of the $y$ values at the corresponding indices. We form one matrix consisting of such values. For the diagonal entries, some additional manipulation is needed which is obtained by diagonal matrix consisting of $y$.
\begin{align}
    \frac{ds}{dz} = diag(s) - ss^{T} = J\end{align}
where $J$ is the Jacobian matrix. Next, let's calculate the gradient
\begin{align}
    \frac{dL}{dz} &= \frac{dL}{ds} \frac{ds}{dz}\newline
    &= J^{T} \bigg( \frac{dL}{ds_{1}}, \ldots, \frac{dL}{ds_{k}} \bigg)^{T}\newline
    \frac{dL}{dz_{i}} &= s_{i}(1-s_{i})\frac{dL}{ds_{i}} - \sum_{j=1, j\neq i}^{k}s_{i}s_{j}\frac{dL}{ds_{j}}\newline
    &= s_{i}\frac{dL}{ds_{i}} - s_{i} \bigg( \sum_{j=1}^{k}\frac{dL}{ds_{j}}s_{j} \bigg)\end{align}
We have a common calculation across all gradients
\begin{align}
    \sum_{j=1}^{k}\frac{dL}{ds_{j}}s_{j} = s^{T}\frac{dL}{ds} = c\end{align}
since $dL/ds$ is shape $k \times 1$ and $s$ is $k \times 1$. The gradient simplifies to
\begin{align}
    \frac{dL}{dz_{i}} &= s_{i}\frac{dL}{ds_{i}} - s_{i}c = s_{i}(\frac{dL}{ds_{i}} - c)\newline
    \frac{dL}{dz} &= \bigg(\frac{dL}{ds} - c \bigg) \odot s\newline
    &= \bigg( \frac{dL}{ds} - s^{T}\frac{dL}{ds} \bigg) \odot s\end{align}
which involves far less calculations than the original formula involving the Jacobian.

### Multiple Data Points

In the case of multiple data points, $z, s \in \mathbb{R}^{N \times k}$ wherer $N$ is the total number of data points. In this case, we are talking of derivative of matrix over matrix which is a matrix of matrices of shape $N \times k \times N \times k$
\begin{align}
    \frac{ds}{dz} &= \begin{bmatrix}
        \frac{ds_{11}}{dz} &\cdots &\frac{ds_{1k}}{dz}\newline
        \vdots &\ddots &\vdots\newline
        \frac{ds_{N1}}{dz} &\cdots &\frac{ds_{Nk}}{dz}\newline
    \end{bmatrix}\newline
    \frac{ds_{ij}}{dz} &= \begin{bmatrix}
        \frac{ds_{ij}}{dz_{11}} &\cdots &\frac{ds_{ij}}{dz_{1k}}\newline
        \vdots &\ddots &\vdots\newline
        \frac{ds_{ij}}{dz_{k1}} &\cdots &\frac{ds_{ij}}{dz_{nk}}\newline
    \end{bmatrix}\newline
    \frac{ds_{ij}}{dz_{lk}} &= 0 \quad i \neq l\newline
    \frac{ds_{ij}}{dz_{ik}} &= \frac{d}{dz_{ik}} \frac{exp(z_{ij})}{\sum_{l=1}^{k}z_{il}} \quad j \neq k\newline
    &= \frac{(\sum_{l=1}^{k}z_{il})(0) - exp(z_{ij})exp(z_{il})}{\big( (\sum_{l=1}^{k}z_{il})^{2} \big)}
    = -s_{ij}s_{il}\newline
    \frac{ds_{ij}}{dz_{ij}} &= \frac{d}{dz_{ij}} \frac{exp(z_{ij})}{\sum_{l=1}^{k}z_{il}}
    = s_{ij}(1 - s_{ij})\end{align}
For $ds_{ij}/dz$, only the $i^{th}$ row is populated and rest all entries are zeros. Hence, when working with batches of $N$ examples, it is often the case that the complete matrix is reduced to the size $N \times p \times p$ by summing along the third axis or the rows of $ds_{ij}/dz$. This reduces redundancy and removes all the entries of zeros.


Using the Jacobian above is difficult to derive the gradients. We proceed in a manner similar to Vector Jacobian Product to calculate the gradient
\begin{align}
    \frac{dL}{dz} &= \frac{dL}{ds} \frac{ds}{dz}\newline
    \frac{dL}{dz_{ij}} &= \sum_{l=1}^{k} \frac{dL}{ds_{il}} \frac{ds_{il}}{dz_{ij}}\newline
    &= \frac{dL}{ds_{ij}}s_{ij}(1-s_{ij}) - \sum_{l=1, l\neq j}^{k} \frac{dL}{ds_{il}}s_{il}s_{ij} \quad \text{from the single data point derivation}\newline
    &= \frac{dL}{ds_{ij}}s_{ij} - s_{ij}\sum_{l=1}^{k}\frac{dL}{ds_{il}}s_{il}
    = \frac{dL}{ds_{ij}}s_{ij} - s_{ij}\frac{dL}{ds_{i}}s_{i}\newline
    \frac{dL}{dz} &= \bigg( \frac{dL}{ds} - \bigg(\frac{dL}{ds} \odot s \bigg)\boldsymbol{1}\_{k} \bigg) \odot s\end{align}
where $\boldsymbol{1}\_{k}$ is a column vector of all ones. The second part of the equation involves broadcasting, since $s \in \mathbb{R}^{N \times k}$ and $\bigg(\frac{dL}{ds} \odot s \bigg)\boldsymbol{1}\_{k} \in \mathbb{R}^{N \times 1}$.

## ReLU

The defintion of **Rectified Linear Unit** is
\begin{align}
    z = max(0, x)\end{align}
and the derivative becomes
\begin{align}
    \frac{dz}{dx} = \begin{cases}
        0 &\mbox{if $x < 0$}\newline
        1 &\mbox{otherwise}
    \end{cases}\end{align}
Since the operation is element-wise, we can calculate the gradient as,
\begin{align}
    z &= max(0, x)\newline
    \frac{dL}{dx} &= \frac{dL}{dz} \frac{dz}{dx}\newline
    &= \frac{dL}{dz} \odot (x > 0)\newline
    (x > 0)\_{ij} &= \begin{cases}
        0 &\mbox{if $x_{ij} < 0$}\newline
        1 &\mbox{otherwise}
    \end{cases}\end{align}
where $x$ of shape $N \times k$.

## tanh

The defintion of **tanh** is
\begin{align}
    z = tanh(x) = \frac{exp(x) - exp(-x)}{exp(x) + exp(-x)} = \frac{exp(2x) - 1}{exp(2x) - 1}\end{align}
and the derivative becomes
\begin{align}
    \frac{dz}{dz} = \frac{(exp(x) + exp(-x))^{2} - (exp(x) - exp(-x))^{2}}{(exp(x) + exp(-x))^{2}} = 1 - tanh^{2}(x)\end{align}
Since the operation is element-wise, we can calculate the gradient as,
\begin{align}
    z &= tanh(x)\newline
    \frac{dL}{dX} &= \frac{dL}{dz} \odot (1 - tanh^{2}(x)) = \frac{dL}{dz} \odot (1 - z^{2})\end{align}
where $x \in \mathbb{R}^{N \times k}$

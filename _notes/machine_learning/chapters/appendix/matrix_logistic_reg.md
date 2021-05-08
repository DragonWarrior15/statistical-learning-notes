---
title: Matrix Calculus in Logistic Regression
---

## Matrix Calculus used in Logistic Regression Derivation

The equations below present the extended version of the matrix calculus in [Logistic Regression]({{ "/notes/machine_learning/chapters/classification/logistic.html#loss-function" | relative_url }})

Note the derivate of $\beta^{T}x$ which is a scalar. $\beta$ and $x$ are $p+1 \times 1$ vectors
\begin{align}
    \frac{\partial}{\partial \beta}\beta^{T}x =
    \begin{bmatrix}
        \frac{\partial}{\partial \beta_{0}} \sum_{j=0}^{p} \beta_{j}x_{j}\newline
        \frac{\partial}{\partial \beta_{1}} \sum_{j=0}^{p} \beta_{j}x_{j}\newline
        \vdots\newline
        \frac{\partial}{\partial \beta_{p}} \sum_{j=0}^{p} \beta_{j}x_{j}
    \end{bmatrix}
    =
    \begin{bmatrix}
        x_{0}\newline
        x_{1}\newline
        \vdots\newline
        x_{p}
    \end{bmatrix}
    = x
\end{align}

We solve the single derivate first ($y_{i}$ and $p(x_{i}$ are scalars)
\begin{align}
{1}
    \frac{\partial}{\partial \beta}\sum_{i=1}^{n} y\beta^{T}x_{i} + log(1 - exp(\beta^{T}x_{i})) &= \sum_{i=1}^{n} y \frac{\partial}{\partial \beta} y\beta^{T}x_{i} - \frac{exp(\beta^{T}x_{i})}{1 - exp(\beta^{T}x_{i})} \frac{\partial}{\partial \beta} y\beta^{T}x_{i}\newline
    &= \sum_{i=1}^{n} x_{i}(y_{i} - p(x_{i}))\end{align}

To get the second derivative, which is the Hessian matrix, we take derivative with $\beta^{T}$ (to get a matrix)
\begin{align}
    \frac{\partial}{\partial \beta^{T}} \sum_{i=1}^{n} x_{i}(y_{i} - p(x_{i})) =-\frac{\partial}{\partial \beta^{T}} \sum_{i=1}^{n} x_{i}p(x_{i}) \newline\end{align}
First, let's take the derivative of the scalar $p(x_{i})$ with a scalar $\beta_{j}$
\begin{align}
    \frac{\partial}{\partial \beta_{j}} p(x_{i}) &= \frac{\partial}{\partial \beta_{j}} \frac{exp(\beta^{T}x_{i})}{1 + exp(\beta^{T}x_{i})}\newline
    &= \frac{\partial}{\partial \beta^{T}x_{i}} \frac{exp(\beta^{T}x_{i})}{1 + exp(\beta^{T}x_{i})} \frac{\partial}{\partial \beta_{j}} \beta^{T}x_{i} \quad \text{chain rule}\newline
    &= \frac{exp(\beta^{T}x_{i}}{(1 + exp(\beta^{T}x_{i}))^{2}} x_{i,j} \quad \text{from} \frac{\partial}{\partial \beta}\beta^{T}x = x\newline
    &= p(x_{i})(1-p(x_{i}))x_{i,j}\end{align}
Hence, the hessian matrix is
\begin{align}
    \frac{\partial l^{2}}{\partial \beta \partial \beta^{T}} &= -\frac{\partial}{\partial \beta^{T}} \sum_{i=1}^{n} x_{i}p(x_{i})\newline
    &= \sum_{i=1}^{n}
    \begin{bmatrix}
        \frac{\partial}{\partial \beta_{0}} x_{i,0}p(x_{i}) &\frac{\partial}{\partial \beta_{1}} x_{i,0}p(x_{i}) &\ldots &\frac{\partial}{\partial \beta_{p}} x_{i,0}p(x_{i})\newline
        \frac{\partial}{\partial \beta_{0}} x_{i,1}p(x_{i}) &\frac{\partial}{\partial \beta_{1}} x_{i,1}p(x_{i}) &\ldots &\frac{\partial}{\partial \beta_{p}} x_{i,1}p(x_{i})\newline
        \vdots &\vdots &\vdots &\vdots\newline
        \frac{\partial}{\partial \beta_{0}} x_{i,p}p(x_{i}) &\frac{\partial}{\partial \beta_{1}} x_{i,p}p(x_{i}) &\ldots &\frac{\partial}{\partial \beta_{p}} x_{i,p}p(x_{i})
    \end{bmatrix}\newline
    &= \sum_{i=1}^{n} p(x_{i})(1-p(x_{i}))
    \begin{bmatrix}
        x_{i,0}x_{i,0} &x_{i,0}x_{i,1} &\ldots & x_{i,0}x_{i,p}\newline
        x_{i,1}x_{i,0} &x_{i,1}x_{i,1} &\ldots & x_{i,1}x_{i,p}\newline
        \vdots &\vdots &\vdots &\vdots\newline
        x_{i,p}x_{i,0} &x_{i,p}x_{i,1} &\ldots & x_{i,p}x_{i,p}\newline
    \end{bmatrix}\newline
    &= \sum_{i=1}^{n} p(x_{i})(1-p(x_{i})) x_{i}x_{i}^{T}\end{align}

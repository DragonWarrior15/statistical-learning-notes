---
title: "Matrix Calculus"
---

# Matrix Calculus

We review and establish some notation for dealing with gradients beyond just scalars. Any vector below is assumed to be a column vector by default.

### Gradient of a Real valued Function with Vector

Let $f$ be a real valued function and $\boldsymbol{x}$ be a vector
\begin{align}
    f(\boldsymbol{x})&: \mathbb{R}^{n} \rightarrow \mathbb{R}\newline
    \frac{\partial f}{\partial \boldsymbol{x}} &= \bigg(\frac{\partial f(\boldsymbol{x})}{\partial x_{1}}, \frac{\partial f(\boldsymbol{x})}{\partial x_{2}},  \ldots, \frac{\partial f(\boldsymbol{x})}{\partial x_{n}} \bigg)^{T}\end{align}

In texts, usually $\partial f/\partial \boldsymbol{x}$ will be written as a row vector instead of a column vector (above). This is done since all vectors in this text will be column vectors, and the gradients should be the same shape as the original vectors for the update equations to work.

### Gradient of a Vector valued Function with Scalar

Let $\boldsymbol{f}$ be a vector and $y$ be a scalar
\begin{align}
    \boldsymbol{f}(\boldsymbol{x})&: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}\newline
    \frac{\partial \boldsymbol{f}}{\partial y} &= \begin{bmatrix}
    \frac{\partial f_{1}(\boldsymbol{x})}{\partial y}\newline
    \frac{\partial f_{2}(\boldsymbol{x})}{\partial y}\newline
    \vdots\newline
    \frac{\partial f_{m}(\boldsymbol{x})}{\partial y}\newline
    \end{bmatrix}\end{align}

### Gradient of a Vector valued Function with Vector

Let $\boldsymbol{f}$ and $x$ be vectors
\begin{align}
    \boldsymbol{f}(\boldsymbol{x})&: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}\newline
    \frac{\partial \boldsymbol{f}}{\partial \boldsymbol{x}} &= \begin{bmatrix}
        \frac{\partial f_{1}(\boldsymbol{x})}{\partial x_{1}}, &\cdots &\frac{\partial f_{1}(\boldsymbol{x})}{\partial x_{i}} &\cdots &\frac{\partial f_{1}(\boldsymbol{x})}{\partial x_{n}}\newline
        \vdots &\cdots &\vdots &\cdots &\vdots\newline
        \frac{\partial f_{j}(\boldsymbol{x})}{\partial x_{1}}, &\cdots &\frac{\partial f_{j}(\boldsymbol{x})}{\partial x_{i}} &\cdots &\frac{\partial f_{j}(\boldsymbol{x})}{\partial x_{n}}\newline
        \vdots &\cdots &\vdots &\cdots &\vdots\newline
        \frac{\partial f_{m}(\boldsymbol{x})}{\partial x_{1}}, &\cdots &\frac{\partial f_{m}(\boldsymbol{x})}{\partial x_{i}} &\cdots &\frac{\partial f_{m}(\boldsymbol{x})}{\partial x_{n}}\newline
    \end{bmatrix}\newline\end{align}

---
title: "Jacobian"
---

### Jacobian
Obtaining the pdf of a transformed variable (using a one-to-one transformation) is simple using the Jacobian (Jacobian of inverse)
\begin{align}
    Y &= g(X)\newline
    X &= g^{-1}(Y)\newline
    f_{Y}(y) &= f_{X}(g^{-1}(y)) \lvert \frac{dx}{dy} \rvert
\end{align}

The modulus ensures that the probability density is positive when the transformation is either increasing or decreasing.

For the two variable case, let $\mathbf{X} = (X_{1}, X_{2})$ denote the random vector. Suppose we have a one-to-one transform (and its inverse) defined as follows
\begin{align}
    \mathbf{Y} &= T(\mathbf{X})\newline
    \mathbf{Y} &= (Y_{1}, Y_{2})\newline
    Y_{1} &= u_{1}(X_{1}, X_{2})\newline
    Y_{2} &= u_{2}(X_{1}, X_{2})\newline
    T^{-1} &= (w_{1}(Y_{1}, Y_{2}), w_{2}(Y_{1}, Y_{2}))\newline
    X_{1} &= w_{1}(Y_{1}, Y_{2}\newline
    X_{2} &= w_{2}(Y_{1}, Y_{2}
\end{align}

Then, the pdf is given by the expression
\begin{align}
    f_{Y}(y) &= f_{X}(w_{1}(y_{1}, y_{2}), w_{2}(y_{1}, y_{2})) \lvert \mathbf{J} \rvert \newline
    \mathbf{J} &= \begin{vmatrix}
        \frac{\partial x_{1}}{y_{1}} &\frac{\partial x_{1}}{y_{2}}\newline
        \frac{\partial x_{2}}{y_{1}} &\frac{\partial x_{2}}{y_{2}}
    \end{vmatrix}
\end{align}

If $A$ denotes the support of $\mathbf{X}$, then $B = T(A)$ will denote the support of $\mathbf{Y}$. Everywhere else, the value of pdf for $Y$ will be zero. Refer to the exercises section for a demonstration of this method.

This method is powerful and applies to change of variables when doing integrals as well.
\begin{align}
    \int \int f_{X}(x_{1}, x_{2}) dx_{1}dx_{2} = \int \int f_{Y}(w_{1}(y_{1}, y_{2}), w_{2}(y_{1}, y_{2})) \lvert J \rvert dy_{1}dy_{2}
\end{align}
where $J$ is the same as defined earlier.

The two variable expression extends to multiple variables as well. Suppose the transformations are given by
\begin{align}
    Y_{i} &= u_{i}(X_{1}, \ldots X_{n}) \quad \forall i = 1, 2, \ldots, n\newline
    X_{i} &= w_{i}(Y_{1}, \ldots Y_{n}) \quad \forall i = 1, 2, \ldots, n\newline
    \implies f_{\mathbf{Y}}(\mathbf{y}) &= f_{\mathbf{X}}(w_{1}(\mathbf{y}),
    \ldots, w_{n}(\mathbf{y})) \detm{\mathbf{J}}\newline
    \text{with}\quad \mathbf{J} &= \begin{vmatrix}
        \frac{\partial x_{1}}{\partial y_{1}} &\cdots &\frac{\partial x_{1}}{\partial y_{n}}\newline
        \vdots &\ddots &\vdots\newline
        \frac{\partial x_{n}}{\partial y_{1}} &\cdots &\frac{\partial x_{n}}{\partial y_{n}}\newline
    \end{vmatrix}
\end{align}

However, we may not be always have a one-to-one transformation. The simplest case is $Y = X^{2}$. In such scenarios, we will partition the space so that each has a one-to-one transform.

For instance, in the above example the partitions will be $-\infty < x < 0$ and $0 \leq x < \infty$. Then, we individually calculate the pdf for $Y$ in all the partitions. If the partitions have an overlap (from the view of support of $y$), we will sum up the corresponding pmf to get the final pmf.

Continuing with the same example, both the partitions map to $0 <\leq y < \infty$. Hence, after finding the pmf in each partition, we can simply sum it up (due to symmetry of the transform). Refer to the exercises for an illustration of this principle.

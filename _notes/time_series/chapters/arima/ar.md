---
title: "Autoregressive Model (AR)"
---

# Autoregressive Model (AR)

As the name suggests, we use linear combinations of values at some of the previous instants to get the value at current time step for a **stationary series**
\begin{align}
    X_{t} = \phi_{1}X_{t-1} + \phi_{2}X_{t-2} + \cdots + \phi_{p}X_{t-p} + W_{t}, \quad \phi_{p} \neq 0\end{align}
is known as **Autoregressive Process AR(p) of order p** since we are using lagged variables till $p$ steps. $w_{t}$ is the white noise with unknown variance. Note that the **time series** used for this equation **must have mean 0**. If that is not the case, the series must be transformed to subtract the mean from all terms (the mean is constant since the series is stationary).


For **stationarity** in an order 2 process, the following inequalities must be satisfied by the coefficients
\begin{align}
    -1 &< \phi_{2} < 1\newline
    \phi_{2} &< 1 + \phi_{1}\newline
    \phi_{2} &< 1 - \phi_{1}\end{align}
where $\phi_{1}$ and $\phi_{2}$ can be positive or negative. More complicated set of rules exist for higher order processes.


This equation is conveniently expressesed using the backshift operator
\begin{align}
    X_{t} &= \phi_{1}BX_{t} + \phi_{2}B^{2}X_{t-2} + \cdots + \phi_{p}B^{p}X_{t} + W_{t}\newline
    &= X_{t}(\phi_{1}B + \phi_{2}B^{2} + \cdots + \phi_{p}B^{p}) + W_{t}\newline
    \text{or,} \; W_{t} &= (1 - \phi_{1}B - \phi_{2}B^{2} - \cdots - \phi_{p}B^{p})X_{t}\newline
    W_{t} &= \phi(B)X_{t}\newline\end{align}
where the **autoregressive operator** $\boldsymbol{\phi(B)}$ is defined as
\begin{align}
    \phi(B) = 1 - \phi_{1}B - \phi_{2}B^{2} - \cdots - \phi_{p}B^{p}\end{align}
Properties of this function are crucial to solve for $X_{t}$.

## AR(1) Model

The AR(1) process can be rewritten as an infinite sum
\begin{align}
    X_{t} &= \phi_{1}X_{t-1} + W_{t}\newline
    &= \phi_{1}(\phi_{1}X_{t-2} + W_{t-1}) + W_{t}\newline
    &= \phi_{1}^{k}X_{t-k} + \sum_{i=0}^{k-1}\phi^{k}W_{t-i}\newline
    &= \sum_{i=0}^{\infty}\phi_{1}^{i}W_{t-i} \numberthiseqn\label{eq:ar_1}\end{align}
If $\lvert \phi_{1} \rvert < 1$, the right hand side series will converge in the mean square sence and vice versa.

### Convergence in Mean Square Sense

A random process $X_{n}$ is said to converge to random variable $X$ in the mean square sense if
\begin{align}
    \lim_{n \to \infty} E[(X_{n} - X)^{2}] = 0\end{align}

In the context of AR(1), this definition is needed since the expectation of both sides of equation [\[eq:ar_1\]](#eq:ar_1){reference-type="eqref" reference="eq:ar_1"} is already the same value of 0.
\begin{align}
    \lim_{k \to \infty} E[(X_{t} - \sum_{j=0}^{k-1}\phi_{1}^{i}W_{t-i})^{2}] = \lim_{k \to \infty} E[(\phi^{k} X_{t-k})^{2}] = 0\end{align}
if $\lvert \phi_{1} \rvert < 1$. This convergence also makes the equaton **causal**, since the value at any time step is only dependent on the value at previous time steps.


## Causality

The condition for **causality** in an AR process
\begin{align}
    W_{t} &= \phi(B)X_{t}\newline
    X_{t} &= \frac{1}{\phi(B)}W_{t} = \psi(B)W_{t} = \sum_{i=0}^{\infty}\psi_{i}W_{t-i}\newline
    \frac{1}{\phi(z)} &= \psi(z) = \sum_{i=0}^{\infty}\psi_{i}z^{i} \; \forall \; \lvert z \rvert \leq 1\newline
    \implies \phi(z) &\neq 0 \; \forall \; \lvert z \rvert \leq 1\end{align}
or equivalently, **roots of the polynomial** $\boldsymbol{\phi(z)}$ **all lie outside the unit circle for causality of an AR process**.


Consider the case of $\lvert \phi_{1} \rvert \geq 1$. Here, we can write $X_{t}$ in terms of the future terms to get convergence
\begin{align}
    X_{t+1} &= \phi_{1}X_{t} + W_{t}\newline
    X_{t} &= \phi_{1}^{-1}X_{t+1} + \phi_{1}^{-1}W_{t}\newline
    &= \phi_{1}^{-1}(\phi_{1}^{-1}X_{t+2} + \phi_{1}^{-1}W_{t+1}) + \phi_{1}^{-1}W_{t}\newline
    &= \phi_{1}^{-k}X_{t+k} + \sum_{i=0}^{k-1}\phi_{1}^{-(i+1)}W_{t+i}\newline
    &= \sum_{i=0}^{\infty}\phi_{1}^{-(i+1)}W_{t+i}\end{align}
which although stationary ($\lvert \phi_{1}^{-1} \rvert < 1$), is not causal (but explosive) since it requires knowledge of the future, and thus of not much use.


The autocovariance of AR(1) is given by
\begin{align}
    Cov(X_{t}, X_{t+h}) &= E \bigg[\bigg(\sum_{i=0}^{\infty}\phi_{1}^{i}W_{t-i} \bigg) \bigg(\sum_{j=0}^{\infty}\phi_{1}^{j}W_{t+h-j} \bigg) \bigg]\newline
    &= E[\sum_{i=0}^{\infty}\phi_{1}^{i}W_{t-i} \phi_{1}^{h+i}W_{t-i}] \quad \text{put $t-i = t+h-j$}\newline
    &= \sigma_{w}^{2} \sum_{i=0}^{\infty}\phi_{1}^{2i+h}\newline
    &= \frac{\sigma_{w}^{2} \phi_{1}^{h}}{1-\phi_{1}^{2}} \quad h \geq 0\end{align}
which is only dependent on the lag. Also, $\gamma(h) = \gamma(-h)$. The ACF becomes
\begin{align}
    \rho(h) &= \gamma(h)/\gamma(0) = \phi_{1}^{h}\newline
     &= \phi_{1}\rho(h-1)\end{align}

For larger orders $> 1$, obtaining equations of format shown [here](#Convergence-in-Mean-Square-Sense) is difficult. The same form could be achieved by comparing the coefficients. We will rewrite this equation as
\begin{align}
    X_{t} &= \sum_{i=0}^{\infty}\psi_{j}W_{t-i}\end{align}
where $\psi_{j} = \phi_{1}^{j}$ is the solution for AR(1). A more general method to solve for the coefficients is given through **Yule-Walker equations**.

## Yule-Walker Equations

### Calculating $\rho$ when coefficients are known

These equations provide an algebraic tool to solve for ACF of any AR(p) process. The equations have a prior assumption that the time series is stationary. They are solved as

1.  The AR(p) process is written as
    \begin{align}
            X_{t} = \phi_{1}X_{t-1} + \phi_{2}X_{t-2} + \cdots + \phi_{p}X_{t-p} + Z_{t}
        \end{align}

2.  Taking expectations both sides should result in the value of the mean (constant since the series is stationary)
    \begin{align}
            \mu = (\phi_{1} + \phi_{2} + \cdots + \phi_{p})\mu + E[Z_{t}]
        \end{align}
    $Z$ is usually a standard normal variable.

3.  We multiply by $X_{t-k}$ on both sides and again take expectation (assume no correlation between $X_{t-k}$ and $Z_{t}$)
    \begin{align}
            E[X_{t-k}X_{t}] &= \phi_{1}E[X_{t-k}X_{t-1}] + \phi_{2}E[X_{t-k}X_{t-2}] + \cdots + \phi_{p}E[X_{t-k}X_{t-p}] + E[X_{t-k}Z_{t}]\newline
            \gamma(-k) &= \phi_{1}\gamma(1-k) + \cdots + \phi_{p}\gamma(p-k)\newline
            \gamma(k) &= \phi_{1}\gamma(k-1) + \cdots + \phi_{p}\gamma(k-p) \; (\text{since $\gamma(k) = \gamma(-k)$ \; $\forall k=1,2,\ldots$})\newline
            \rho(k) &= \phi_{1}\rho(k-1) + \cdots + \phi_{p}\rho(k-p) \; (\text{dividing by $\gamma(0)$})
        \end{align}

4.  We look for a solution of the form $\rho(k) = \lambda^{k}$. The equation thus obtained is called a **characteristic equation** and is a common solution to equations where any terms is a linear combination of a few previous terms
    \begin{align}
            \lambda^{k} = \phi_{1}\lambda^{k-1} + \phi_{2}\lambda^{k-2} + \cdots + \phi_{p}\lambda^{k-p}
        \end{align}
    which can be solved to get the roots of a polynomial (roots can be both real and complex). For invertibility, the roots must lie outside the unit circle in the complex plane.

5.  After solving for $\lambda$, the roots are $\lambda_{1}, \ldots, \lambda_{k}$. Then,
    \begin{align}
            \rho(k) = c_{1}\lambda_{1} + \cdots + c_{k}\lambda_{k}
        \end{align}
    since any linear combination of the roots is also a solution to the eqution. We can solve for the coefficients using
    \begin{align}
            \rho(0) &= 1\newline
            \rho(k) &= \rho(-k) \; \forall k=1,2,\ldots
        \end{align}

### Obtaining Coefficients Using Sample Estimates of ACF

Now suppose we want to obtain the coefficients for the AR process. We use the Yule-Walker equations in reverse. $\rho$ can be estimated using the known values of the series. Consider the Yule-Walker equations for different values of $k$
\begin{align}
{3}
    \rho(k) &= \phi_{1}\rho(k-1) &+ \cdots &+ \phi_{p}\rho(k-p)\newline
    \rho(1) &= \phi_{1}\rho(0) &+ \cdots &+ \phi_{p}\rho(1-p)\newline
    \rho(2) &= \phi_{1}\rho(2-1) &+ \cdots &+ \phi_{p}\rho(2-p)\newline
    &\vdots\newline
    \rho(p) &= \phi_{1}\rho(p-1) &+ \cdots &+ \phi_{p}\rho(0)\newline\end{align}
We can substitute $\rho(k) = \rho(-k)$ and obtain a matrix form of the equations
\begin{align}
    \begin{bmatrix}
        \rho(1)\newline
        \rho(2)\newline
        \vdots\newline
        \rho(p)
    \end{bmatrix}
    =
    \begin{bmatrix}
        \rho_{0} &\rho_{1} &\cdots &\rho_{p-1}\newline
        \rho_{1} &\rho_{0} &\cdots &\rho_{p-2}\newline
        \vdots &\vdots &\vdots &\vdots\newline
        \rho_{p-1} &\rho_{p-2} &\cdots &\rho_{0}
    \end{bmatrix}
    \begin{bmatrix}
        \phi(1)\newline
        \phi(2)\newline
        \vdots\newline
        \phi(p)
    \end{bmatrix}\end{align}
Replacing $\rho$ with sample estimates $\hat{\rho}$
\begin{align}
    \begin{bmatrix}
        \phi(1)\newline
        \phi(2)\newline
        \vdots\newline
        \phi(p)
    \end{bmatrix}
    =
    \begin{bmatrix}
        \hat{\rho}\_{0} &\hat{\rho}\_{1} &\cdots &\hat{\rho}\_{p-1}\newline
        \hat{\rho}\_{1} &\hat{\rho}\_{0} &\cdots &\hat{\rho}\_{p-2}\newline
        \vdots &\vdots &\vdots &\vdots\newline
        \hat{\rho}\_{p-1} &\hat{\rho}\_{p-2} &\cdots &\hat{\rho}\_{0}
    \end{bmatrix}^{-1}
    \begin{bmatrix}
        \hat{\rho}(1)\newline
        \hat{\rho}(2)\newline
        \vdots\newline
        \hat{\rho}(p)
    \end{bmatrix}\end{align}
which can be solved to get the coefficients of a **stationary** AR(p) process. There will be a unique solution since these matrices are nothing but autocovariance matrix and similar to the covariance matrix of a random variable, these are alo positive semidefinite $rightarrow$ inverse exists.


We can extend this idea to estimate the variance of noise
\begin{align}
    X_{t} &= \phi_{1}X_{t-1} + \phi_{2}X_{t-2} + \cdots + \phi_{p}X_{t-p} + Z_{t}\newline
    Var(X_{t}) &= \sum_{k=1}^{p}\phi_{k}^{2}Var(X_{t-k}) + 2\sum_{i=1}^{p-1}\sum_{j=i+1}^{p} \phi_{i}\phi_{j}Cov(X_{i}X_{j}) + Var(Z_{t})\newline\end{align}
where we have removed the interaction terms of noise and $X_{k}$ since they are independent. Since the variance of a time series is constant ($\gamma(0)$) and we have the estimates $\hat{gamma}$ for all lags,
\begin{align}
    \hat{\sigma}^{2} = \hat{\gamma}(0)\bigg(1 - \sum_{k=1}^{p}\phi_{k}^{2} - 2\sum_{i=1}^{p-1}\sum_{j=i+1}^{p} \phi_{i}\phi_{j}\hat{\rho}(j - i)\bigg)\end{align}
giving the sample estimate of the variance of white noise.

---
title: "ARMA(p,q) Process"
---

# ARMA(p,q) Process

This is a combination of AR and MA parts. The AR has order $p$ and MA has order $q$
\begin{align}
    X_{t} = \phi_{1}X_{t-1} + \cdots + \phi_{p}X_{t-p} + W_{t} + \beta_{1}W_{t-1} + \cdots \beta_{q}W_{t-q}\end{align}
where $X_{t}$ is stationary, $\phi_{p}, \beta_{q} \neq 0$ and $\sigma_{w}^{2} > 0$. By the above definition, $E[X_{t}] = 0$, and if that is not the case, we subtract the constant mean from throughout the series. The series can be rewritten as
\begin{align}
    X_{t}- \phi_{1}X_{t-1} - \cdots - \phi_{p}X_{t-p} &= W_{t} + \beta_{1}W_{t-1} + \cdots \beta_{q}W_{t-q}\newline
    (1 - \phi_{1}B - \cdots - \phi_{p}B^{p})X_{t} &= (1 + \beta_{1}B + \cdots +\beta_{q}B^{q})W_{t}\newline
    \phi(B)X_{t} &= \beta(B)W_{t}\end{align}
We can complicate the last equation by arbitrarily multiplying both sides by a new polynomial
\begin{align}
    \eta(B)\phi(B)X_{t} &= \eta(B)\beta(B)W_{t}\newline
    X_{t} &= W_{t}\newline
    (1-B)X_{t} &= (1-B)W_{t}\newline
    X_{t} &= X_{t-1} + W_{t} - W_{t-1}\end{align}
which makes the original white noise process into an ARMA(1,1) process. This refers to **overparametrization** of the model and we would want to use the least complex model in our analysis. If we conclude the process to be ARMA, we are inducing non-existent correlation between terms at successive time steps, although a visual inspection of the time series might refute this observation.


Based on our observations in AR and MA processes, we must modify the ARMA process to solve the following problems

1.  Overparametrization of ARMA

2.  Stationarity in AR by looking at future terms

3.  Non uniqueness of MA

The first problem is solved by imposing the constraint that **MA and AR polynomials do not have any common factors** and are reduced to their simplest forms. The polynomials being referred to are the functions of backshift operator $B$ in $\phi(B)X_{t} = \beta(B)W_{t}$ (we can treat $B$ as a complex number for the purpose of strict mathematical solving).


For the second point, we define $X_{t}$ to be **causal** if $X_{t}$ can be rewritten as
$$\begin{gathered}
    X_{t} = \sum_{i=0}^{\infty} \psi_{i} W_{t-i}\newline
    \psi_{0} = 1 \quad \sum_{i=0}^{\infty} \lvert \psi_{i} \rvert < \infty \quad \psi(B) = \sum_{i=0}^{\infty} \psi_{i}B^{i}\end{gathered}$$
Here $X_{t}$ is only dependent on the past terms and not the future ones. Comparing with $\phi(B)X_{t} = \beta(B)W_{t}$ and using complex number $z$ instead of $B$
\begin{align}
    \psi(z) = \frac{\beta(z)}{\phi(z)} \quad \lvert z \rvert \leq 1\end{align}
to solve for the coefficients of $\psi(z)$. Clearly $\lvert z \rvert \leq 1$ so that the sums do not diverge. This implies that
\begin{align}
    \phi(z) \neq 0 \quad \forall \; \lvert z \rvert \leq 1\end{align}
which in turn means that **roots of** $\boldsymbol{\phi(z)}$ **lie outside the unit circle for causality of ARMA process**.


To address the third problem of uniqueness of ARMA, we introduce the notion of invertibility as in AR processes. To have invertibility, we must be able to express $W_{t}$ as a function of $X_{t}$ and older time steps in a convergent manner.
\begin{align}
    \phi(B)X_{t} &= \beta(B)W_{t}\newline
    W_{t} &= \frac{\phi(B)}{\beta(B)}X_{t}\newline
    &= \pi(B)X_{t}\newline
    \implies W_{t} &= \sum_{i=0}^{\infty} \pi_{i}X_{t-i}\newline
    \pi_{0} = 1 \quad \sum_{i=0}^{\infty} \lvert \pi_{i} \rvert &< \infty \quad \pi(B) = \sum_{i=0}^{\infty} \pi_{i}B^{i}\end{align}
where we can find the coefficients of $\pi(B)$ by comparing both the sides. For convergence, the conditions are similar as the causality conditions
\begin{align}
    \pi(z) = \frac{\phi(z)}{\beta(z)}\newline
    \implies \lvert z \rvert \leq 1\newline
    \implies \text{roots of $\beta(z)$ lie outside the unit circle}\end{align}
Hence, **for invertibility, the roots of polynomial** $\boldsymbol{\beta(z)}$**lie outside the unit circle**.


### Overparametrization, Causality and Invertibility

In summary,

1.  Overparametrization of ARMA

    This is solved by imposing the condition that the MA and AR polynomials are reduced to their lowest forms by removing common factors

2.  Stationarity in AR by looking at future terms

    This is solved by imposing the condition that the roots of the AR polynomial lie outside the unit circle

3.  Non uniqueness of MA

    This is solved by imposing the condition that the roots of the MA polynomial lie outside the unit circle

## Using the ACF and PACF plots

| Plot | **AR(p)** | **MA(q)** | **ARMA(p,q)** |
| ==== | ========= | ========= | ============= |
| **ACF** | Tails off | Cuts off after lag $q$ | Tails off |
**PACF** | Cuts off after lag $p$ | Tails off | Tails off |

---
title: "Moving Average Process (MA)"
---

# Moving Average Process (MA)

A moving average process will use a weighted sum the past noises and a constant to calculate the current value of the time series. Mathematically
\begin{align}
    X_{t} = W_{t} + \beta_{1}W_{t-1} + \beta_{2}W_{t-2} + \cdots + \beta_{q}W_{t-q} \quad \beta_{q} \neq 0\end{align}
is a moving average process of **order q** or **MA(q)** for the stationary process $X_{t}$. **MA(q) process is stationary for any values of the coefficients**. This can be proven by observing the following
\begin{align}
    E[X_{t}] &= E[W_{t}] + \beta_{1}E[W_{t-1}] + \beta_{2}E[W_{t-2}] + \cdots + \beta_{q}E[W_{t-q}] = 0\newline
    Cov(X_{t}, X_{t+h}) &= E[(\sum_{i=0}^{q} beta_{i}W_{t-i}) (\sum_{i=0}^{q} beta_{i}W_{t+h-i})]\newline
    &= \begin{cases} \sum_{i=0}^{q-h} \beta_{i}\beta_{i+h} &\mbox{$h \leq q$}\newline 0 &\mbox{otherwise} \end{cases}\end{align}
where $\beta_{0} = 1$. This implies that the covariance is only dependent on lag. Hence, MA(q) process is always stataionary.


Consequently, ACF for MA(q) is only dependent on the lag, and after lag is greater than $q$, the ACF is always 0. Thus, **if we observe the ACF of MA(q), it will cut off after lag q**. If it is known that the time series is indeed a moving average one, we can infer the value of $q$ from the point in ACF plot where the lag starts to become close to 0.


A more convenient form is
\begin{align}
    X_{t} &= W_{t}(1 + \beta_{1}BW_{t} + \beta_{2}B^{2}W_{t} + \cdots + \beta_{q}B^{q}W_{t})\newline
    &= \beta(B)W_{t}\newline
    \beta(B) &= 1 + \beta_{1}B + \beta_{2}B^{2} + \cdots + \beta_{q}B^{q}\end{align}
where $\beta(B)$ is a polynomial and is also called the **moving average operator**.

## MA(1) Model

This model is only dependent on the noise from current and previous step
\begin{align}
    X_{t} &= W_{t} + \beta_{1}W_{t-1}\newline
    E[X_{t}] &= 0\newline
    \gamma(h) &= E[X_{t}, X_{t+h}] = E[(W_{t} + \beta_{1}W_{t-1})(W_{t+h} + \beta_{1}W_{t+h-1})]\newline
    &= \begin{cases}
        \sigma_{w}^{2}(1 + \beta_{1}^{2}) &\mbox{$h = 0$}\newline
        \sigma_{w}^{2}\beta_{1} &\mbox{$h \pm 1$}\newline
        0 &\mbox{otherwise}
    \end{cases}\newline
    \rho(h) &= \begin{cases} \frac{\beta_{1}}{1+\beta_{1}^{2}} &\mbox{$h = 1$}\newline 0 &\mbox{otherwise} \end{cases}\end{align}
By symmetry, $\gamma(h) = \gamma(-h)$ and $\rho(h) = \rho(-h)$. By limit theorem, $\lim_{\beta_{1} \to \infty} \rho(1) = 1/2$. Notice that in MA(1) process, the relation only extends till lag 1. This is different from AR(1) process, where the relation could extend till infinite terms.

## Non-Uniqueness and Invertibility

For the same variance of noise, the MA(1) process with $\beta_{1}$ and $1/\beta_{1}$ coefficients have the same value of $\rho$. Making the value of $\gamma$ same requires manipulating the noise as well. The following two processes have the same $\gamma$ as well
\begin{align}
{2}
    X_{t} &= W_{t} + \beta_{1}W_{t-1} \quad &W \sim \mathcal{N}(0,\sigma_{w}^{2})\newline
    X_{t} &= W_{t} + \frac{1}{\beta_{1}}W_{t-1} \quad &W \sim \mathcal{N}(0,\beta_{1}^{2}\sigma_{w}^{2}) \numberthiseqn\label{eq:ma_1}\newline\end{align}

Since we only observe $X_{t}$, both of the above representations are valid solutions in determining the equation of the process. To make the equation unique, we need to consider infinite sums similar to what was done in the AR process.


Consider expressing $W_{t}$ in terms of $X_{t}$ and other terms
\begin{align}
    X_{t} &= (1 + \beta_{1}B)W_{t}\newline
    W_{t} &= (1 + \beta_{1}B)^{-1}X_{t}\newline
    &= (1 - \beta_{1}B + \beta_{1}^{2}B^{2} - \cdots)X_{t}\newline
    &= X_{t} - \beta_{1}X_{t-1} + \beta_{1}^{2}X_{t-2} - \cdots\end{align}
which is an AR($\infty$) process. Clearly, the model is stable/convergent only when $\lvert \beta_{1} \rvert < 1$. In this case, we will choose the second representation of $X_{t}$ as $X_{t} &= W_{t} + \frac{1}{\beta_{1}}W_{t-1} \quad &W \sim \mathcal{N}(0,\beta_{1}^{2}\sigma_{w}^{2})$, as it is **invertible** (we can invert from one representation to another).

\begin{align}
    X_{t} &= \beta(B)W_{t}\newline
    W_{t} &= \frac{1}{\beta(B)}X_{t} = \pi(B)X_{t} = \sum_{i=0}^{\infty} \pi_{i}X_{t-i}\newline
     \frac{1}{\beta(z)} &= \pi(z) = \sum_{i=0}^{\infty} \pi_{i}z^{i} \; \forall \; \lvert z \rvert \leq 1 \; \text{for finite sums}\newline
     \implies \beta(z) &\neq 0 \; \forall \; \lvert z \rvert \leq 1\end{align}
which differently stated means that the **roots of the polynomial** $\boldsymbol{\beta(z)}$ **lie outside the unit circle**.

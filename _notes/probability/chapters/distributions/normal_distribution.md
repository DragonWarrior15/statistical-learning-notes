---
title: "Normal Distribution"
---

## Normal Distribution

The Normal distribution (or gaussian distribution) is defined between $-\infty$ and $\infty$. It is parametrized by mean $\mu$ and variance $\sigma$, $X \sim \mathcal{N}(\mu, \sigma^{2})$
\begin{align}
        f_{X}(x) = \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}
    \end{align}
As already described,
\begin{align}
        E[X] &= \mu\newline
        Var(X) &= \sigma^{2}
    \end{align}

### Standard Normal Distribution

A *Standard Normal* is defined as a normal distribution with $\mu = 0$ and $\sigma^{2} = 1$
Any normal distribution can be converted to a standard normal as $X = \frac{X - \mu}{\sigma}$
If $Y = aX + b$, then $Y \sim \mathcal{N}(a \mu + b, a^{2}\sigma^{2})$.


For a standard normal variable $Z$, it is standard to denote
\begin{align}
        P(Z \leq z) = \Phi(z) \quad P(Z = z) = \phi(z) = \mathcal{N}(0,1)
    \end{align}

Further, for a given $\alpha \in (0,1)$, define $z_{\alpha}$ by
\begin{align}
        P(Z > z_{\alpha}) = \alpha = 1-\Phi(z_{\alpha})
    \end{align}
Some standard values of $\alpha$ can be useful

-   $z_{0.01} = 1.2816$

-   $z_{0.05} = 1.645$

-   $z_{0.025} = 1.96$

-   $z_{0.01} = 2.33$

The 68–95–99.7 rule is also useful which states that
* Probability of $X$ lying between 1 standard deviation on either side of mean is 68%
* Probability of $X$ lying between 2 standard deviation on either side of mean is 95%
* Probability of $X$ lying between 3 standard deviation on either side of mean is 99.7%

### Moment Generating Function

\begin{align}
        E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}
    \end{align}
We will rearrange the terms to form a perfect square in the exponent part with a changed mean.
\begin{align}
        E[e^{tX}] &= \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\newline
        &= \int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi \sigma^{2}}}\exp \bigg( -\frac{(x-(\mu+\sigma^{2}t))^{2} - (\mu+\sigma^{2}t)^{2} + \mu^{2}}{2 \sigma^{2}} \bigg)\newline
        &= \int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi \sigma^{2}}} \exp \bigg(-\frac{(x-(\mu+\sigma^{2}t)^{2}}{2 \sigma^{2}} \bigg) \exp \bigg(\mu t + \frac{\sigma^{2} t^{2}}{2} \bigg)\newline
        E[e^{tX}] &= \exp \bigg(\mu t + \frac{\sigma^{2} t^{2}}{2}\bigg)
    \end{align}
Since the total integral of a normal distribution is 1 (the total probability).

### Sum of Normal Distributions

With the help of moment generating functions, this calculation becomes easier. Let $X_{1}, \ldots X_{n}$ be $n$ independent normal distributions with $X_{i} \sim \mathcal{N}(\mu_{i}, \sigma^{2}\_{i})$.
\begin{align}
        E[e^{t(X_{1} + X_{2} + \cdots + X_{n})}] &= \prod_{i=1}^{n} E[e^{tX_{i}}] = \prod_{i=1}^{n} e^{\mu_{i} t + \frac{\sigma_{i}^{2} t^{2}}{2}}\newline
        &= \exp(\sum_{i=1}^{n} \mu_{i} t+ \sum_{i=1}^{n}\sigma^{2} \frac{t^{2}}{2})\newline
        \implies X_{1} + X_{2} + \cdots + X_{n} &\sim \mathcal{N}(\mu_{1} + \cdots + \mu_{2}, \sigma_{1}^{2} + \cdots + \sigma_{2}^{2})
    \end{align}

### Multivariate Normal Distribution

Multivariate normal distribution is an extension of a normal distribution into multiple dimensions
\begin{align}
        f_{\mathbf{X}}(\boldsymbol{x}) = \frac{1}{\sqrt{(2\pi)^{d} \lvert \Sigma \rvert}} exp(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})\Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})^{T})
    \end{align}
for $d$ dimensional vector $\mathbf{x}$ with mean vector $\boldsymbol{\mu}$ and covriance matrix $\Sigma$.

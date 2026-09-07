# Normal Distribution

<!-- Math Macros: This block defines reusable commands but stays invisible on GitHub -->
$$
\newcommand{\detm}[1]{\left \lvert #1 \right \rvert}
\newcommand{\roundbr}[1]{\left( #1 \right)}
\newcommand{\squarebr}[1]{\left[ #1 \right]}
$$

## Normal Distribution

The Normal distribution (or gaussian distribution) is defined between $-\infty$ and $\infty$. It is parametrized by mean $\mu$ and variance $\sigma$, $X \sim \mathcal{N}(\mu, \sigma^{2})$

$$
\begin{aligned}
    f_{X}(x) = \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}
\end{aligned}
$$

As already described,

$$
\begin{aligned}
    E[X] &= \mu\newline
    Var(X) &= \sigma^{2}
\end{aligned}
$$

### Standard Normal Distribution

A *Standard Normal* is defined as a normal distribution with $\mu = 0$ and $\sigma^{2} = 1$
Any normal distribution can be converted to a standard normal as $X = \frac{X - \mu}{\sigma}$
If $Y = aX + b$, then $Y \sim \mathcal{N}(a \mu + b, a^{2}\sigma^{2})$.


For a standard normal variable $Z$, it is standard to denote

$$
\begin{aligned}
    P(Z \leq z) &= \Phi(z)\newline P(Z = z) &= \phi(z) = \mathcal{N}(0,1)
\end{aligned}
$$

Further, for a given $\alpha \in (0,1)$, define $z_{\alpha}$ by
$$
\begin{aligned}
    P(Z > z_{\alpha}) = \alpha = 1-\Phi(z_{\alpha})
\end{aligned}
$$
Some standard values of $\alpha$ can be useful

- $z_{0.01} = 1.2816$
- $z_{0.05} = 1.645$
- $z_{0.025} = 1.96$
- $z_{0.01} = 2.33$

The 68–95–99.7 rule is also useful which states that
* Probability of $X$ lying between 1 standard deviation on either side of mean is 68%
* Probability of $X$ lying between 2 standard deviation on either side of mean is 95%
* Probability of $X$ lying between 3 standard deviation on either side of mean is 99.7%

It is often easier to derive all formulae here by first considering the standard normal and defining it completely. Then any normal distribution with mean $\mu$ and variance $\sigma^{2}$ can be obtained using the transformation $Y = \sigma Z + \mu$. All calculations for mean, variance and mgf readily follow.

### Moment Generating Function

$$
\begin{aligned}
    E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}
\end{aligned}
$$

We will rearrange the terms to form a perfect square in the exponent part with a changed mean.

$$
\begin{aligned}
    E[e^{tX}] &= \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\newline
    &= \int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi \sigma^{2}}}\exp \bigg( -\frac{(x-(\mu+\sigma^{2}t))^{2} - (\mu+\sigma^{2}t)^{2} + \mu^{2}}{2 \sigma^{2}} \bigg)\newline
    &= \int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi \sigma^{2}}} \exp \bigg(-\frac{(x-(\mu+\sigma^{2}t)^{2}}{2 \sigma^{2}} \bigg) \exp \bigg(\mu t + \frac{\sigma^{2} t^{2}}{2} \bigg)\newline
    E[e^{tX}] &= \exp \bigg(\mu t + \frac{\sigma^{2} t^{2}}{2}\bigg)
\end{aligned}
$$

Since the total integral of a normal distribution is 1 (the total probability).

### Sum of Normal Distributions

With the help of moment generating functions, this calculation becomes easier. Let $X_{1}, \ldots X_{n}$ be $n$ independent normal distributions with $X_{i} \sim \mathcal{N}(\mu_{i}, \sigma^{2}_{i})$.

$$
\begin{aligned}
    E[e^{t(X_{1} + X_{2} + \cdots + X_{n})}] &= \prod_{i=1}^{n} E[e^{tX_{i}}] = \prod_{i=1}^{n} e^{\mu_{i} t + \frac{\sigma_{i}^{2} t^{2}}{2}}\newline
    &= \exp(\sum_{i=1}^{n} \mu_{i} t+ \sum_{i=1}^{n}\sigma^{2} \frac{t^{2}}{2})\newline
    \implies X_{1} + X_{2} + \cdots + X_{n} &\sim \mathcal{N}(\mu_{1} + \cdots + \mu_{2}, \sigma_{1}^{2} + \cdots + \sigma_{2}^{2})
\end{aligned}
$$

### Multivariate Normal Distribution

Multivariate normal distribution is an extension of a normal distribution into multiple dimensions

$$
\begin{aligned}
    f_{\mathbf{X}}(\boldsymbol{x}) = \frac{1}{\sqrt{(2\pi)^{d} \detm{\Sigma}}} exp(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})\Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})^{T})
\end{aligned}
$$

for $d$ dimensional vector $\mathbf{x}$ with mean vector $\boldsymbol{\mu}$ and covriance matrix $\Sigma$.

This is easy to derive if we start from a standard normal first.

Consider $n$ independent identically distributed standard normals $Z_{i} \sim N(0, 1)$. The joint distribution is

$$
\begin{aligned}
    f_{\mathbf{Z}}(\mathbf{z}) &= \prod_{i=1}^{n}f_{Z_{i}}(z_{i}) = \roundbr{\frac{1}{\sqrt{2\pi}}}^{n}\exp\roundbr{-\frac{1}{2}\sum_{i=1}^{n}z_{i}^{2}}\newline
    &= \roundbr{\frac{1}{2\pi}}^{\frac{n}{2}}\exp\roundbr{-\frac{1}{2}\mathbf{z}^{T}\mathbf{z}}
\end{aligned}
$$

$E[\mathbf{Z}] = 0 = E[\mathbf{Z}]^{T} $ (element wise).

$$
\begin{aligned}
    Cov(\mathbf{Z}, \mathbf{Z}) &= E[\mathbf{Z}\mathbf{Z}^{T}] - E[\mathbf{Z}]E[\mathbf{Z}]^{T}\newline
    &= \mathbf{I}_{n}\newline
    \text{as} \quad E[\mathbf{Z}\mathbf{Z}^{T}]_{ij} &= Cov(Z_{i}, Z_{j}) = 0 \quad \text{independence}\newline
    E[\mathbf{Z}\mathbf{Z}^{T}]_{ii} &= Cov(Z_{i}, Z_{i}) = Var(Z_{i}) = 1 \quad \text{independence}
\end{aligned}
$$

The mgf

$$
\begin{aligned}
    M(\mathbf{t}) &= E\squarebr{e^{\mathbf{t}^{T}\mathbf{Z}}} = \exp\roundbr{\frac{1}{2}\mathbf{t}^{T}\mathbf{t}}
\end{aligned}
$$

by independence.

Now, assume a real symmetric semipositive definite matrix $\Sigma$ that represents a variance-covariance matrix. From spectral decomposition, there exists $\Sigma^{1/2}$ such that $\Sigma^{1/2} \Sigma^{1/2} = \Sigma$ (from linear algebra). Also, this matrix is itself symmetric.

Assume a constant vector $\mathbf{\mu}$. Then,

$$
\begin{aligned}
    \mathbf{X} &= \Sigma^{1/2}\mathbf{Z} + \mathbf{\mu}\newline
    \implies E[\mathbf{X}] &= \Sigma^{1/2}E[\mathbf{Z}] + \mathbf{\mu} = \mathbf{\mu}\newline
    Cov(\mathbf{X}, \mathbf{X}) &= E[\mathbf{X}\mathbf{X}^{T}] - E[\mathbf{X}]E[\mathbf{X}]^{T}\newline
    &= \Sigma^{1/2}Cov(\mathbf{Z})\roundbr{\Sigma^{1/2}}^{T} = \Sigma^{1/2}\mathbf{I}\_{n}\roundbr{\Sigma^{1/2}}^{T} = \Sigma\newline
    M(\mathbf{t}) &= E\squarebr{\exp\roundbr{\mathbf{t}^{T}\roundbr{\Sigma^{T}\mathbf{Z} + \mathbf{\mu}}}}\newline
    &= E\squarebr{\exp\roundbr{\mathbf{t}^{T}\Sigma^{1/2}\mathbf{Z}}}E\squarebr{\exp\roundbr{\mathbf{t}^{T}\mathbf{\mu}}} = E\squarebr{\exp\roundbr{\roundbr{\mathbf{t}^{T}\Sigma^{1/2}}\mathbf{Z}}}\exp\roundbr{\mathbf{t}^{T}\mathbf{\mu}}\newline
    &= \exp\roundbr{\frac{1}{2}\mathbf{t}^{T}\mathbf{\Sigma}\mathbf{t}}\exp\roundbr{\mathbf{t}^{T}\mathbf{\mu}}\newline
    &= \exp\roundbr{\mathbf{t}^{T}\mathbf{\mu} + \frac{1}{2}\mathbf{t}^{T}\Sigma\mathbf{t}}
\end{aligned}
$$

which must be familiar from the univariate case where mgf is $\exp\roundbr{\mu t + 1/2 \sigma^{2}t^{2}}$.

The distribution of $\mathbf{X}$ can be obtained using the Jacobian

$$
\begin{aligned}
    \mathbf{J} &= \frac{d\mathbf{Z}}{d\mathbf{X}} = \detm{\Sigma^{-1/2}} \newline
    \mathbf{Z} &= \Sigma^{-1/2}\roundbr{\mathbf{X} - \mathbf{\mu}}
\end{aligned}
$$

where the negative sign denotes the inverse.

$$
\begin{aligned}
    f_{\mathbf{X}}(\mathbf{x}) &= \roundbr{\frac{1}{2\pi}}^{\frac{n}{2}}\exp\roundbr{-\frac{1}{2}\roundbr{\mathbf{X} - \mathbf{\mu}}^{T}\roundbr{\Sigma^{-1/2}}^{T}\Sigma^{1/2}\roundbr{\mathbf{X} - \mathbf{\mu}}} \detm{\Sigma^{-1/2}}\newline
    &= \roundbr{\frac{1}{2\pi}}^{\frac{n}{2}}\frac{1}{\detm{\Sigma^{1/2}}}\exp\roundbr{-\frac{1}{2}\roundbr{\mathbf{X} - \mathbf{\mu}}^{T}\Sigma\roundbr{\mathbf{X} - \mathbf{\mu}}}
\end{aligned}
$$

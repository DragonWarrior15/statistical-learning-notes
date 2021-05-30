---
title: "Distributions for a Normal Population"
---

## Distributions for a Normal Population

Consider $X_{1}, X_{2}, \ldots, X_{n}$ be independently derived from a normal population with mean $\mu$ and variance $\sigma^{2}$

i.e., $X_{i} \sim \mathcal{N}(\mu, \sigma^{2}) \forall i = 1, 2, \ldots, n$


Based on the derivations above,
\begin{align}
        E[\overline{X}] &= \mu\newline
        Var(\overline{X}) &= \frac{\sigma^{2}}{n}
    \end{align}

And since the sum of normal random variables is also normal,
\begin{align}
        \frac{\overline{X} - \mu}{\sigma/\sqrt{n}} \sim \mathcal{N}(0, 1)
    \end{align}
which is similar to the central limit theorem.


From the derivation above for the sample variance,
\begin{align}
        E[S^{2}] = \sigma^{2}
    \end{align}

Now let's calcluate the distribution of $S^{2}$
\begin{align}
        S^{2} &= \frac{\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}}{n-1}\newline
        (n-1)S^{2} &= \sum_{i=1}^{n} (X_{i} - \overline{X})^{2}\newline
        &= \sum_{i=1}^{n} ((X_{i} - \mu) - (\overline{X} - \mu))^{2}\newline
        &= \sum_{i=1}^{n} ((X_{i} - \mu)^{2} + (\overline{X} - \mu)^{2} - 2(X_{i} - \mu)(\overline{X} - \mu))\newline
        &= \sum_{i=1}^{n} (X_{i} - \mu)^{2} + n(\overline{X} - \mu)^{2} - 2(\overline{X} - \mu)\sum_{i=1}^{n}(X_{i} - \mu)\newline
        &= \sum_{i=1}^{n} (X_{i} - \mu)^{2} + n(\overline{X} - \mu)^{2} - 2n(\overline{X} - \mu)^{2}\newline
        &= \sum_{i=1}^{n} (X_{i} - \mu)^{2} - n(\overline{X} - \mu)^{2}\newline
        \frac{(n-1)S^{2}}{\sigma^{2}} &= \sum_{i=1}^{n} (\frac{X_{i} - \mu}{\sigma})^{2} - (\frac{\overline{X} - \mu}{\sigma/\sqrt{n}})^{2} \quad\text{to make standard normals}\newline
        \text{or,}\quad \frac{(n-1)S^{2}}{\sigma^{2}} + (\frac{\overline{X} - \mu}{\sigma/\sqrt{n}})^{2} &= \sum_{i=1}^{n} (\frac{X_{i} - \mu}{\sigma})^{2}
    \end{align}

The right hand side is a chi-square variable with $n$ degrees of freedom and the second part of the left hand side is a chi-square variable with $1$ degree of freedom. We know that sum of independent chi-square variables is also a chi-square variable with degrees of freedom equal to the sum of individual degrees of freedom. Hence, it follows that
\begin{align}
        \frac{(n-1)S^{2}}{\sigma^{2}} \sim \chi_{n-1}^{2}
    \end{align}
and also the fact that **for a normal population, the sample mean and sample variance are independent variables with normal and chi-square distributions respectively**. This independence is a unique property for a normal distribution and is useful in parameter estimation and hypothesis testing.


Another interesting observation from the above derivations is
\begin{align}
        \sqrt{n}\frac{\overline{X} - \mu}{S} &\sim t_{n-1}\newline
        \text{whereas}\quad \sqrt{n}\frac{\overline{X} - \mu}{\sigma} &\sim \mathcal{N}(0,1)
    \end{align}
Note that the denominator is in the first equation is sample variance. The derivation is
\begin{align}
        \frac{Z}{\sqrt{\chi_{n}^{2}/n}} &\sim t_{n} \quad\text{definition}\newline
        \text{or,}\quad \frac{\frac{\overline{X} - \mu}{\sigma / \sqrt{n}}}{\sqrt{\frac{(n-1)S^{2}}{\sigma^{2}} \frac{1}{n-1}}} &\sim t_{n-1}\newline
        \text{or,}\quad \sqrt{n}\frac{\overline{X} - \mu}{S} &\sim t_{n-1}
    \end{align}

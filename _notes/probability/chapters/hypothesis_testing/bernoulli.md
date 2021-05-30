---
title: "Tests around Bernoulli Population"
---

## Tests around Bernoulli Population

Suppose we have a set of $n$ samples and we want to test how many of them satisfy a property (or equivalently, success). Let $p$ be the fraction of population satisfying he property and we want to check if this equals $p_{0}$
\begin{align}
        H_{0}: p \leq p_{0} \quad \text{versus} \quad p > p_{0}
    \end{align}

i.e., we reject this batch if the size of sample not satisfying the property (defective) is more than some predefined quantity/significance $p_{0}$.


We reject when the defectives in the sample ($X$) are more than a threshold $k$
\begin{align}
        P(X \geq k) = \sum_{i=k}^{n} \binom{n}{i} = \sum_{i=k}^{n} p^{i}(1-p)^{n-i}
    \end{align}

which is an increasing function in $p$. Hence, when $H_{0}$ is true,
\begin{align}
        P(X \geq k) \leq \sum_{i=k}^{n} p_{0}^{i}(1-p_{0})^{n-i}
    \end{align}

and we reject when $X \geq k^{\*}$ depending on the significance level $\alpha$
\begin{align}
        k^{\*} = \text{minimum}\quad k \quad \text{where} \quad \sum_{i=k}^{n} p_{0}^{i}(1-p_{0})^{n-i} \leq \alpha
    \end{align}
because there can be multiple $k$ which satisfy the above equation, and we want to reject $H_{0}$ as soon as the number of defectives in sample $X$ is more than the minimum $k$.


The test can also be done using *p-value*
\begin{align}
        \text{p-value} &= P(Bin(n, p_{0}) \geq x)\newline
        &= \sum_{i=x}^{n}p_{0}^{i}(1-p_{0})^{n-i}
    \end{align}

where $x$ is the count of defects in the sample. We reject $H_{0}$ at any $\alpha >$ *p-value* since in that situation the number of defects required will be much less than $x$.

For large $n$, $X$ will behave like a normal distribution and when $H_{0}$ is true,
\begin{align}
        \frac{X - np_{0}}{\sqrt{np_{0}(1-p_{0})}} \sim \mathcal{N}(0,1)
    \end{align}

and criteria discussed in [section]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#known-variance" | relative_url }}) hold.

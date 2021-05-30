---
title: "Tests around Variance of Normal Population"
---

## Tests around Variance of Normal Population

For a $n$ sized sample of independent observations from a normal population, we are interested in checking
\begin{align}
        H_{0}: \sigma^{2} = \sigma_{0}^{2} \quad \text{versus} \quad \sigma^{2} \neq \sigma_{0}^{2}
    \end{align}

Recall from [section]({{ "/notes/probability/chapters/sample_mean_var/normal.html#distributions-for-a-normal-population" | relative_url }})
\begin{align}
        \frac{(n-1)S^{2}}{\sigma^{2}} \sim \chi_{n-1}^{2}
    \end{align}

Then if $H_{0}$ is true, our test statistic
\begin{align}
        TS = \frac{(n-1)S^{2}}{\sigma_{0}^{2}} \sim \chi_{n-1}^{2}
    \end{align}

and from the test simply becomes
\begin{alignat}{2}
        \text{Accept} \quad &H_{0} \quad &&\text{if} \quad \chi_{1-\alpha/2, n-1}^{2} \leq TS \leq \chi_{\alpha/2, n-1}^{2}\newline
        \text{Reject} \quad &H_{0} \quad &&\text{otherwise}
    \end{alignat}

One sided test can be done in a similar manner, comparing with $\chi_{1-\alpha, n-1}^{2}$ or $\chi_{\alpha, n-1}^{2}$ based on which side we want to reject $H_{0}$.


### Comparing Variance of Two Normal Populations

We are interested in comparing
\begin{align}
        H_{0}: \sigma_{x}^{2} = \sigma_{y}^{2} \quad \text{versus} \quad \sigma_{x}^{2} \neq \sigma_{y}^{2}
    \end{align}

Recall that the ratio of sample variance with population variance is $\chi^{2}$-distributed, and the ratio of two $\chi^{2}$-distributed variables has an F-distribution. Hence, when $H_{0}$ is true,
\begin{align}
        TS = \frac{S_{x}^{2}}{S_{y}^{2}} \sim F_{n-1, m-1}
    \end{align}

Noting that F-distribution is always positive, the region for accepting $H_{0}$ simply become
\begin{alignat}{2}
        \text{Accept}\quad &H_{0} \quad &&\text{if} \quad F_{1-\alpha/2, n-1, m-1} \leq TS \leq F_{\alpha/2, n-1, m-1}\newline
        \text{Reject}\quad &H_{0} \quad &&\text{otherwise}
    \end{alignat}

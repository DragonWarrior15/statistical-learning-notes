---
title: "Testing Equality of Means of Two Normal Populations"
---

## Testing Equality of Means of Two Normal Populations

### Known Variances

Consider the two populations as
\begin{align}
        X_{1}, X_{2}, \ldots, X_{n} &\sim \mathcal{N}(\mu_{x}, \sigma_{x}^{2})\newline
        Y_{1}, Y_{2}, \ldots, Y_{m} &\sim \mathcal{N}(\mu_{y}, \sigma_{y}^{2})
    \end{align}

Then, the difference in the sample means will itself be a normal distribution (since it is the difference of two normals), and the test statistic can be defined as below
\begin{align}
        \overline{X} - \overline{Y} \sim \mathcal{N}(\mu_{x} - \mu_{y}, \sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}})\newline
        T = \frac{(\overline{X} - \overline{Y}) - (\mu_{x} - \mu_{y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} \sim \mathcal{N}(0, 1)
    \end{align}

when $H_{0}$ is true,
\begin{align}
        T = \frac{(\overline{X} - \overline{Y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} \sim \mathcal{N}(0, 1)
    \end{align}
and we compare the following hypotheses
\begin{alignat}{3}
        &H_{0}: \mu_{x} = \mu_{y} \quad &\text{versus} \quad &H_{1}: \mu_{x} \neq \mu_{y}\newline
        \text{or,} \quad &H_{0}: \mu_{x} - \mu_{y} = 0 \quad &\text{versus} \quad &H_{1}: \mu_{x} - \mu_{y} \neq 0
    \end{alignat}
we reject $H_{0}$ when the difference between the means is large, i.e., $H_{0}$ is testing whether the test statistic is close to zero or not

\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &T &> &z_{\alpha/2}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &T &\leq &z_{\alpha/2}
    \end{alignat}
where the variances of both the populations are known.


In a very similar fashion, the hypthesis testing rules for one sided test can be derived.

For
\begin{align}
        H_{0}: \mu_{x} \leq \mu_{y} \quad \text{versus} \quad H_{1}: \mu_{x} > \mu_{y}
    \end{align}
We reject $H_{0}$ when the difference $\mu_{x} - \mu_{y}$ is highly positive
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\frac{(\overline{X} - \overline{Y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} &> &z_{\alpha}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\frac{(\overline{X} - \overline{Y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} &\leq &z_{\alpha}
    \end{alignat}

For the other side of the test, we use the same criteria as above, but switching the sets $X$ and $Y$.

### Unknown but Equal Variances

We consider the same two populations of $Xs$ and $Ys$, but this time the variances are unknown. for simplicity of analysis, we assume that the unknown variances are same
\begin{align}
        \sigma_{x} = \sigma_{y} = \sigma
    \end{align}

From [section]({{ "/notes/probability/chapters/parameter_estimation/interval_estimates.html#estimating-difference-in-means-of-two-normal-populations" | relative_url }}), we know
\begin{align}
        S_{p}^{2} = \frac{(n-1)S_{1}^{2} + (m-1)S_{2}^{2}}{n + m - 2}\newline
        \frac{(\overline{X} - \overline{Y}) - (\mu_{x} - \mu_{y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} \div \frac{S_{p}}{\sigma} \sim t_{n+m-2}
    \end{align}

If $H_{0}$ is true, $\mu_{x} = \mu_{y}$ and we have
\begin{align}
        T = \frac{(\overline{X} - \overline{Y})}{S_{p}\sqrt{\frac{1}{m} + \frac{1}{n}}} \sim t_{n+m-2}
    \end{align}

and we have the critical region defined as
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &T &> &t_{\alpha/2, n+m-2}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &T &\leq &t_{\alpha/2, n+m-2}
    \end{alignat}

and for the one sided hypothesis
\begin{align}
        H_{0}: \mu_{x} \leq \mu_{y} \quad \text{versus} \quad H_{1}: \mu_{x} > \mu_{y}
    \end{align}
We reject $H_{0}$ when the difference $\mu_{x} - \mu_{y}$ is highly positive
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &T &> &t_{\alpha, n+m-2}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &T &\leq &z_{\alpha, n+m-2}
    \end{alignat}

### Unknown and Unequal Variances

We consider the natural test statistic as follows
\begin{align}
        \frac{(\overline{X} - \overline{Y}) - (\mu_{x} - \mu_{y})}{\sqrt{\frac{S_{x}^{2}}{n} + \frac{S_{y}^{2}}{m}}}
    \end{align}
Even when $H_{0}$ is true, the above is not a simple distribution to solve for. If we make the additional assumption that $n$ and $m$ are large, then
\begin{align}
        \frac{(\overline{X} - \overline{Y})}{\sqrt{\frac{S_{x}^{2}}{n} + \frac{S_{y}^{2}}{m}}} \sim \mathcal{N}(0, 1)
    \end{align}
and the same criteria for accepting and rejecting $H_{0}$ discussed [above](#known-variances) are applicable, but after replacing population variances with sample variances.


### Unknown and Unequal Variances

Suppose we want to observe the change in a quantity in a sample, after some kind of intervention. A simple example can be change in the mileage of a car after installation of a catalytic converter. Suppose we have $n$ samples with us, and for each of the sample, we associate $X_{i}$ with the measurement of the quantity before intervention and $Y_{i}$ with the quantity post intervention. Note that $X_{i}$ is not independent of $Y_{i}$ because they come from the same $i^{th}$ sample. Hence, the test discussed in [section](#known-variances) is not applicable.


Instead, we consider the quantity $W = X - Y$ and assume that $W_{i}$ come from a normal population. We can then consider the hypothesis
\begin{align}
        H_{0}: \mu_{w} = 0 \quad \text{versus} \quad H_{1}: \mu_{w} \neq 0
    \end{align}

Using the results derived in [section]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#unknown-variance" | relative_url }}), we have
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\sqrt{n}\frac{\overline{W}}{S_{w}} &> &t_{\alpha/2, n-1}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\sqrt{n}\frac{\overline{W}}{S_{w}} &\leq &t_{\alpha/2, n-1}
    \end{alignat}

One sided tests can be derived in exactly the same manner as [section]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#unknown-variance" | relative_url }}) and the concepts discussed in [section]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#p-value" | relative_url }}) still hold true.

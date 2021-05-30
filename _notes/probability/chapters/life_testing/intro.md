---
title: "Life Testing"
---

# Life Testing

This section develops statistical methods around estimtating distribution of variables indicating the lifetime of a particular object. For instance, if the lifetime has an exponential distribution, we utilise the sample to obtain the parameters of the exponential distribution.


Let $X$ be a continuous random variable denoting lifetime of an item, having cumulative distribution $F$ and density function $f$, then
\begin{align}
        \text{hazard function or failure rate,} \quad \lambda(t) &= \frac{f(t)}{1 - F(t)}\newline
        P(X \in (t, t+dt)|X > t) &= \frac{P(X \in (t, t+dt), X > t)}{P(X > t)} = \frac{P(X \in (t, t+dt))}{P(X > t)}\newline
        &\approx \frac{f(t)}{1 - F(t)} dt
    \end{align}

**$\lambda(t)$ denotes the conditional probability that an item of age t will fail in the next moment.**


For exponential distribution, $\lambda(t) = (\lambda e^{-\lambda x})/e^{-\lambda x} = \lambda$ because of the memoryless propoerty.


Hazard function uniquely determines the cumulative distribution $F$
\begin{align}
        \lambda(s) &= \frac{\frac{d}{ds} F(s)}{1 - F(s)} = \frac{d}{ds} (-log(1 - F(s)))\newline
        F(t) &= 1 - exp\left(-\int_{0}^{s} \lambda(s) ds \right)
    \end{align}

## Exponential Distribution: Stopping at rth failure

Suppose we have $n$ items with exponentially distributed lifetime with unknown parameter and we wish to estimate the mean $\theta (note \lambda = 1/\theta)$. We observe the items until $r$ failures and try to estimate $\theta$. Let $X_{i}$ denote the lifetime of the $i^{th}$ item with the following notation
\begin{align}
        x_{1} \leq x_{2} \leq \ldots \leq x_{r} \quad \text{for} \quad i_{1}, i_{2}, \ldots, i_{n}
    \end{align}
i.e., $X_{i_{j}} = x_{j}$. Then the joint likelihood becomes
\begin{align}
        L &= \left(\prod_{i=1}^{r} \frac{1}{\theta}e^{-x_{i}/\theta}\right) \left(\prod_{j=r+1}^{n} e^{-x_{r}/\theta}\right)\newline
        &= \frac{1}{\theta^{r}}exp \left\\{-\frac{1}{\theta} \left(\sum_{i=1}^{r} x_{i} + (n-r)x_{r} \right) \right\\}\newline
        \log(L) &= -r\log(\theta) - \frac{\sum_{i=1}^{r} x_{i}}{\theta} - \frac{(n-r)x_{r}}{\theta}\newline
        \frac{d}{d\theta}\log(L) &= -\frac{r}{\theta} + \frac{\sum_{i=1}^{r} x_{i}}{\theta^{2}} + \frac{(n-r)x_{r}}{\theta^{2}}\newline
        \hat{\theta} &= \frac{\sum_{i=1}^{r} x_{i} + (n-r)x_{r}}{r} = \frac{\tau}{r}
    \end{align}
where we note that for $n-r$ items, the lifetime is known only to be more than $x_{r}$ and thus we use the cumulative probability of lifetime $> x_{r}$ in the likelihood equation. We can replace the values with random variables in above equations.


$\tau$ is the total time on test, i.e. the total time of survival of each item for the duration the test ran ($X_{r}$). Now, we can rewrite $\tau$ using the differences between consecutive times of failures. Note than all items survive for $X_{1}$ time, $n-1$ items survive for at least $X_{2} - X_{1}$ time, and so on till $n-r+1$ items survive for additional $X_{r} - X_{r-1}$ time. Thus,
\begin{align}
        \tau = nX_{1} + (n-1)(X_{2} - X_{1}) + \cdots + (n-r+1)(X_{r} - X_{r-1})
    \end{align}
and from [answer]({{ "/notes/probability/chapters/exercises/a_minexp.html" | relative_url }}), we know that $X_{1}$ is exponential with mean $\theta/n$ and thus, $nX_{1}$ has mean $\theta$. By memoryless property, $X_{2} - X_{1}$ is also exponential with mean $\theta/(n-1)$ and so $(n-1)(X_{2} - X_{1})$ has mean $\theta$. Thus, $\tau$ is the sum of independent exponential variables and is a Gamma distribution with parameters $(r, 1/\theta)$. Since Gamma distribution is related to a $\chi^{2}$ distribution (see [here]({{ "/notes/probability/chapters/distributions/chi_square.html#relation-between-chi-square-and-gamma-distribution" | relative_url }}))
\begin{align}
        \frac{2\tau}{\theta} &\sim \chi_{2r}^{2}\newline
        P(\chi_{1-\alpha/2, 2r}^{2} &< \frac{2\tau}{\theta} < \chi_{\alpha/2, 2r}^{2}) = 1-\alpha\newline
        \theta &\in \left(\frac{2\tau}{\chi_{\alpha/2, 2r}^{2}}, \frac{2\tau}{\chi_{1-\alpha/2, 2r}^{2}} \right) \quad \text{with confidence $1-\alpha$}
    \end{align}

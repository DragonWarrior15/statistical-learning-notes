---
title: "Maximum Likelihood Estimator"
---

## Maximum Likelihood Estimator

Maximum Likelihood Estimator or MLE is based on the idea to **find that value of $\theta$ that maximizes the probability of observing the given set of samples of the population**. Alternately, let $x_{i}$ for $i=1,2,\ldots,n$ be $n$ samples drawn from a population whose distribution is parametrized by $\theta$ (can be a vector as well). Then we define the likelihood function as
\begin{align}
        \text{likelihood function}\quad = L(\theta) = f(x_{1}, x_{2}, \ldots, x_{n}|\theta) = \quad \text{a function of $\theta$}
    \end{align}
i.e., the joint probability (or density) of occurrence of all the samples under the given distribution for some value of $\theta$.

We aim to maximize this likelihood to get the estimate of $\theta$.
\begin{align}
        \hat{\theta} = \argmax_{\theta}L(\theta)
\end{align}
where $\hat{\theta}$ denotes our estimate of $\theta$. If the likelihood is a differentiable function of $\theta$, we can simply equate the derivative of likelihood with respect to $\theta$ to zero.

It is often the case that taking logarithm of both sides allows for an easy way of estimation. Note that both likelihood an log likelihood are maximized by the same value of estimator because $\log$ is a monotonically increasing function (convex).

If $\mathbf{\theta}$ is a vector, we will obtain a system of equations to be solved simultaneously.


### MLE for Bernoulli Variable

Suppose we observe $n$ independent samples from a Bernoulli process and the aim is to find the MLE for the probability of success.

Let $p$ denote the probability of success. Then,
\begin{align}
        P(X_{i} = x) &= p^{x}(1-p)^{1-x} \quad\text{where $x$ is $0$ or $1$}\newline
        \text{or,}\quad P(X_{i} = x_{i}) &= p^{x_{i}}(1-p)^{1-x_{i}}
    \end{align}
Since all the samples are independent, the joint probability or likelihood is simply the product of all the probabilities
\begin{align}
        f(x_{1}, x_{2}, \ldots, x_{n}|p) &= p^{x_{1}}(1-p)^{1-x_{1}} \ldots p^{x_{n}}(1-p)^{1-x_{n}}\newline
        &= p^{\sum_{i=1}^{n}x_{i}} (1-p)^{n-\sum_{i=1}^{n}x_{i}}\newline
        log(f(x_{1}, x_{2}, \ldots, x_{n}|p)) &= {\sum_{i=1}^{n}x_{i}}log(p) + (n-{\sum_{i=1}^{n}x_{i}})log(1-p)
    \end{align}
Taking the derivative with respect to $p$ to maximize,
\begin{align}
        \frac{d}{dp}log(f(x_{1}, x_{2}, \ldots, x_{n}|p)) &= {\sum_{i=1}^{n}x_{i}}\frac{1}{p} - (n-{\sum_{i=1}^{n}x_{i}})\frac{1}{1-p} = 0\newline
        \text{or,}\quad \hat{p} &= \frac{\sum_{i=1}^{n}x_{i}}{n}
    \end{align}
which is the proportion of successful trials in the sample. It is also an unbiased estimator.

### MLE for Poisson Variable

Suppose that we observe $n$ random samples obtained from a poisson process. Recall
\begin{align}
        P(X = k) = \frac{e^{-\lambda} \lambda^{k}}{k!}
    \end{align}
Hence, the joint distribution can be written as
\begin{align}
        f(x_{1}, x_{2}, \ldots, x_{n}|p) &= \prod_{i=1}^{n} \frac{e^{-\lambda} \lambda^{x_{i}}}{x_{i}!}\newline
        f(x_{1}, x_{2}, \ldots, x_{n}|p) &= \frac{e^{-n\lambda} \lambda^{\sum_{i=1}^{n} x_{i}}}{\prod_{i=1}^{n} x_{i}!}\newline
        log(f(x_{1}, x_{2}, \ldots, x_{n}|p)) &= -n\lambda + (\sum_{i=1}^{n} x_{i})log(\lambda) - \sum_{i=1}^{n} log(x_{i}!)\newline
        \frac{d}{dp}(f(x_{1}, x_{2}, \ldots, x_{n}|p)) &= -n + (\sum_{i=1}^{n} x_{i})\frac{1}{\lambda}\newline
        &= 0\newline
        \text{or,}\quad \hat{\lambda} &= \frac{\sum_{i=1}^{n} x_{i}}{n}
    \end{align}
i.e., the average rate is simply the average of all the observed arrivals.

### MLE for Normal Variable

Suppose we observe $n$ samples from a normal population whose mean is $\mu$ and variance is $\sigma^{2}$. We will aim to obtain MLE estimates for both the mean and variance. Recall
\begin{align}
         P(X = x) = \frac{1}{\sqrt{2 \pi \sigma^{2}}} exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})
    \end{align}

Hence, the likelihood will be
\begin{align}
        f(x_{1}, x_{2}, \ldots, x_{n}|\mu, \sigma^{2}) &= \prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi \sigma^{2}}} exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})\newline
        log(f(x_{1}, x_{2}, \ldots, x_{n}|\mu, \sigma^{2})) &= -\frac{n}{2}\log(2\pi) - n\log(\sigma) - \frac{1}{2\sigma^{2}}(\sum_{i=1}^{n} (x_{i} - \mu)^{2})\newline
        \frac{d}{d\mu}(log(f(x_{1}, x_{2}, \ldots, x_{n}|\mu, \sigma^{2}))) &= -\frac{1}{\sigma^{2}}(\sum_{i=1}^{n} (x_{i} - \mu))\newline
        &= 0\newline
        \text{or,}\quad \hat{\mu} &= \frac{\sum_{i=1}^{n} x_{i}}{n}\newline
        \frac{d}{d\sigma}(log(f(x_{1}, x_{2}, \ldots, x_{n}|\mu, \sigma^{2}))) &= - \frac{n}{\sigma} - \frac{1}{2\sigma^{2}}(\sum_{i=1}^{n} (x_{i} - \mu)^{2})\newline
        &= 0\newline
        \text{or,}\quad \hat{\sigma}^{2} &= \frac{\sum_{i=1}^{n}(x_{i} - \mu)^2}{n}\newline
        &= \frac{\sum_{i=1}^{n}(x_{i} - \overline{x})^2}{n}\newline
        \text{where}\quad \overline{x} &= \frac{\sum_{i=1}^{n} x_{i}}{n}
    \end{align}
Note that the estimator for variance is different from the sample variance
\begin{align}
        \text{MLE}\quad \sigma^{2} &= \frac{\sum_{i=1}^{n}(x_{i} - \overline{x})^2}{n}\newline
        S^{2} &= \frac{\sum_{i=1}^{n}(x_{i} - \overline{x})^2}{n - 1}
    \end{align}

### MLE for Uniform Random Variable

Consider oberving $n$ samples from a uniform distribution with the parameter $\theta$. Then,
\begin{align}
        f(x_{1}, x_{2}, \ldots, x_{n}|\theta) = \frac{1}{\theta^{n}}
    \end{align}
which is clearly maximized when $\theta$ is minimum. But since $\theta$ has to be at least as large as the maximum observed value,
\begin{align}
        \hat{\theta} = max(x_{1}, x_{2}, \ldots, x_{n})
    \end{align}

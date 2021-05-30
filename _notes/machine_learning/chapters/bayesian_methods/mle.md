---
title: "Maximum Likelihood Estimator (MLE)"
---

## Maximum Likelihood Estimator (MLE)

MLE is a technique to get the estimates of the parameters of a distribution. Suppose we have a distribution with unknown parameters $\theta$ and we have a set of observed variables $X$ coming from that distribution. Then
\begin{align}
    \hat{\theta}\_{MLE} = \max_{\theta}p(X|\theta)\end{align}
i.e., the best estimate of $\theta$ assuming the data comes from the given distribution. $p(X|\theta)$ is nothing but the joint likelihood of the data under the given distribution. This is not strictly a probability value. To convert this to a probability value, we would be dividing by a normalizing constant which would not play a role in maximization.


Suppose we have $N$ observations that we know come from a Multivariate Gaussian. Suppose the unknown mean is $\mu$ (a $d$ dimensional vector) and the (symmetric) covariance matrix is $\Sigma$ ($d \times d$).
\begin{align}
    p(X|\theta) &= p(x_{1}|\theta)p(x_{2}|\theta) \ldots p(x_{N}|\theta)\newline
    &= \prod_{i=1}^{N}\frac{1}{(2\pi)^{d/2} \lvert \Sigma \rvert^{1/2}} exp \bigg(-\frac{1}{2}(x_{i} - \mu)^{T}\Sigma^{-1}(x_{i} - \mu) \bigg)\newline
    log(p(X|\theta)) &= -\frac{Nd}{2}log(2\pi) - \frac{N}{2}log(\lvert \Sigma \rvert) + \sum_{i=1}^{N}-\frac{1}{2}(x_{i} - \mu)^{T}\Sigma^{-1}(x_{i} - \mu)\newline
    \frac{\partial log(p(X|\theta))}{\partial \mu}(\mu, \Sigma) &= -\frac{1}{2}\sum_{i=1}^{N} ((x_{i} - \mu)^{T}\Sigma^{-1})^{T} - \frac{1}{2}\sum_{i=1}^{N} \Sigma^{-1}(x_{i} - \mu)\newline
    &= -\Sigma^{-1}\sum_{i=1}^{N} (x_{i} - \mu)\newline
    \text{Hence,} \quad 0 &= \sum_{i=1}^{N} (x_{i} - \mu)\newline
    \hat{\mu}\_{MLE} &= \frac{1}{N}\sum_{i=1}^{N} x_{i}\end{align}

where we have used the fact that $\Sigma$ is symmetic and so will be it's inverse. We obtain the last two equations by equating the derivative to $0$ to find the maxima.

### Fisher Information

The maximum likelihood estimation procedure can also be used to estimate the precision in the values of $\hat{\theta}$. Let $l(\theta;X)$ denote the log likelihood. Then,
\begin{align}
    P(X|\theta) &= \prod_{i=1}^{N} p(x_{i}|\theta)\newline
    l(\theta;X) &= \sum_{i=1}^{N} l(\theta;x_{i})\newline
    \frac{\partial l(\theta;X)}{\partial \theta}(\theta) &= \sum_{i=1}^{N} \frac{\partial l(\theta;x_{i})}{\partial \theta}(\theta)\newline
    \text{Informtion Matrix} \quad \mathbf{I}(\theta) &= -\sum_{i=1}^{N} \frac{\partial^{2}l(\theta;x_{i})}{\partial \theta \partial \theta^{T}}\end{align}

Let $\hat{\theta}$ denote $\hat{\theta}\_{MLE}$. The information matrix evaluated at $\hat{\theta}$ is also called the observed information. Also notice that at the maxima, $l(\hat{\theta}) = 0$. Fisher information is given by
\begin{align}
    \mathbf{i}(\theta) = E_{\theta}[\mathbf{I}(\theta)]\end{align}

where both $\mathbf{i}$ and $\mathbf{I}$ behave analogous to a variance term. If $\theta_{0}$ denotes the true value of the distribution parameters, we have in the limiting case of $N \rightarrow \inf$
\begin{align}
    \hat{\theta} \sim \mathcal{N}(\theta_{0}, \mathbf{I}^{-1}(\theta_{0})) = \mathcal{N}(\theta_{0}, \mathbf{i}^{-1}(\theta_{0}))\end{align}
since in the limiting case, expected value will be the same as the sum of inifinite terms (the probability weights in expectation will be represented correctly in this infinite sum).

The $1-\alpha$ confidence intervals of the parameter estimates can be quickly evaluated using the estimate of variance at $\hat{\theta}$
\begin{align}
    P(-z_{\alpha/2} < \frac{\hat{\theta}\_{j} - \theta_{0,j}}{\mathbf{I}^{-1}(\theta_{0,j})} < z_{\alpha/2}) = 1 - \alpha\newline
    \text{or,} \quad \theta_{0,j} \in \hat{\theta}\_{j} \pm \mathbf{I}^{-1}(\hat{\theta}\_{j})z_{\alpha/2}\end{align}
and we can replace $\mathbf{I}$ with $\mathbf{i}$ in the case of large $N$.


A more exact distribution can be obtained using
\begin{align}
    2(l(\hat{\theta}) - l(\theta_{0})) \sim \chi^{2}\_{p}\end{align}
where $p$ is the dimension of the vector space of $x_{i}$s. Note that this gives the distribution of log likelihood and not $\theta$ directly.

---
title: "Evaluating an Estimator"
---

## Evaluating an Estimator

Let $\boldsymbol{X} = (X_{1}, X_{2}, \ldots, X_{n})$ be the set of random variables sampled from a population whose parameters are defined by $\theta$. Let $d(\boldsymbol{X})$ denote an estimator of $\theta$. Then
\begin{align}
        r(d, \theta) = E[(d(\boldsymbol{X}) - \theta)^{2}]
    \end{align}
denotes the mean squared estimator of $\boldsymbol{X}$. Although it is rare to find an estimator that minimizes this error, we can certainly find the minima under the set of estimators satisfying a certain criteria.

The bias of an estimator is defined as
\begin{align}
        b_{\theta}(d) = E[d(\boldsymbol{X})] - \theta
    \end{align}
If the bias is zero, then the estimator is called an **unbiased estimator**. That is, the expected value of the estimator is same as the parameter being estimated.


For an unbiased estimator, the mean square error is
\begin{align}
        r(d, \theta) &= E[(d(\boldsymbol{X}) - \theta)^{2}]\newline
        &= E[(d(\boldsymbol{X}) - E[d(\boldsymbol{X})])^{2}]\newline
        &= Var(d(\boldsymbol{X}))
    \end{align}
i.e., the mean squared error of an unbiased estimator is equal to its variance.


Let $X_{1}, X_{2}, \ldots, X_{n}$ be sampled from a distribution whose mean is $\theta$. Then,
\begin{align}
        d(\boldsymbol{X}) &= \sum_{i=1}^{n} \lambda_{i} X_{i}\newline
        \text{and}\quad \sum_{i=1}^{n}\lambda_{i} &= 1
    \end{align}
is also an unbiased estimator because
\begin{align}
        E[\sum_{i=1}^{n} \lambda_{i} X_{i}] &= \sum_{i=1}^{n} \lambda_{i} E[X_{i}]\newline
        &= \theta \sum_{i=1}^{n}\lambda_{i}\newline
        &= \theta
    \end{align}

### Combining Unbiased Estimators

Suppose we have $n$ unbiased estimators $d_{1}, \ldots, d_{n}$ for a parameter $\theta$ with different independent variances
\begin{align}
        E[d_{i}] = \theta \quad Var(d_{i}) = \sigma_{i}^{2}
    \end{align}
Then, a weighted combination of these estimators is also an unbiased estimator of $\theta$ (assuming that the weights sum up to 1). Suppose we wish to find a set of weights that minimize the mean squared error to get the best estimator, then
\begin{align}
        d &= \sum_{i=1}^{n} w_{i} d_{i} \quad\text{where $\sum_{i=1}^{n} w_{i} = 1$}\newline
        r(d, \theta) &= Var(d) \quad\text{(derived above)}\newline
        &= Var(\sum_{i=1}^{n} w_{i} d_{i})
        = \sum_{i=1}^{n} w_{i}^{2} Var(d_{i}) \quad\text{by independence}\newline
        &= \sum_{i=1}^{n} w_{i}^{2} \sigma_{i}^{2}
    \end{align}
\begin{align}
        \text{So we minimize}\quad \sum_{i=1}^{n} w_{i}^{2} \sigma_{i}^{2} - \lambda(\sum_{i=1}^{n} w_{i}-1) \quad \text{ssing $\lambda$ as Lagrange multiplier}\newline
        \text{Taking the derivative for any $i$,}\quad 0 = 2\sigma_{i}^{2} w_{i} - \lambda \newline
        \text{Using}\quad \sum_{i=1}^{n} w_{i} = 1, \quad
        w_{i} = \frac{1/\sigma_{i}^{2}}{1/\sigma_{1}^{2} + 1/\sigma_{2}^{2} + \cdots + 1/\sigma_{n}^{2}}
    \end{align}
or, the weights for the estimators are inversely proportional to their individual variances. This is useful in situations when we have $n$ independent results for evaluation of a parameter, and we want to increase our confidence in the estimator by combining all these independent results.


### Relation between Bias and Variance

The result obtained above that the mean squared error of an unbiased estimator is it's variance can be generalized for the case of any estimator as follows
\begin{align}
        r(d, \theta) &= E[(d - \theta)^{2}]\newline
        &= E[(d - E[d] + E[d] -\theta)^{2}]\newline
        &= E[(d - E[d])^{2} + (E[d] - \theta)^{2} + 2(d - E[d])(E[d] - \theta)]\newline
        &= E[(d - E[d])^{2}] + E[(E[d] - \theta)^{2}] + 2(E[d] - \theta)E[d - E[d]]\newline
        &= E[(d - E[d])^{2}] + (E[d] - \theta)^{2}\newline
        r(d, \theta) &= Var(d) + b_{\theta}^{2}(d)\newline
    \end{align}
where we have noted that $E[d - E[d]] = E[d] - E[d] = 0$ and $E[d] - \theta$ is a constant since $E[d]$ itself is a constant.

### Minimum Variance Unbiased Estimator (MVUE)

For an unbiased estimator, the MSE derived above is only dependent on the variance of the estimator. Hence, the MVUE is the one for which the variance is the minimum.

#### Cramer Rao Lower Bound (CRLB) & Related Theorems

The CRLB sets a lower bound on the variance of any unbiased estimator. If this lower bound is known,

* If the variance of an unbiased estimator equals this lower bound, we know that we have found the MVUE
* The lower bound provides a benchmark against which to compare different estimators
* The bound can be used to rule out impossible estimators

##### Fisher Information

To calculate the CRLB, we first define Fisher Information (FI). For any distribution with the density function $f_{X}(x \vert \theta)$ and a random variable $X$, the FI measures a kind of variance of $X$ with respect to $\theta$. If the density function has peaks, knowing $X$ can provide a lot of information about $\theta$. On the other hand, a flat distribution will require many samples of $X$ to find out a good estimate of $\theta$. Mathemtically, for a single random variable $X$, FI is defined as
\begin{align}
        \mathcal{I}(\theta) = E \bigg[ \bigg(\frac{\partial}{\partial \theta} \ln f_{X}(X; \theta)\bigg)^{2} \bigg \vert \theta \bigg]
    \end{align}
and if the density is twice differentiable,
\begin{align}
        \mathcal{I}(\theta) = -E \bigg[ \frac{\partial^{2}}{\partial \theta^{2}} \ln f_{X}(X; \theta) \bigg \vert \theta \bigg]
    \end{align}

Fisher information is additive. The total Fisher information for a set of $n$ independent random variables from the same distribution will simply be $n\mathcal{I}(\theta)$ where $\mathcal{I}(\theta)$ has been derived above.

##### Sufficient Statistic

Another important definition is a sufficient statistic. Any statistic of the population $t = T(X)$ (for instance, sample mean is a population statistic, and so is sample variance) is called a sufficient statistic for the parameter $\theta$ if the conditional probability distribution of the data (or sample) $X$ given $t$ does not depend on parameter $\theta$. That is, once $t$ is known, the data will provide no additional information about $\theta$.
\begin{align}
        t = T(X) \quad \text{is sufficient statistic if} \quad P(X \vert t) \perp \theta
    \end{align}

##### Fisher Neyman Factorization Theorem

The theorem states that a given statistic $T(X)$ is sufficient if and only if
\begin{align}
        f_{X}(x;\theta) = h(X)g(T(X), \theta)
    \end{align}
where $h$ depends on the data while $g$ depends on $\theta$ and on the data $X$ only through $T(X)$.

Then, for an unbiased estimator $\hat{\theta}$ and Fisher information $\mathcal{I}(\theta)$ for a single observation, the CRLB is
\begin{align}
        Var(\hat{\theta}) \geq \frac{1}{n\mathcal{I}(\theta)}
    \end{align}

The above is a universal bound for unbiased estimators. The lower bound is slightly different for biased estimators. Let $b(\theta)$ denote the bias for estimator $T(X)$, then
\begin{align}
        Var(T(X)) \geq \frac{(1 + b'(\theta))^{2}}{n\mathcal{I}(\theta)}
    \end{align}

##### Complete Statistic

A statistic $T$ is called complete if $E_{\theta}[g(T)] = 0$ for all $\theta$ and some function $g$ implies that $P(g(T) = 0) = 1$ for all $\theta$.

##### Lehmann--Scheffe Theorem

The theorem states that any unbiased estimator of an unknown quantity that depends on the data only through a complete sufficient statistic is the unique best unbiased estimator of that quantity.

##### Rao-Blackwell Theorem

If $g(X)$ is any kind of estimator of an unknown $\theta$, the conditional expectation of $g(X)$ given $T(X)$ (a sufficient statistic) is typically a better estimate of $\theta$ and never worse. Often, one can start off with a crude estimator $g(X)$ and compute the expected value to get an estimator that is optimal in various senses.

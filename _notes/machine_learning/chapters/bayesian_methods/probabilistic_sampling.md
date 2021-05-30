---
title: "Sampling from Distributions"
---

## Sampling from Distributions

### Rejection Sampling

Consider a probability distribution $p(x)$ that we want to sample from, and suppose there is another distribution $q(x)$ such that $p(x) \leq Mq(x)$ where $M$ is a constant scalar. Assume that $q$ is a distribution from which we can easily sample. Then to sample from $p(x)$

1.  Sample a point $x_{0}$ from $q(x)$

2.  Sample a point $u$ from $U(0,Mq(x_{0}))$

3.  Accept $x_{0}$ with probability $\frac{p(x_{0})}{Mq(x_{0})}$ if $u \leq p(x_{0})$

The scheme works because any point we are accepting lies inside the curve $p(x)$. Also, on average, we will get $1$ accepted point for every $M$ samples because the total points generated cover the area under $q(x)$ while the accepted ones cover the area under $Mq(x)$. The total points accepted are simply the ratios of area under $p(x)$ and $M(q(x)$.


The technique works equally well if we know the distribution only upto a normalization constant
\begin{align}
    \frac{\tilde{p}(x)}{Z} \leq Mq(x) \implies \tilde{p}(x) \leq M^{\prime}q(x), \; M^{\prime} = ZM\end{align}

{% include image.html url="notes/machine_learning/images/sampling_1.png" description="Rejection Sampling: $u$ is selected with probability $p(x)/Mq(x)$" img_classes="notes-img" %}

### Gibbs Sampling

Gibbs Sampling is a markov chain based sampling method which samples from a multivaraiate distribution one component at a time. Specifically, any component is sampled using a conditional distribution on all the remaining components, where we use the latest available values for those components. Suppose we are sampling from a $d$ dimensional distribution $p(x)$

1.  Initialize ($x_{1}^{(0)},\ldots x_{d}^{(0)}$) as random values or zeros

2.  For $k = 0,1,2,\ldots$
    \begin{align}
            x_{1}^{(k+1)} &\sim p(x_{1}|x_{2}^{(k)},\ldots x_{d}^{(k)})\newline
            x_{2}^{(k+1)} &\sim p(x_{2}|x_{1}^{(k+1)},x_{3}^{(k)},\ldots x_{d}^{(k)})\newline
            x_{3}^{(k+1)} &\sim p(x_{3}|x_{1}^{(k+1)},x_{2}^{(k+1)},x_{4}^{(k)},\ldots x_{d}^{(k)})\newline
            \vdots\newline
            x_{d}^{(k+1)} &\sim p(x_{d}|x_{1}^{(k+1)},x_{2}^{(k+1)},\ldots x_{d-1}^{(k+1)})\newline
        \end{align}

Each of the samplings steps involve a single variable. This sampling is easy if we know a good sampling procedure for the same already, or something generic like rejection sampling can be used.


This iterative procedure works because
\begin{align}
    p(x_{1}^{(k+1)},\ldots,x_{d}^{(k+1)}) = \sum_{x_{1}^{(k)},\ldots,x_{d}^{(k)}} Q(x_{1}^{(k)},\ldots,x_{d}^{(k)} \rightarrow x_{1}^{(k+1)},\ldots,x_{d}^{(k+1)}) p(x_{1}^{(k)},\ldots,x_{d}^{(k)})\newline
    Q = p(x_{1}^{(k+1)}|x_{2}^{(k)},\ldots x_{d}^{(k)})p(x_{2}^{(k+1)}|x_{1}^{(k+1)},x_{3}^{(k)},\ldots x_{d}^{(k)}) \ldots p(x_{d}^{(k+1)}|x_{1}^{(k+1)},x_{2}^{(k+1)},\ldots x_{d-1}^{(k+1)})\end{align}
which can be solved by breaking the sum over the different components and marginalizing the sum one component at a time. $Q$ is nothing but the transition probability of the markov chain.


Since the procedure uses a markov chain, we disregard some of the initial points as the chain may not have converged till then. This is called the burn-in period (say 1000 samples). Further, it is sually the case that successive samples have high degree of correlation between. To avoid this, after the burn-in period has passed, we only keep every $k^{th}$ (say 100) observation in the final set of samples. The procedure works even if the distribution is known only upto a normalization constant.

### Metropolis Hastings

Metropolis Hastings uses the concept of rejection sampling and markov chains to develop and efficient sampling procedure. Unlike the fixed transition probabilities in Gibbs sampling, we have the freedom to choose the appropriate transition function here, to produce less correlated samples.

Consider a markov chain $Q$ that will define transition probabilities and sampling procedure, a critic $A$ that will tell us to accept or reject a sampled point and $T$ as the final markov chain. Then,
\begin{align}
    T(\boldsymbol{x}\rightarrow \boldsymbol{x}^{\prime}) = Q(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime})A(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime})\end{align}
which we want to be stationary.
\begin{align}
    \text{Assume} \quad \pi(\boldsymbol{x})T(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime}) &= \pi(\boldsymbol{x}^{\prime})T(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x})\newline
    \implies \sum_{\boldsymbol{x}} \pi(\boldsymbol{x})T(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime}) &= \sum_{\boldsymbol{x}} \pi(\boldsymbol{x}^{\prime})T(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x}) = \pi(\boldsymbol{x}^{\prime})\end{align}
which is the stationarity condition for a markov chain and $\pi$ denote the long term stationary probabilities. These are indeed the probability distribution $P$ we are trying to approximate. To check stationarity, we only need to work with the first equation and choose $A$ accordingly
\begin{align}
{2}
    \pi(\boldsymbol{x})Q(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime})A(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime}) &= \pi(\boldsymbol{x}^{\prime})Q(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x})A(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x})\newline
    \frac{A(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime})}{A(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x})} &= \frac{\pi(\boldsymbol{x}^{\prime})Q(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x})}{\pi(\boldsymbol{x})Q(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime})} = \rho\newline
    A(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime}), A(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x}) &= \begin{cases} \rho, 1 &\mbox{if $\rho < 1$}\newline
    1, 1/\rho &\mbox{otherwise} \end{cases}\newline
    \implies A(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime}) &= \min \bigg(1, \frac{\pi(\boldsymbol{x}^{\prime})Q(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x})}{\pi(\boldsymbol{x})Q(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime})}\bigg)\end{align}
when $\rho < 1$, we keep $A(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime}) = \rho$ so as to maximize the acceptance probability (other combinations like fractions of $\rho$ will also work, but will have lower acceptance probability). $A$ is also a probability distribution and $\in [0,1]$.


The Metropolis Hastings Algorithm becomes

1.  Initialize $\boldsymbol{x}^{(k)}$ randomly

2.  For $k = 1, 2, \ldots$

    1.  Sample $\boldsymbol{x}^{\prime} \sim Q(\boldsymbol{x}^{(k)} \rightarrow \boldsymbol{x}^{\prime})$

    2.  Calculate acceptance probability as
        \begin{align}
                    \rho = \min \bigg(1, \frac{P(\boldsymbol{x}^{\prime})Q(\boldsymbol{x}^{\prime} \rightarrow \boldsymbol{x})}{P(\boldsymbol{x})Q(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime})} \bigg)
                \end{align}

    3.  With probability $\rho$, $\boldsymbol{x}^{(k+1)} = \boldsymbol{x}^{\prime}$ else $\boldsymbol{x}^{(k)}$

A very naive choice of $x^{\prime} \sim Q(\boldsymbol{x} \rightarrow \boldsymbol{x}^{\prime}) = \mathcal{N}(\boldsymbol{x}, \boldsymbol{I})$. A few points about Metropolis Hastings algorithm

-   The algorithm is rejection sampling applied at markov chains

-   There is a burn-in period and we will reject some of the initial samples (say 1000) to allow the chain to stabilize

-   We have the choice over $Q$ which can be a family of distributions. Different choices of $Q$ will lead to different rates of convergence

-   The method can be executed in parallel by running different chains on different machines

-   Unnormalized distributions can also be sampled from since we have the ratio term in $A$

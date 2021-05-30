---
title: "Answer"
---

To find the lower bound, we need to calculate the Fisher Information first (we use the second form since the density is twice differentiable)
\begin{align}
        \mathcal{I}(\theta) &= -E \bigg[ \frac{\partial^{2}}{\partial \theta^{2}} \ln f_{X}(X; \theta) \bigg \vert \theta \bigg]\newline
        &= -E \bigg[ \frac{\partial^{2}}{\partial \theta^{2}} \bigg(-\ln(\theta) - \frac{X}{\theta} \bigg) \bigg]\newline
        &= -E \bigg[ \frac{1}{\theta}^{2} - \frac{2X}{\theta^{3}} \bigg]\newline
        &= -\frac{1}{\theta}^{2} + \frac{2}{\theta^{3}}E[X] = -\frac{1}{\theta}^{2} + \frac{2}{\theta^{2}} = \frac{1}{\theta^{2}}\newline
        \implies Var(\theta) &\geq \frac{1}{n\mathcal{I}(\theta)} = \frac{\theta^{2}}{n}
    \end{align}
For the second part, to show $T$ is the MVUE of $\theta$, we calculate the expected value and variance of the statistic (of the $n$ independent random variables)
\begin{align}
        E[T] &= \frac{1}{n} \sum_{i=1}^{N}E[X_{i}] = E[X] = \theta\newline
        Var(T) &= \sum_{i=1}^{n} Var(\frac{X_{i}}{n}) = n\frac{\theta^{2}}{n^{2}} = \frac{\theta^{2}}{n}
    \end{align}
Since $E[T] = E[X]$, $T$ is an unbiased estimator. And, since the $Var(X) =$ CRLB, $T$ is the MVUE of $\theta$.

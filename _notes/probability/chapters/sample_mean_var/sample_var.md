---
title: "Sample Variance"
---

## Sample Variance

The sample variance is defined as
\begin{align}
        S^{2} = \frac{\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}}{n - 1}
    \end{align}
where $\overline{X}$ is the sample mean. Similar to the sample mean, this is also a random variable. We divide by $n-1$ so that the estimator is unbiased, as shown below by calculating the mean of the estimator
\begin{align}
        E[S^{2}] &= E[\frac{\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}}{n - 1}]\newline
        &= \frac{1}{n-1} \sum_{i=1}^{n} E[(X_{i} - \overline{X})^{2}]
        = \frac{1}{n-1} \sum_{i=1}^{n} E[X_{i}^{2} - 2X_{i} \overline{X} + \overline{X}^{2}]\newline
        &= \frac{1}{n-1} \big( \sum_{i=1}^{n} E[X_{i}^{2}] - E[2\overline{X} \sum_{i=1}^{n}X_{i}] + \sum_{i=1}^{n}E[\overline{X}^{2}] \big)\newline
        &= \frac{1}{n-1} \big( \sum_{i=1}^{n} E[X_{i}^{2}] - E[2n\overline{X}^{2}] + nE[\overline{X}^{2}] \big)\newline
        \text{Using}\quad E[X^{2}] &= Var(X) + E[X]^{2},\newline
        E[S^{2}] &= \frac{1}{n-1} \big( \sum_{i=1}^{n} E[Var(X_{i}) + E[X_{i}]^{2}] - nE[\overline{X}^{2}] \big)\newline
        &= \frac{1}{n-1}(n\sigma^{2} + n\mu^{2} - n(\frac{\sigma^{2}}{n} + \mu^{2}))\newline
        E[S^{2}] &= \sigma^{2}
    \end{align}
i.e., the mean of the sample variance is same as the variance of the distribution (population variance). Further, the division by $n-1$ to calculate sample variance comes from the fact that we are already using $\overline{X}$ as an estimate for sample mean which takes away one degree of freedom.

---
title: "Inferences Concerning Coefficients"
---

## Inferences Concerning Coefficients

We are most interseted in checking whether a coefficient has an effect or not
\begin{align}
        H_{0}: \theta_{1} = 0 \quad \text{versus} \quad H_{1}: \theta_{1} \neq 0
    \end{align}

We know from above derivations that
\begin{align}
        \frac{\hat{\theta}\_{1} - \theta_{1}}{\sigma^{2} / S_{xx}} \sim \mathcal{N}(0, 1)\newline
        \frac{SS_{R}}{\sigma^{2}} \sim \chi_{n-2}^{2}
    \end{align}
and both the random variables are independent of each other. Hence their division is t-distributed random variable and when $H_{0}$ is true, $\theta_{1} = 0$
\begin{align}
        \frac{\sqrt{S_{xx}}\hat{\theta}\_{1}/\sigma}{\sqrt{\frac{SS_{R}}{\sigma^{2} (n-2)}}} = \hat{\theta}\_{1}\sqrt{\frac{(n-2)S_{xx}}{SS_{R}}} = TS \sim t_{n-2}
    \end{align}
We do this since we do not know the exact value of $\sigma^{2}$ and need to eliminate it with a sample derived version. The hypothesis test at significance level $\alpha$ simply becomes
\begin{align}
{4}
        \text{Reject\quad} &H_{0} \text{\quad if \quad} &\lvert TS \rvert &> &t_{\alpha/2, n-2}\newline
        \text{Accept\quad} &H_{0} \text{\quad if\quad} &\vert TS \rvert &\leq &t_{\alpha/2, n-2}
    \end{align}
which can be converted to a *p-value* using the $TS$ and t-distribution. A small *p-value* will lead to rejection of $H_{0}$ meaning that the data provides evidence of a relationship between dependent and independent variables.


A confidence interval for $\theta_{1}$ at $1-\alpha$ confidence can be obtained as follows
\begin{align}
        P(-t_{\alpha/2, n-2} < (\hat{\theta}\_{1} - \theta_{1})\sqrt{\frac{(n-2)S_{xx}}{SS_{R}}} < t_{\alpha/2, n-2}) = 1-\alpha\newline
        \text{Confidence Interval is} \quad \bigg(\hat{\theta}\_{1} - t_{\alpha/2, n-2}\sqrt{\frac{SS_{R}}{(n-2)S_{xx}}} < \theta_{1} < \hat{\theta}\_{1} + t_{\alpha/2, n-2}\sqrt{\frac{SS_{R}}{(n-2)S_{xx}}} \bigg)
    \end{align}

The hypothesis test for $\theta_{0}$ can be done in the exact same manner as $\theta_{1}$ by considering the following test statistic
\begin{align}
        TS = (\hat{\theta}\_{1} - \theta_{1})\sqrt{\frac{n(n-2)S_{xx}}{(\sum_{i=1}^{n} x_{i}^{2})SS_{R}}} \sim t_{n-2}
    \end{align}


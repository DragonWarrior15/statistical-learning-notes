---
title: "Inferences Concerning Future Response"
---

## Inferences Concerning Future Response

The previous section discussed the distribution of the mean response. In many scenarios, we are interested in the distribution of the actual response $Y$ at input $x_{0}$, which takes the noise into account as well. We note
\begin{align}
        Y_{0} &\sim \mathcal{N}(\theta_{0} + \theta_{1}x_{0}, \sigma^{2})\newline
        \hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0} &\sim \mathcal{N}\bigg(\theta_{0} + \theta_{1}x_{0}, \sigma^{2} \bigg[ \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg]\bigg)\newline
        Y_{0} - \hat{\theta}\_{0} - \hat{\theta}\_{1}x_{0} &\sim \mathcal{N}\bigg(0, \sigma^{2}\bigg( 1 + \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg)\bigg)
    \end{align}

Now we utilise the distribution of $SS_{R}$ to eliminate $\sigma^{2}$ and get to the t-distribution
\begin{align}
        \frac{Y_{0} - \hat{\theta}\_{0} - \hat{\theta}\_{1}x_{0}}{\sigma\sqrt{1 + \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}}}} \div \sqrt{\frac{SS_{R}}{(n-2)\sigma^{2}}} \sim t_{n-2}
    \end{align}
and the **prediction** interval for the response (not mean response is) at $1-\alpha$ confidence
\begin{align}
        (\hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}) \pm t_{\alpha/2, n-2} \sqrt{\bigg( 1+ \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg) \bigg( \frac{SS_{R}}{n-2}\bigg)}
    \end{align}

Note that **prediction interval is the interval where we expect the value of a random variable to lie, whereas the confidence interval is the one where the value of a parameter estimate to lie.**


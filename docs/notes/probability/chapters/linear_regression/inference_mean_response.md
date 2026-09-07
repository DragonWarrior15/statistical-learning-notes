# Inferences Concerning Mean Response

## Inferences Concerning Mean Response

For any new point $x_{0}$, the unbiased estimator for the response is

$$
\begin{aligned}
        y_{0} &= \hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}\newline
        E[y_{0}] &= E[\hat{\theta}\_{0}] + E[\hat{\theta}\_{1}]E[x_{0}] = \theta_{0} + \theta_{1}x_{0}
    \end{aligned}
$$

To get the distribution of this mean response, note that

$$
\begin{aligned}
        Y_{0} &= \hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0} = \overline{Y} - \hat{\theta}\_{1}\bar{x} + \hat{\theta}\_{1}x_{0}\newline
        &= \frac{1}{n}\sum_{i=1}^{n} Y_{i} + (x_{0} - \bar{x})\frac{\sum_{i=1}^{n} (x_{i} - \bar{x})Y_{i}}{\sum_{i=1}^{n} (x-\bar{x})^{2}}\newline
        &= \sum_{i=1}^{n} \bigg( \frac{1}{n} + \frac{(x_{i} - \bar{x})(x_{0} - \bar{x})}{S_{xx}} \bigg)Y_{i}
    \end{aligned}
$$

which is a linear combination of independent normally distributed random variables $Y_{i}s$. Thus, the mean response is also a normally distributed random variable and we can get the confidence intervals by considering the mean and variance of this random variable

$$
\begin{aligned}
        Var(\hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}) &= \sum_{i=1}^{n} \bigg( \frac{1}{n} + \frac{(x_{i} - \bar{x})(x_{0} - \bar{x})}{S_{xx}} \bigg)^{2}Var(Y_{i})\newline
        \hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0} &\sim \mathcal{N}\bigg(\theta_{0} + \theta_{1}x_{0}, \sigma^{2} \bigg[ \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg]\bigg)
    \end{aligned}
$$

To eliminate $\sigma^{2}$,

$$
\begin{aligned}
        SS_{R}/\sigma^{2} \sim \chi_{n-2}^{2}\newline
        \frac{(\hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}) - (\theta_{0} + \theta_{1}x_{0})}{\sigma^{2} \bigg[ \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg]} \div \sqrt{\frac{SS_{R}}{(n-2)\sigma^{2}}} \sim t_{n-2}
    \end{aligned}
$$

and the confidence intervals for confidence $1-\alpha$ become

$$
\begin{aligned}
        (\hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}) \pm t_{\alpha/2, n-2} \sqrt{\bigg( \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg) \bigg( \frac{SS_{R}}{n-2}\bigg)}
    \end{aligned}
$$


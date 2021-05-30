---
title: "Mean and Variance of Coefficients"
---

## Mean and Variance of Coefficients

First note that
\begin{align}
        E[Y_{i}] = E[\theta_{0} + \theta_{1}X_{i} + W_{i}] = \theta_{0} + \theta_{1}X_{i}\newline
        E[\overline{Y}] = (\sum_{i=1}^{n} E[Y_{i}])/n = \theta_{0} + \theta_{1}\overline{X}\newline
        Var(Y_{i}) = \sigma_{2}
    \end{align}
Thus,
\begin{align}
        E[\hat{\theta}\_{1}] &= E\bigg[ \frac{\sum_{i=1}^{n} (x_{i} - \overline{x}) (Y_{i} - \overline{Y})}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg]\newline
        &= E\bigg[ \frac{\sum_{i=1}^{n} (x_{i} - \overline{x}) (E[Y_{i}] - E[\overline{Y}])}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg]\newline
        &= \theta_{1}\newline
        E[\hat{\theta}\_{0}] &= E[\overline{Y} - \hat{\theta_{1}} \bar{x}] = \theta_{0}
    \end{align}
meaning that our estimates of the parameters are unbiased and their error will equal the variance
\begin{align}
        Var(\hat{\theta}\_{1}) &= Var \bigg( \frac{\sum_{i=1}^{n} (x_{i} - \overline{x}) (Y_{i} - \overline{Y})}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg)
        = Var \bigg( \frac{\sum_{i=1}^{n} (x_{i} - \overline{x})Y_{i}}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg)\newline
        &= \frac{1}{(\sum_{i=1}^{n}(x_{i} - \overline{x})^{2})^{2}} \sum_{i=1}^{n} (x_{i} - \overline{x})^{2} Var(Y_{i})
        = \frac{\sigma^{2}}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}}\newline
        Var(\hat{\theta}\_{0}) &= Var(\overline{Y} - \hat{\theta_{1}} \bar{x})
        = Var \bigg( \sum_{i=1}^{n} \bigg( \frac{1}{n} - \frac{\bar{x}(x_{i} - \bar{x})}{\sum_{i=1}^{n}(x_{i} - \bar{x})^{2}} \bigg) \bigg)\newline
        &= \frac{\sigma^{2}}{n^{2}} \bigg( \sum_{i=1}^{n} \bigg( \frac{\sum_{i=1}^{n}x_{i}^{2} - n\bar{x}x_{i}}{\sum_{i=1}^{n}x_{i}^{2} - n\bar{x}^{2}} \bigg)^{2} \bigg)
        = \frac{\sigma^{2}}{n^{2} (\sum_{i=1}^{n}x_{i}^{2} - n\bar{x}^{2})^{2}} (n(\sum_{i=1}^{n})^{2} - n^{2}\bar{x}^{2}(\sum_{i=1}^{n})^{2})\newline
        &= \sigma^{2} \frac{\sum_{i=1}^{n} x_{i}^{2}}{n\big((\sum_{i=1}^{n} x_{i}^{2}) - n\bar{x}^{2} \big)}
    \end{align}
because both the estimators are linear combinations of independent identically distributed normal random variables $Y_{i}s$, and the variance of linear combination of independent random variables is simply the sum of variances multiplied by squares of coefficients.


Thus, **$\hat{\theta_{0}}$ and $\hat{\theta}\_{1}$ are both normally distributed random variables.** with the following distributions

\begin{align}
        \hat{\theta}\_{1} &\sim \mathcal{N}\bigg(\theta_{1}, \frac{\sigma^{2}}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg)\newline
        \hat{\theta}\_{0} &\sim \mathcal{N}\bigg(\theta_{0}, \sigma^{2} \frac{\sum_{i=1}^{n} x_{i}^{2}}{n\big((\sum_{i=1}^{n} x_{i}^{2}) - n\bar{x}^{2} \big)} \bigg)
    \end{align}

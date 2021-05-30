---
title: "Simple Linear Regression"
---

## Simple Linear Regression

Here, the independent variable is assumed to have a single dimension, and thus we are only looking towards estimating two coefficients. Let $x_{i}$ be the $i^{th}$ observation and $Y_{i}$ be the associated response, then
\begin{gather}
    \hat{Y}\_{i} = \hat{\beta}\_{0} + \hat{\beta}\_{1}x_{i}\newline
    \text{Minimize error to estimate coefficients} \quad \minimize_{\beta_{0}, \beta_{1}} \sum_{i=1}^{n} (y_{i} - \beta_{0} - \beta_{1}x_{i})^{2}\newline
    \hat{\beta}\_{1} = \frac{\sum_{i=1}^{n}(x_{i} - \bar{x})(Y_{i} - \overline{Y})}{\sum_{i=1}^{n} (x_{i} - \bar{x})^{2}}, \quad \hat{\beta}\_{0} = \overline{Y} - \hat{\beta}\_{1}\bar{x}\newline
    \hat{\theta}\_{1} \sim \mathcal{N}\bigg(\theta_{1}, \frac{\sigma^{2}}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg)\newline
    \hat{\theta}\_{0} \sim \mathcal{N}\bigg(\theta_{1}, \sigma^{2} \frac{\sum_{i=1}^{n} x_{i}^{2}}{n\big((\sum_{i=1}^{n} x_{i}^{2}) - n\bar{x}^{2} \big)} \bigg)
\end{gather}

The mean squared error is used here as it is the natural error function that emerges when we try to obtain MLE estimates of the coefficients. As is visible from the fomulae for point estimates of coefficients, they are linear combinations of normal variables ($Y$) and thus are normally distributed.

Simple linear regression is discussed in detail in the probability notes on this site. It also discusses confidence intervals for the coefficients, the prediction intervals for the response and hypothesis testing for relation between input and response.


### Coefficient of Determination

$R^{2}$ is often used as a metric for checking how good the regression model is. It's definition is invariant to the number of independent variables
\begin{gather}
    R^{2} = \frac{S_{YY} - RSS}{S_{YY}} = 1 - \frac{RSS}{S_{YY}}\newline
    S_{YY} = \text{total variance in Y, }\quad RSS = \text{sum of squares of residuals}\newline
    S_{YY} - RSS = \text{total variance explained by inputs}
\end{gather}
A good model will explain most of the variance in $Y$ usig the input variables. Hence, $R^{2}$ close to $1$ is a good model and vice versa. **$R^{2}$ usually increases as more and more variables are added to the model**.

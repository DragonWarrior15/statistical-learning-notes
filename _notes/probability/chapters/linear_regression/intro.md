---
title: "Linear Regression"
---

# Linear Regression

We are given pairs of data $(x_{1},y_{1}), (x_{2},y_{2}), \ldots, (x_{n},y_{n})$ (all independent) where we assume that $x$ and $y$ are governed by the linear relation
\begin{align}
        y \approx \theta_{0} + \theta_{1}x
    \end{align}
The aim is to determine the model which is parametric consisting of two parameters $\theta_{0}$ and $\theta_{1}$. We find it using the least squares estimate, i.e., minimizing
\begin{align}
        \minimize_{\theta_{0}, \theta_{1}} \sum_{i=1}^{n} (y_{i} - \theta_{0} - \theta_{1}x)^{2}
    \end{align}
The true model also includes noise and is given by
\begin{align}
        Y_{i} = \theta_{0} + \theta_{1}X_{i} + W_{i}
    \end{align}
where we assume the noise $W_{i} \sim \mathcal{N}(0, \sigma^{2})$ and is independently and identically distributed. Observing some $X$ and $Y$ is same as observing the noise.
\begin{align}
        P(X=x,Y=y) &= P(W=y-\theta_{0}-\theta_{1}x) = \frac{1}{\sqrt{2\pi \sigma_{2}}} \exp\bigg(-\frac{(y-\theta_{0}-\theta_{1}x)^{2}}{2 \sigma^{2}}\bigg)\newline
        P(X_{1}=x_{1},Y_{1}=y_{1}, \ldots, X_{n}=x_{n},Y_{n}=y_{n}) &= \prod_{i=1}^{n} P(X_{1}=x_{i},Y_{i}=y_{i})\newline
        &= \prod_{i=1}^{n} W_{i} = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma_{2}}} \exp\bigg(-\frac{(y_{i}-\theta_{0}-\theta_{1}x_{i})^{2}}{2\sigma^{2}}\bigg)
    \end{align}
Maximizing the above product is maximizing the likelihood of the occurrence of the data under the model parameters $\theta_{0}$ and $\theta_{1}$. Since taking log will not change the maxima, we usually maximize the log likelihood
\begin{align}
        \maximize_{\theta_{0}, \theta_{1}} \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^{2}}} \exp(-\frac{(y_{i}-\theta_{0}-\theta_{1}x_{i})^{2}}{2\sigma^{2}}) = \minimize_{\theta_{0}, \theta_{1}} \sum_{i=1}^{n} (y_{i}-\theta_{0}-\theta_{1}x_{i})^{2}
    \end{align}

We can take derivatives with respect to the parameters of the above function to get the estimate for the parameters as
\begin{align}
        \bar{x} &= \frac{1}{n} \sum_{i=1}^{n} x_{i} \text{,}\quad \bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_{i}\newline
        \hat{\theta}\_{1} &= \frac{\sum_{i=1}^{n} (x_{i} - \bar{x}) (y_{i} - \bar{y})}{\sum_{i=1}^{n}(x_{i} - \bar{x})^{2}} = \frac{E[(X-\overline{X})(Y-\overline{Y})]}{E[(X-\overline{X})^{2}]} = \frac{Cov(X,Y)}{Var(X)}\newline
        \hat{\theta}\_{0} &= \bar{y} - \hat{\theta_{1}} \bar{x}
    \end{align}

The above formulae can also be derived if the additives are a function of $X$. Since the linear relationship will still be respected and the loglikelihood can be maximized to get the estimates of the parameters.


Some useful notation
\begin{align}
{2}
        S_{xY} &= \sum_{i=1}^{n} (x_{i} - \bar{x})(Y_{i} - \overline{Y}) &= (\sum_{i=1}^{n}x_{i}Y_{i}) - n\bar{x}\overline{Y}\newline
        S_{xx} &= \sum_{i=1}^{n} (x_{i} - \bar{x})^{2} &= (\sum_{i=1}^{n} x_{i}^{2}) - n\bar{x}^{2}\newline
        S_{YY} &= \sum_{i=1}^{n} (Y_{i} - \overline{Y})^{2} &= (\sum_{i=1}^{n} Y_{i}^{2}) - n\overline{Y}^{2}
    \end{align}

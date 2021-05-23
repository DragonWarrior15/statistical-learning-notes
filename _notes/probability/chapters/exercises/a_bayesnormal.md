---
title: "Answer"
---

We first begin by calculating the posterior of $\theta$ given observations
\begin{align}
        f(\theta \vert X_{1}, X_{2}, \ldots, X_{n}) &= \frac{f(X_{1}, X_{2}, \ldots, X_{n} \vert \theta)p(\theta)}{\int f(X_{1}, X_{2}, \ldots, X_{n} \vert \theta)p(\theta) d\theta}\newline
        f(X_{1}, X_{2}, \ldots, X_{n} \vert \theta) &= \frac{1}{\sqrt{2 \pi \sigma_{0}^{2}}} exp \left(-\frac{\sum_{i=1}^{n} (X_{i} - \theta)^{2}}{2\sigma_{0}^{2}} \right)\newline
        p(\theta) &= \frac{1}{\sqrt{2 \pi \sigma^{2}}} exp \left(-\frac{(\theta - \mu)^{2}}{2\sigma^{2}} \right)\newline
        f(X_{1}, X_{2}, \ldots, X_{n} \vert \theta)p(\theta) &= \frac{1}{2 \pi \sigma_{0} \sigma} exp \left(-\frac{\sum_{i=1}^{n} (X_{i} - \theta)^{2}}{2\sigma_{0}^{2}} -\frac{(\theta - \mu)^{2}}{2\sigma^{2}} \right)\newline
        \frac{\sum_{i=1}^{n} (X_{i} - \theta)^{2}}{2\sigma_{0}^{2}} +\frac{(\theta - \mu)^{2}}{2\sigma^{2}} &= \frac{\theta^{2}(\sigma_{0}^{2} + n\sigma^{2}) - 2\theta \left(\sigma_{0}^{2} \mu + \sigma^{2} \sum_{i=1}^{n} X_{i} \right) + \left(\sigma_{0}^{2} \mu^{2} + \sigma^{2} \sum_{i=1}^{n}X_{i}^{2} \right)}{2\sigma_{0}^{2}\sigma^{2}}\newline
        &= \frac{\left(\theta - \frac{\sigma_{0}^{2} \mu + \sigma^{2}\sum_{i=1}^{n} X_{i}}{\sigma_{0}^{2} + n\sigma^{2}}\right)^{2} + \left(\frac{\sigma_{0}^{2} \mu^{2} + \sigma^{2} \sum_{i=1}^{n}X_{i}^{2}}{\sigma_{0}^{2} + n\sigma^{2}} - \left(\frac{\sigma_{0}^{2} \mu + \sigma^{2}\sum_{i=1}^{n} X_{i}}{\sigma_{0}^{2} + n\sigma^{2}}\right)^{2}\right)}{(2\sigma_{0}^{2} \sigma^{2})/(\sigma_{0}^{2} + n\sigma^{2})}\newline
        f(X_{1}, X_{2}, \ldots, X_{n} \vert \theta)p(\theta) &= \left(\frac{1}{2\sigma_{0}\sigma}exp(\frac{\left(\frac{\sigma_{0}^{2} \mu^{2} + \sigma^{2} \sum_{i=1}^{n}X_{i}^{2}}{\sigma_{0}^{2} + n\sigma^{2}} - \left(\frac{\sigma_{0}^{2} \mu + \sigma^{2}\sum_{i=1}^{n} X_{i}}{\sigma_{0}^{2} + n\sigma^{2}}\right)^{2}\right)}{2\sigma_{0}^{2} \sigma^{2})/(\sigma_{0}^{2} + n\sigma^{2})}\right)\times\newline
        &\left(\frac{1}{\sqrt{2\pi(2\sigma_{0}^{2} \sigma^{2})/(\sigma_{0}^{2} + n\sigma^{2})}}exp\left(-\frac{\left(\theta - \frac{\sigma_{0}^{2} \mu + \sigma^{2}\sum_{i=1}^{n} X_{i}}{\sigma_{0}^{2} + n\sigma^{2}}\right)^{2}}{2\sigma_{0}^{2} \sigma^{2}/(\sigma_{0}^{2} + n\sigma^{2})}\right)\right)\newline
        &= C \times \mathcal{N}\left(\frac{\sigma_{0}^{2} \mu + \sigma^{2}\sum_{i=1}^{n} X_{i}}{\sigma_{0}^{2} + n\sigma^{2}}, \frac{2\sigma_{0}^{2} \sigma^{2}}{\sigma_{0}^{2} + n\sigma^{2}}\right)\newline
        f(\theta \vert X_{1}, X_{2}, \ldots, X_{n}) &= \frac{C \times \mathcal{N}\left(\frac{\sigma_{0}^{2} \mu + \sigma^{2}\sum_{i=1}^{n} X_{i}}{\sigma_{0}^{2} + n\sigma^{2}}, \frac{2\sigma_{0}^{2} \sigma^{2}}{\sigma_{0}^{2} + n\sigma^{2}}\right)}{C \times \int_{-\infty}^{\infty} \mathcal{N}\left(\frac{\sigma_{0}^{2} \mu + \sigma^{2}\sum_{i=1}^{n} X_{i}}{\sigma_{0}^{2} + n\sigma^{2}}, \frac{2\sigma_{0}^{2} \sigma^{2}}{\sigma_{0}^{2} + n\sigma^{2}}\right) d\theta}\newline
        &= \mathcal{N}\left(\frac{\sigma_{0}^{2} \mu + \sigma^{2}\sum_{i=1}^{n} X_{i}}{\sigma_{0}^{2} + n\sigma^{2}}, \frac{2\sigma_{0}^{2} \sigma^{2}}{\sigma_{0}^{2} + n\sigma^{2}}\right)\newline
        &= \mathcal{N}\left(\frac{\sigma_{0}^{2} \mu + n\sigma^{2}\overline{X}}{\sigma_{0}^{2} + n\sigma^{2}}, \frac{2\sigma_{0}^{2} \sigma^{2}}{\sigma_{0}^{2} + n\sigma^{2}}\right)
    \end{align}
since the integral of a normal over the entire domain is equal to the total probability which is 1. Thus, the new estimate of the mean is the weighted sum of the prior mean and the estimated mean from the observations, with the weights being proportional to the inverse of the standard deviations. The new standard deviation is also the geometric mean of the original standard deviations.

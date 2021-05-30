---
title: "Exercises"
---

# Exercises

## Questions

1.  Consider the random walk with drift model
    \begin{align}
            x_{t} = \delta + x_{t-1} + w_{t}
        \end{align}
    for $t = 1,2,\ldots$ with $x_{0} = 0$ and $w_{t}$ is white noise with variance $\sigma_{w}^{2}$.

    1.  Show that the model can be written as $x_{t} = \delta t + \sum_{k=1}^{t}\sigma_{w}^{k}$.

    2.  Find the mean and autocovariance of $x_{t}$. Comment on the stationarity.

    3.  Show $\rho_{x}(t-1,t) = \sqrt{(t-1)/t}$ which converges as $t\rightarrow \infty$.

    4.  Suggest a transformation to make the series stationary and prove stationarity of the new series.

2.  Consider a periodic time series expressed as
    \begin{align}
            x_{t} = U_{1}sin(2\pi \omega_{0}t) + U_{2}cos(2\pi \omega_{0}t)
        \end{align}
    where $U_{1}$ and $U_{2}$ are independent random variables with $0$ mean and variances $\sigma^{2}$ each. Compute the mean and autocovariance function of $x_{t}$.

## Soluitons

1.  Note that $E[w_{t}] = 0$, $E[w_{t}^{2}] = \sigma_{w}^{2}$ and $E[w_{s}w_{t}] = 0$ for all $s \neq t$

    1.  We use the recursive definition of the series
        \begin{align}
                     x_{t} = \delta + \bigg( \delta + x_{t-2} + w_{t-1} \bigg) + w_{t}
                \end{align}
        Continuing the expansion will yield
        \begin{align}
                    x_{t} = \delta t + x_{0} + \sum_{k=1}^{t}w_{k} = \delta t + \sum_{k=1}^{t}w_{k}
                \end{align}

    2.  \begin{align}
                    E[x_{t}] &= E[\delta t] + \sum_{k=1}^{t} E[w_{k}] = \delta t\newline
                    E[x_{t}^{2}] &= E[(\delta t + \sum_{k=1}^{t}w_{k})^{2}]\newline
                    &= \delta^{2}t^{2} + t\sigma_{w}^{2}\newline
                    E[x_{t+h}x_{t}] &= E[(\delta (t+h) + \sum_{k=1}^{t+h}w_{k})(\delta t+ \sum_{k=1}^{t+h}w_{k})]\newline
                    &= \delta^{2}t(t+h) + \min(t,t+h)\sigma_{w}^{2}\newline
                    \gamma(t+h,t) &= E[x_{t+h}x_{t}] - \mu_{t+h}\mu_{t}\newline
                    &= \min(t,t+h)\sigma_{w}^{2} = \sigma_{w}^{2}(t + \min(0,h))\newline
                    \gamma(t,t) &= t\sigma_{w}^{2}
                \end{align}
        making both mean and auto covariance functions of time. This implies non stationarity.

    3.  \begin{align}
                    \rho(t-1,t) &= \frac{\gamma(t-1,t)}{\sqrt{\gamma(t-1,t-1) \gamma(t,t)}} = \frac{(t-1)\sigma_{w}^{2}}{\sqrt{(t-1)\sigma_{w}^{2} t \sigma_{w}^{2}}}\newline
                    &= \sqrt{\frac{t-1}{t}} \to 1 \;\text{as}\; t \to \infty
                \end{align}

    4.  The simplest transformation to make a stationary series will be
        \begin{align}
                    y_{t} &= x_{t} - x_{t-1}\newline
                    E[y_{t}] &= E[x_{t}] - E[x_{t-1}] = \delta\newline
                    \gamma(t+h,t) &= E[y_{t+h}y_{t}] - E[y_{t+h}]E[y_{t}]\newline
                    &= E[(x_{t+h} - x_{t+h-1})(x_{t} - x_{t-1})] - \delta^{2}\newline
                    &= E[x_{t+h}x_{t} - x_{t+h}x_{t-1} - x_{t+h-1}x_{t} + x_{t+h-1}x_{t-1}] - \delta^{2}\newline
                    &= \delta^{2} \bigg [ t(t+h) - (t+h)(t-1) - (t+h-1)t \newline&+ (t+h-1)(t-1) - 1 \bigg] + \sigma_{w}^{2} \bigg[\min(t,t+h) - \min(t+h,t-1) \newline&- \min(t+h-1,t) + \min(t+h-1,t-1) \bigg] \;(\text{from sub-answer 2}) \newline
                    &= \sigma_{w}^{2} \bigg[2\min(0,h) - \min(h+1,0) - \min(h-1,0) \bigg]\newline
                    \gamma(t+h,t) &= \begin{cases} \sigma_{w}^{2} &\mbox{$h = 0$}\newline
                    0 &\mbox{otherwise} \end{cases}
                \end{align}
        making expectation constant and the autocovariance only a function of lag and not time. Thus, the transformed series is stationary

2.  We use the definitions to calculate mean and autocovariance

    1.  Mean
        \begin{align}
                    E[x_{t}] &= E[U_{1}] sin(2\pi \omega_{0}t) + E[U_{2}] cos(2\pi \omega_{0}t)= 0
                \end{align}

    2.  Autocovariance
        \begin{align}
                    E[U_{1}^{2}] &= Var(U_{1}) + E[U_{1}]^{2} = \sigma^{2} = E[U_{2}^{2}]\newline
                    E[U_{1}U_{2}] &= E[U_{1}]E[U_{2}] = 0 \; (\text{independence})\newline
                    \gamma(h) &= E[(x_{t+h} - E[x_{t+h}])(x_{t} - E[x_{t}])] = E[x_{t+h}x_{t}]\newline
                    &= E[U_{1}U_{2}]f(t,h) + E[U_{1}^{2}]sin(2\pi\omega_{0}(t+h))sin(2\pi\omega_{0}t) \newline&+ E[U_{2}^{2}]sin(2\pi\omega_{0}(t+h))sin(2\pi\omega_{0}t)\newline
                    &= \sigma^{2}cos(2\pi\omega_{0}(t+h) - 2\pi\omega_{0}t) = \sigma^{2}cos(2\pi\omega_{0}h)
                \end{align}
        which implies the series is at least weakly stationary

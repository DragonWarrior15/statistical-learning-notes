---
title: "Smoothing in Time Series"
---

# Smoothing in Time Series

### Moving Average Smoothing

Here we take a moving average of the time series in order to remove some of the noise. This can be handy to observe trends or seasonality in a time series that might otherwise be lost in the noise.
\begin{align}
    M_{t} &= \sum_{i=-k}^{k}a_{i}X_{t+i}\newline
    \text{with} \; \sum_{i=-k}^{k}a_{i} &= 1\end{align}
which becomes a symmetric filter with $a_{j} = a_{-j}$. All the weights in this equation are positive. The more values we average together, the closer to a flat line the resulting series will become.

### Kernel Smoothing

The idea is similar to above but using a distance based kernel
\begin{align}
    M_{t} &= \sum_{i=1}^{n}w_{i}X_{i}\newline
    w_{i} &= \frac{K(t-i)}{\sum_{j=1}^{n}K(t-j)}\newline
    K(z) &= \frac{1}{\sqrt{2\pi\sigma^{2}}}exp(-\frac{1}{2\sigma^{2}}z^{2}) \; \text{for gaussian kernel}\end{align}

### Lowess or Nearest Neighbor Regression

The idea is similar to neares neighbors regression, but here when looking at $k$ neighbors, we consider all the points to the left and right of current point at distance $k/2$. We will use these points to build a regression equation and the prediction will be our $M_{t}$. Clearly, the more neighbors we include in the regression, the smoother will be the fit.

### Smoothing Splines

This approach is very similar to regression splines. The prediction is made as
\begin{align}
    M_{t} = \beta_{0} + \beta_{1}t + \beta_{2}t^{2} + \beta_{3}t^{3}\end{align}
in the case of a cubic polynomial. The usual approach to solve this would be to first divide the entire data into $k+1$ intervals using $k$ knots (points chosen from the dataset), and fit separate cubic polynomials on each of the intervals, maintaining constraints like continuity and differentiability at the knots. This method gives us the cubic splines.

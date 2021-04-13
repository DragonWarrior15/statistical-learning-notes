---
title: "Simple Exponential Smoothing - Introduction"
---

# Simple Exponential Smoothing

ARIMA models are good to understand the underlying structure of the time series. But often, we are interested in just forecasting the values of the time series for the near future. Some very basic methods can be to

-   Naive method: forecast the same value as the last known time step.

-   Average method: Forecast the average of the last few values/all available values.

These naive methods rarely give good results in practice and we resort to slightly more advanced techniques to get good results.


Lets define some notations
\begin{align}
    x_{n+h|n} &= \text{forecast for step $n+h$ using data available at $n$}\newline
    x_{n+1|n} &= x_{n} \quad \text{Naive method}\newline
    x_{n+1|n} &= \frac{1}{n} \sum_{i=1}^{n}x_{i}\end{align}

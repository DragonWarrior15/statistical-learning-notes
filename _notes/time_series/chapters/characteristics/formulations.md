---
title: "Time Series Formulations"
---

# Time Series Formulations

## White Noise

The simplest time series is just a series of uncorrelated variables. It has three flavours

1.  white noise $w_{t} \sim wn(0, \sigma_{w}^{2})$

2.  white independent noise $w_{t} \sim iid(0, \sigma_{w}^{2})$

3.  Gaussian white noise $w_{t} \sim iid \mathcal{N}(0, \sigma_{w}^{2})$

Just the noise is particularly difficult to model and we introduce some kind of correlation and smoothness into the model.

## Moving Average and Filtering

Any time series can be smoothed by considering moving averages. A very simple example can be taking the average of three consecutive observations
\begin{align}
    v_{t} = \frac{1}{3}(x_{t-1} + x_{t} + x_{t+1})\end{align}
Care must be taken to ensure that the sum of the coefficients of all the terms is one.


As is evident, if we take more number of such terms, the slower oscillations become more prominent in comparison to the faster oscillations making moving averages work as a kind of **filter**.

## Autoregression

This involves using a regression like function to predict the value of the time series at the current timestep. A simple example would be
\begin{align}
    x_{t} = x_{t-1} + 0.9x_{t-2} + w_{t}\end{align}
where $w_{t}$ is noise. Here we are using the observations from the last two timesteps to make our predictions. This idea can be extended to include more terms and even difference of terms as part of the equation. We make an assumption for some initial values to calculate $x_{1}$ and $x_{2}$.

## Random Walk with Drift

The prediction function can be defined as
\begin{align}
    x_{t} &= \delta + x_{t-1} + w_{t}\newline
    x_{t} &= \delta t + \sum_{t} w_{t}\end{align}
where $\delta$ is the drift. Setting $\delta = 0$ is same as a random walk.

## Signal in Noise

Sometimes, the signal can be seen as having a periodic component with some noise
\begin{align}
    x_{t} = A\cos (2\pi \omega t + \phi) + w_{t}\end{align}
where $\phi$ is the phase or the offset of the signal, $\omega$ is the time period and $A$ is the amplitude. $w_{t}$ is noise that we cannot predict.


Let $\sigma_{w}$ denote the variance of the noise. Then, **signal-to-noise ratio** is the ratio of the amplitude of the signal to the variance of noise. The higher this quantity, the easier it is to detect the signal. In real data, the signal is always obscured by some noise.

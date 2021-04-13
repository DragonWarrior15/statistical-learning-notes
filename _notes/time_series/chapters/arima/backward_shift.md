---
title: "Backward Shift Operators"
---

# ARIMA
# Backward Shift Operators

This is a very useful notation in the analysis of time series, especially ARIMA models. A single backward shift operator denotes the time series with a single lag
\begin{align}
    BX_{t} = X_{t-1}\end{align}
where $X$ is the random variable denoting the time series. We can recursively apply this operator to get
\begin{align}
    B^{2}X_{t} &= BX_{t-1} = X_{t-2}\newline
    B^{k}X_{t} &= X_{t-k}\end{align}

This operator can be used in time series analysis to create polynomial like functions to convert from one time series to another.
\begin{align}
    X_{t} &= Z_{t} + \theta_{1}Z_{t-1} + \theta_{2}Z_{t-2}\newline
    &= Z_{t} + \theta_{1}BZ_{t} + \theta_{2}B^{2}Z_{t}\newline
    &= (1 + \theta_{1}B + \theta_{2}B^{2})Z_{t}\end{align}

An inverse of this operator also exists such that
\begin{align}
    B^{-1}B &= 1\newline
    B^{-1}X_{t-1} &= X_{t}\end{align}
where $B^{-1}$ is called the **forward shift operator**.


To make time series analysis easier, it is often the case that we will take difference of successive terms in order to induce the stationarity conditions. We conveniently define the **Differencing operator** as
\begin{align}
    \nabla X_{t} &= (1-B)X_{t} = X_{t} - X_{t-1}\newline
    \nabla^{2}X_{t} &= (1-B)^{2}X_{t} = (1 - 2B + B^{2})X_{t}\newline
    \nabla^{2}X_{t} &= \nabla(\nabla X_{t}) = \nabla(X_{t} - X_{t-1})\newline
    &= (X_{t} - X_{t-1}) - (X_{t-1} - X_{t-2}) = X_{t} - 2BX_{t} + B^{2}X_{t}\newline
    \nabla^{d}X_{t} &= (1-B)^{d}X_{t} \numberthiseqn\label{eq:eq_arima_1}\end{align}
which illustrates how we can use the differencing operator to obtain successive differences. Higher powers of this operator can be expanded algebraically using the last equation.


Differencing is a technique frequently used to make the time series stationary. Usually a difference of order 1 or 2 suffices. In some cases, we may need to remove the seasonal trend in which case we will resort to order $m$ difference where $m$ is the length of a seasonal cycle.

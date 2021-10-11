---
title: "Parameter Estimation"
---

# Parameter Estimation

In probability theory, we usually have the distribution known to us and we try to use this information to obtain theoretical results applicable on population of this distribution. However, in statistics, we are given the samples drawn from the population, and we are interested in estimating the parameters of this population. For instance, it can be known that the samples are drawn from a normal distribution and the objective is to use the samples to obtain the mean and variance of the normal distribution. It is possible to partially know the parameters in some cases, for example mean is unknown but the variance is known. Following are some methods to obtain the *estimates* of these parameters.

Since the samples some from the same population, they are identically distributed. We also assume that they are independently drawn. Hence, the samples are independent identically distrubted or i.i.d.

## Statistic
For the drawn sample $X_{1}, \ldots, X_{n}$, let $T = T(X_{1}, \ldots, X_{n})$ be a function of the sample. Then $T$ is called a **statistic**.

Once the sample is drawn, we use $x_{1}, \ldots, X_{n}$ to denote a realization of the statistic $T$.

For evaluating the value of $\theta$, it makes sense to consider $T(X_{1}, \ldots, X_{n})$ as an estimator of $\theta$. More formally, this $T$ is called a **point estimate** of $\theta$.

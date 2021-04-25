---
title: "Bayesian Methods"
---

# Bayesian Methods

The Bayes formula will be invaluable throughout the analysis of Bayesian methods in Machine Learning. Suppose we observe $N$ data points jointly represented by $X$ and we know that they come from a distribution with parameters $\theta$, then
\begin{align}
    P(\theta \vert X) = \frac{P(X \vert \theta)P(\theta)}{P(X)}\end{align}
where

* $P(\theta \vert X)$ is called the posterior, the probability distribution of $\theta$ having observed the data
* $P(X \vert \theta)$ is called the likelihood, the probability of occurence of the data under a given $\theta$
* $P(\theta)$ is called the prior, our prior beliefs about the parameters without seeing the data
* $P(X)$ is the probability distribution of the data which is fixed for a given data set

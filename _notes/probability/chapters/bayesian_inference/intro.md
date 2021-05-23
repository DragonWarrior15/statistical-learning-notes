---
title: "Bayesian Inference"
---

# Bayesian Inference

We have a signal $S$ that goes through a \"model\" $a$ through which we observe $X$ (with sum added noise $N$). The aim of Bayesian Inference is to try to infer $S$ given the observed $X$.


Hypothesis testing is done on an unknown that takes some possible values, and the aim is to arrive at a value that gives a small probability of incorrect decision (e.g. - Radar)


Estimation is aimed at finding the value of a quantity with a small estimation error (e.g. poll estimation)


Bayes Rule
\begin{align}
        p_{\Theta|X}(\theta|x) &= \frac{p_{\Theta}(\theta)p_{X|\Theta}(x|\theta)}{p_{X}(x)} \quad\text{$\theta$ and $X$ are both discrete}\newline
        \text{or,}\quad Posterior &= \frac{Prior * Model}{Data}\newline
        p_{\Theta|X}(\theta|x) &= \frac{p_{\Theta}(\theta)f_{X|\Theta}(x|\theta)}{f_{X}(x)} \quad\text{$\theta$ is discrete and $X$ is continuous}\newline
    \end{align}
Note that Bayesian inference will give us a distribution over the possible values, but it is often desirable to get an estimate.

## Maximum a Posteriori (MAP)

MAP is a point estimate of the unknown quantity and is defined as follows
\begin{align}
        p_{\Theta|X}(\theta|x) = \max_{\theta}p_{\Theta|X}(\theta|x) \quad\text{$\theta$ with maximum posterior probability}\newline
    \end{align}
In continuous case, expected value can be a better estimate

## Maximum Likelihood Estimation

This is another method to give estimates from the Bayesian Inference. We assume the random variable of interest to be generated through a model with some parameters, i.e. $X \sim p_{X}(x;\theta)$ and we pick the $\theta$ that makes the data most likely
\begin{align}
        \hat{\theta}\_{MLE} &= \argmax_{\theta} p_{X|\Theta}(x|\theta)\newline
        \hat{\theta}\_{MAP} &= \argmax_{\theta} p_{\Theta|X}(\theta|x)\newline
        &= \argmax_{\theta} p_{X|\Theta}(x|\theta)p_{\Theta}(\theta)
    \end{align}

Thus, we can see that if we assume a uniform prior on $\theta$, MAP and MLE estimates are the same. MLE estimates tha maximum through cosideration of multiple probabilistic models. We can get different estimates for different priors.

## Least Mean Square Estimate

Here, we aim to find an estimate such that
\begin{align}
        \theta^{\*} &= \min_{c} E[(\Theta - c)^{2}]\newline
        E[(\Theta - c)^{2}] &= E[\Theta^{2}] - 2cE[\Theta] + c^{2}\newline
        \text{Taking derivative,}\quad \frac{dE}{dc} &= 0\newline
        c &= E[\Theta]\newline
        \text{In general,}\quad c &= E[\Theta|X] \quad\text{minimizes $E[(\Theta - g(X))^{2}]$ over all estimators $g(X)$ }
    \end{align}
$E[\Theta]$ minimizes the least squares estimate


When $X$ is observed, the best estimate simply becomes $E[\Theta \vert X]$.

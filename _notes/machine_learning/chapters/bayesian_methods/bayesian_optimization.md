---
title: "Bayesian Optimization"
---

## Bayesian Optimization

In an optimization problem like finding the minima or maxima, methods like gradient descent will only work if we can compute the gradients. Random Search/Grid Search can work when it is cheap to obtain new data points so that we can repeatedly check for the optima.


Bayesian Optimization is useful when we want to fit a non parametric model on the data and also know about the uncertainities associated with such models. Such models are useful when obtaining a data point can be expensive (such as oil drilling coordinates) and we would like to obtain the optima in the least number of trials (such as drug discovery, oil drilling etc).


We work with two functions in Bayesian Optimization, $\hat{f}$ which is a cheap to compute alternative to $f$ and acquisition function $\mu$ which tells us which areas of the input space we should explore first. Gaussian Process are a nice fit for $\hat{f}$ since they also give us the uncertainity around the predictions which can be used in $\mu$.


Acquisition function will have a tradeoff between exploitation (search in areas with high value of $\hat{f}$) and exporation (search in areas with high uncertainity in $\hat{f}$). Different acquisition functions are available

-   Maximum probability of improvement (MPI)
    Suppose we have the maximum $f^{\*}$ among the current observed points. Let $\epsilon$ be an improvement parameter
    \begin{alignat}{2}
            \mu(x) &= P(\hat{f}(x) \geq f^{\*} + \epsilon) &&= P \left(\frac{\hat{f}(x) - E[\hat{f}(x)]}{Var(\hat{f}(x))} \geq \frac{(f^{\*} + \epsilon) - E[\hat{f}(x)]}{Var(\hat{f}(x))} \right)\newline
            &= P \left(Z < \frac{E[\hat{f}(x)] - (f^{\*} + \epsilon)}{Var(\hat{f}(x))} \right) &&= \Phi\left(\frac{E[\hat{f}(x)] - (f^{\*} + \epsilon)}{Var(\hat{f}(x))} \right)
    \end{alignat}
    where $Z$ is the standard normal and $\Phi$ is the cumulative probability distribution for $Z$. This works well if the maximum is known. $\epsilon$ controls the exploration with higher values favoring the same.

-   Upper Confidence Bound (UCB)
    \begin{align}
            \mu(x) = E[\hat{f}(x)] + \eta Var(\hat{f}(x))
        \end{align}
    where $\eta$ is a function parameter.

-   Expected Improvement (EI)
    \begin{align}
            EI &= E[max(\hat{f}(x) - f^{\*}, 0)]\newline
            \mu(x) &= \begin{cases}
                (E[\hat{f}(x)] - (f^{\*} + \epsilon))\Phi(Z) + Var(\hat{f}(x)) \phi(Z) &\mbox{if $Var(\hat{f}(x)) > 0$}\newline
                0 &\mbox{otherwise}
            \end{cases}\newline
            Z &= \begin{cases} \frac{E[\hat{f}(x)] - (f^{\*} + \epsilon)}{Var(\hat{f}(x))} &\mbox{if $Var(\hat{f}(x)) > 0$}\newline 0 &\mbox{otherwise} \end{cases}
        \end{align}
    This is the most commonly used acquisition function. The next point is chosen based on the maxima of this function (can be found using gradient ascent). The parameter $\epsilon$ controls how much exploration we want to perform (higher values favor exploration).

Bayesian Optimization using Gaussian Process vs Random Search

-   Random Search is easy to parallize while GP is sequential

-   Random Search requires much more points than GP to find the optima

-   GP is better when each evaluation of a new point is expensive

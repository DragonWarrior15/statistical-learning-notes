---
title: "Regression splines (Polynomials)"
---

## Regression splines (Polynomials)

This is a class of methods that extends upon the family of polynomial and step regressions.


Instead of fitting a global polynomial to $X$, we fit **local piecewise polynomials** to X such that they are continuous at the breakpoints. The points wherer the polynomials change are called **knots**.


As we increase the number of knots, we can get a more flexible predictor. In general, if there are $K$ knots, we have $K+1$ polynomials.


Having this many splines creates a lot of degrees of freedom in the data. To solve these many equations, we need to impose constraints of **continuity and continuity of derivatives at knots**. In general, for a $d$ degree spline, we will impose the function to be continuous at knots and also have the $d-1$ derivatives to be equal at the knots. The reduced degrees of freedom are essential for obtaining unique solutions to the coefficients such that to overall curve still looks continuous.


Instead of fitting multiple splines, we can also defined the function in a single format as follows. A truncated power basis function is defined as
\begin{align}
        h(x, \xi) = (x - \xi)\_{+}^{d} = \begin{cases} (x-\xi)^{d} &\mbox{if $x > \xi$}\newline
            0 &\mbox{$0$ otherwise} \end{cases}\newline
        \hat{y} = \beta_{0} + \beta_{1}b_{1}(x) + \beta_{2}b_{2}(x) + \cdots + \beta_{K+d}b_{K+d}(x)
    \end{align}
where the terms $b_{1},\ldots,b_{d}$ are the usual terms $x, x^{2}, \ldots, x^{d}$ and the remaining terms correspond to a truncated power function per knot. This ensures that the polynomials are continuous at the knots upto the $d-1$ derivates.


A **natural spline** is a regression spline that has the additional constraint of being linear at the boundaries, i.e., outside the extreme knots. This reduced flexibility allows for stable estimates at the knots and also makes the confidence bands narrower.

### Choosing the degrees of freedom

While it may make sense to put knots at the points where the function seems to change rapidly (and not at the points where the function seems to be relatively stable), in practice the knots are usually placed at equal quantiles of the data, or generally are placed in an equidistant fashion.

For deciding the degree of freedoms, another popular choice is cross validation. We always use say $10\%$ of the data as test and gauge the RSS on this set across different degrees of freedom. A plot of RSS vs. the degrees of freedom (similar to elbow curve) can aid choosing the desired point where the RSS significantly drops.

In practice, cubic splines are popular as higher order polynomials tend to give high variance, and the plots with cubic splines also look relatively stable.

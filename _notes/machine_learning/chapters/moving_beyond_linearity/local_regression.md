---
title: "Local Regression"
---

## Local Regression

As the name suggests, we fit regression models in the neighborhood of the point for which we want to make a prediction. But the difference from a normal linear regression is that we give weights to the points such that the points closest get higher weights and points further away get zero.


Suppose we want to make the predicton at the point $x_{0}$. The algorithm is as follows

1.  gather the fraction $s = k/n$ points closest to $x_{0}$ where $s$ is also called the span an acts like a regularizer. Higher $s$ will make a global fit and vice versa.

2.  Assign a weight $K_{i0} = K(x_{i}, x_{0})$ to all the points in the neighborhood of $x_{0}$ such that the point closest gets the highest weight while the one furthest away gets the weight zero. All the other points in the data get the weight zero.

3.  Minimize the error given by
    \begin{align}
                RSS = \sum_{i=1}^{n} K(x_{i}, x_{0})(y_{i} - \beta_{0} - \beta_{1}x_{i})^{2}
            \end{align}
    to estimate the values of $\beta_{0}$ and $\beta_{1}$. Note that $K$ is a function known beforehand and thus constant.

4.  Make the prediction as $\hat{y}\_{0} = \beta_{0} + \beta_{1}x_{0}$

These models are very useful for adapting to changes in the neighborhood of a given point. The distance function can take several forms like constant, linear, quadratic or even normal distribution.

The approach can be extended to multiple dimensions as well by defining corresponding distances. However, the approach performs **poorly in dimensions higher than $3$ or $4$** as it becomes difficult to find neighbors in the surrounding area (dimensionality curse).

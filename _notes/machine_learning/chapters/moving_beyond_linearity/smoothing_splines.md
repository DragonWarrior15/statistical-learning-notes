---
title: "Smoothing Splines"
---

## Smoothing Splines

The idea is to fit a smooth function that predicts the reponse well. We minimize the following
\begin{align}
        Loss = \sum_{i=1}^{n} (y_{i} - g(x_{i}))^{2} + \lambda \int g^{\prime \prime}(t)^{2}dt \quad \text{$\lambda > 0$}
    \end{align}
which can be decomposed into two parts, the first part encourages the function $g$ to fit the data well and the second part encourages the function to be smooth throughout.

If the function is constant or straight line, the double derivative is zero while on the other extreme, if the function changes rapidly, double derivative will also take large values.


When $\lambda$ is zero, the function simply takes the values of $y$ and thus becomes very jumpy (introducing high variance). On the other extreme, if $\lambda \to \inf$, the function is forced to be linear (which makes the double derivative zero). This is exactly the least square fit that we have seen earlier.


The function that minimizes the above loss is nothing but a cubic spline with knots at $x_{1}, x_{2}, \ldots, x_{n}$ with the additional constraint that the first and second derivatives are smooth at the knots. (The function is cubic in between the points). Outside the extreme knots, the function simply takes a linear form.

In some sense, this is similar to the [natural splines]({{ "/notes/machine_learning/chapters/moving_beyond_linearity/regression_splines.html" | relative_url }}) but is a shrinked version of the same, $\lambda$ controlling the level of shrinkage (or how large the roughness can be).

\begin{align}
        \hat{g}\_{\lambda} &= S_{\lambda}y\newline
        df_{\lambda} &= \sum_{i=1}^{n} \{S_{\lambda}\}\_{ii}
    \end{align}
where $\hat{g}\_{\lambda}$ is a $n$-vector containing the values at the points $x_{i}$s as a solution to a particular value of $\lambda$. $S_{\lambda}$ is a $n\times n$ matrix obtained as the solution of the above error function.

### Choosing Reguularization Parameter

It is possible to show that as $\lambda$ increases from $0 \to \inf$, the effective degrees of freedom ($df_{\lambda}$) go from $n \to 2$.


Cross validation can also be a useful approach to determine the value of $\lambda$. However, similar to linear regression, there exists a formula for computing the loss for LOOCV by just fitting a single model to the entire data set.
\begin{align}
        RSS_{cv}(\lambda) = \sum_{i=1}^{n} (y_{i} - \hat{g}\_{\lambda}^{(-i)}(x_{i}))^{2} = \sum_{i=1}^{n} \bigg[ \frac{y_{i} - \hat{g}\_{\lambda}(x_{i})}{1 - \{S_{\lambda}\}\_{ii}} \bigg]^{2}
    \end{align}
where $\hat{g}\_{\lambda}^{(-i)}(x_{i})$ denotes the estimate at any $x_{i}$ without using the point $i$ for calculating the loss (leave one out), while $\hat{g}\_{\lambda}(x_{i})$ denotes the estimate at $x_{i}$ using all of the data.

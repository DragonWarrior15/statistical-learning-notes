---
title: Exercises
---

## Exercises

1.  Suppose that a curve $\hat{g}$ is icomputed to smoothly fit a set of $n$ points using the following formula
    \begin{align}
                \hat{g} = \argmin_{g} \bigg( \sum_{i=1}^{n} (y_{i} - g(x_{i}))^{2} + \lambda \int \big[ g^{(m)} \big]^{2} dx \bigg)
            \end{align}
    where $g^{(m)}$ represents the $m$th derivtive of $g$ (and $g^{(0)}= g$). Provide the functional form of $g$ in the following scenarios.

    1.  $\lambda = \inf, m = 0$

    2.  $\lambda = \inf, m = 1$

    3.  $\lambda = \inf, m = 2$

    4.  $\lambda = \inf, m = 3$

    5.  $\lambda = 0, m = 3$

2.  Suppose we fit a curve with basis functions $b_{1}(X) = I(0 \leq X \leq 2) - (X-1)I(1 \leq X \leq 2)$, $b_{2}(X) = (X - 3)I(3 \leq X \leq 4) + I(4 \leq X \leq 5)$. We fit the regression model
    \begin{align}
            Y = \beta_{0} + \beta_{1}b_{1}(X) + \beta_{2}b_{2}(X) + \epsilon
            \end{align}
    and obtain the coefficient estimates as $\hat{\beta}\_{0} = 1, \hat{\beta}\_{1} = 1$ and $\hat{\beta}^{2} = 3$. Plot the estimated curve between $X = -2$ and $X = 2$.

3.  Consider the two curves $\hat{g}\_{1}$ and $\hat{g}\_{2}$ defined by
    \begin{align}
                \hat{g}\_{1} = \argmin_{g} \bigg( \sum_{i=1}^{n}(y_{i} - g(x_{i}))^{2} + \lambda \int \big[ g^{(3)}(x) \big]^{2} dx \bigg)
                \hat{g}\_{2} = \argmin_{g} \bigg( \sum_{i=1}^{n}(y_{i} - g(x_{i}))^{2} + \lambda \int \big[ g^{(4)}(x) \big]^{2} dx \bigg)
            \end{align}
    where $g^{(m)}$ represents the $m$th derivative of $g$.

    1.  as $\lambda \to \inf$, will $\hat{g}\_{1}$ or $\hat{g}\_{2}$ have the smaller training RSS ?

    2.  as $\lambda \to \inf$, will $\hat{g}\_{1}$ or $\hat{g}\_{2}$ have the smaller test RSS ?

    3.  as $\lambda = 0$, will $\hat{g}\_{1}$ or $\hat{g}\_{2}$ have the smaller training and test RSS ?

## Solutions

1.  <details><summary>Solution</summary>
    Higher derivatives will allow for a higher degree polynomial to be fit to the data

    1.  Since $\lambda$ is $\inf$, we only need to worry about the second term. Minimizing area under $g(x)^{2}$ is same as taking $g(x) = 0$.

    2.  Similar to above, now area under $g^{(1)}(x)$ must be minimized which means the second derivative is zero and $g$ is a constant. To minimize the residuals, $g = \sum_{i=1}^{n}y_{i}$.

    3.  Second derivative is zero means $g$ is a linear function. To minimize residuals, this is same as linear regression least squares.

    4.  thrid derivative is zero means that $g$ is a quadratic. Hence, we fit a quadratic equation over the data by minimizing the least squares.

    5.  We only need to bother with the residuals term now. Now $g$ can take many forms depending on how smooth we wish the function to be.</details>

2.  <details><summary>Solution</summary>
    For the range $[-2,2]$ the curve is simply defined as below
    \begin{align}
    {1}
                \hat{Y} = \begin{cases} 1     &\mbox{$-2 \leq x < 0$}\newline
                                        2     &\mbox{$ 0 \leq x < 1$}\newline
                                        3 - x &\mbox{$ 1 \leq x \leq 2$} \end{cases}
            \end{align}
    </details>

3.  <details><summary>Solution</summary>
    For $\lambda \to \inf$, the second part of the loss will dominate. As the derivative will increase, the solution can be a higher degree polynomial (as discussed in ans 1) which means a more flexible model and hence lower error on training data.

    1.  $\hat{g}\_{2}$ is the more flexible model and thus should have lower training RSS.

    2.  Test RSS is not trivial but generally, the more flexbile the model, the higher variance it has and the lower test RSS. Thus, $\hat{g}\_{1}$ should have the lower test RSS.

    3.  $\lambda = 0$ implies that both the error terms are similar and thus, both the functions are same.
    </details>

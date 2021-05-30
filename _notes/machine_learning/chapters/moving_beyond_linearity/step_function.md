---
title: "Step Function"
---

## Step Function

Polynomial Regression, like Linear Regression, still imposes a global structure on the data. The functional form of the model is same throughout. Step Function on the other hand has a local structure and divided the range into **$k$ intervals such that each interval is fitted with a different constant**.
\begin{align}
        C_{0}(X) &= I(X < c_{1})\newline
        C_{1}(X) &= I(c_{1} \leq X < c_{2})\newline
        C_{2}(X) &= I(c_{2} \leq X < c_{3})\newline
        &\vdots\newline
        C_{k-1}(X) &= I(c_{k-1} \leq X < c_{k})\newline
        C_{k}(X) &= I(c_{k} \geq X)\newline
        \hat{y} &= \beta_{0} + \beta_{1}C_{1}(x) + \cdots + \beta_{k}C_{k}(x)
    \end{align}
Note that, $\beta_{0}$ and $C_{0}(x)$ are equivalent since both will act as the intercept and the mean value of $y$ in the range $x < c_{1}$. Similarly, each of the $\beta_{i}$ captures the average of the response in the corresponding interval defined by the indicator function.

This approach works well when there are natural breakpoints in the data and if there are indeed constant trends in those intervals. As soon as a non constant trend emerges locally, the approach fails.

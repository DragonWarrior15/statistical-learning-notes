---
title: "Linear Model Selection and Regularization"
---

# Linear Model Selection and Regularization

Linear models are often simple and easy to interpret at the cost of having high bias if the relationship in the data is not linear. Some considerations about linear models

-   If $n >> p$, least square estimates often have less variance. If $n$ is larger than $p$, then least square estimates can have some variance. While if $n < p$, we are looking at non unique solutions which can cause lot of variation in the test predictions.

-   It is often the case that many of the predictors do not have a relationship with the response. Hence, it is a good idea to remove those and make the model more interpretable at the cost of some bias. Least square estimates almost never give zero coefficients.

There are major ways in which the number of variables in the model can be reduced

-   Selecting a **subset of variables** that go well with the response. This itself can be done by forward selection, backward elimination etc.

-   **Shrinking** some of the **coefficients** to zero. This is a great help in reducing the variance of the predictions.

-   **Dimension Reduction** helps in projecting the $p$ predictors onto a $M$ dimensional space where $M < p$. This utilizes linear combinations to create a set of new features.

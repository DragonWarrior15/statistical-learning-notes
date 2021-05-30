---
title: "Problems when using Linear Regression"
---

## Problems when using Linear Regression

##### Non linearity of data

will make linear regression perform poorly as the basic assumption is that the data has linear relation with response. In case the data is non-linear, we expect to see distinct patterns in the residual vs variable plots. To induce linearity, transformations like $\log$, $exp$, $sqrt$ etc. can be checked.

##### Correlation of errors

We do not expect $\epsilon_{i}$ to give any information regarding $\epsilon_{i+1}$ as that will cause the standard errors to be underestimated giving wider confidence intervals. This can be checked by plotting the residuals vs a shifted version, which should not give any discernable patterns.

##### Heteroscedasticity

or non-constant variance in residuals also violates the assumption that the response/errors have constant variance. This can be checked by plotting the residuals vs a variable. In case the variance is not constant, we expect to see the residuals to get further away from each other as we progress along the variable x.

##### Outliers

can cause trouble with the model as mean square error will give more weightage to larger errors. This can be checked for by plotting either the histogram of the variable to ensure thin tails, or by plotting the residual/standard error estimate, which should have no discernable pattern.

##### Multicollinearity

occurs when one of the variable is expressible as a linear combination of a set of the remaining variables. This can cause large variance in the estimation of the coefficients. It can be checked for using *Variance Inflation Factor*
\begin{align}
    VIF &= \frac{1}{1 - R_{X_{j}|X_{-j}}^{2}}\end{align}
where $R_{X_{j}|X_{-j}}^{2}$ is the $R^{2}$ score obtained by regressing the $j^{th}$ variable on all the remaining variables. Typically, VIF should be $\leq 3$-$5$. Higher values indicate significant correlation of this variable with the others.

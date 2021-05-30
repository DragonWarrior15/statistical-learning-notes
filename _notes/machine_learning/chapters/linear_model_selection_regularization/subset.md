---
title: "Subset Selection"
---

## Subset Selection

### Best Subset Selection

This is a naive approach that essentially tries to find the best model among $2^{p}$ models that are trained on all possible subsets of the $p$ variables. As we increase the subset of variables, the training error will monotonically decrease whereas the same cannot be said for the test error. A number of criteria like test MSE, $R^{2}$, AIC etc can be used to pick the models.


In case of classification models, similar argument holds and a more general error metric $deviance$ can be used. $Deviance$ is defined as $-2 * \log likelihood$ of the data. The smaller the $deviance$, the better the model fit.


The huge search space presented by this approach easily overfits as the search space presents more opportunities to find better fits. However, this causes a higher variance in the predictions on future data and can possibly also have higher test error.

##### Note regarding dummy variables

Whenever we have a group of variables that actually represent the same quantity, like a dummy variable for gender/income, it is important to keep either all of them, or none of them in the model. This is in accordance with keeping the degrees of freedom consistent. Hence, in any subset selection algorithm, all variables of the set are either considered together or not considered at all.

### Forward Stepwise Selection

This is a greedy approach that significantly shrinks the search space being checked (in comparison to the best subset selection approach).

Forward Stepwise Selection Algorithm

1.  Let $M_{0}$ denote the null model, i.e., the model with no predictors

2.  For $k = 0, 1, \ldots, p - 1$

    1.  Consider all $p - k$ models formed by adding a single predictor to the model $M_{k}$

    2.  Select the best model $M_{k+1}$ among the $p - k$ models on the basis of the error metric

3.  From the models $M_{0}, M_{1}, \ldots, M_{p}$, select the one with the lowest cross validation error on the evaluation choosing the appropriate error metric

This approach effectively has reduced the search space from $2^{p}$ to $1 + p(p+1)/2$. Although, now it is not guaranteed that the model selected will be the best one among $2^{p}$.


Note that in linear regression, the forward stepwise method will start with first adding the intercept, and then the independent variables one by one.

### Backward Stepwise Selection

This approach is the opposite of forward stepwise selection. We recursively reduce the number of variables in our model.

1.  Let $M_{p}$ denote the complete model, i.e., the model with all p predictors

2.  For $k = p, p-1, \ldots, 1$

    1.  Consider all $k-1$ models that keep all but one predictors in the current model $M_{k}$

    2.  Among these, select the best model $M_{k-1}$ with the lowest error

3.  From the models $M_{0}, M_{1}, \ldots, M_{p}$, select the one with the lowest cross validation error on the evaluation choosing the appropriate error metric

The number of models explored is same as the forward stepwise method.

A hybrid approach is usually selected where we start with the usual forward selection method, but while adding variables, we do not add a variable if it does not give significant improvement. Another approach can be to remove redundant variables using p-test at every step of forward selection.

---
title: "Exercises"
---

## Exercises

### Questions

1.  We perform the best subset, forward stepwise and backward stepwise on a single data set and obtain p+1 models containing $0, 1, \ldots, p$ predictors.

    1.  Which of the three models with $k$ predictors has the smalles training RSS ?

    2.  Which of the three models with $k$ predictors has the smallest test RSS ?

    3.  True or False

        1.  The predictors in the $k$-variable model identified by forward stepwise are a subset of the predictors in the $(k+1)$-variable model identified by forward stepwise selection.

        2.  The predictors in the $k$-variable model identified by backward stepwise are a subset of the predictors in the $(k+1)$-variable model identified by backward stepwise selection.

        3.  The predictors in the $k$-variable model identified by backward stepwise are a subset of the predictors in the $(k + 1)$-variable model identified by forward stepwise selection.

        4.  The predictors in the $k$-variable model identified by forward stepwise are a subset of the predictors in the $(k+1)$-variable model identified by backward stepwise selection.

        5.  The predictors in the $k$-variable model identified by best subset are a subset of the predictors in the $(k + 1)$-variable model identified by best subset selection.

2.  For parts (a) through (c), indicate the correct choice and explain the answer.

    1.  The lasso, relative to least square is

        1.  More flexible and hence will give improved prediction accuracy when its increase in bias is less than its decrese in variance.

        2.  More flexible and hence will give improved prediction accuracy when its increase in variance is less than its decrease in bias.

        3.  Less flexible and hence will give improved prediction accuracy when its increase in bias is less than its decrease in variance.

        4.  Less flexible and hence will give improved prediction accuracy when its increase in variance is less than its decrease in bias.

    2.  Repeat (a) for ridge regression relative to least squares.

    3.  Repeat (b) for non-linear methods relative to least squares.

3.  Suppose we estimate regression coefficients in a linear model by minimizing
    \begin{align}
                \sum_{i=1}^{n}\bigg( y_{i} - \beta_{0} - \sum_{j=1}^{p}\beta_{j}x_{ij} \bigg)^{2} \text{ subject to } \sum_{j=1}^{p}\mid \beta_{j} \mid \leq s
            \end{align}
    for a particular value of $s$. For the following parts, indicate which of the options is correct and explain.

    1.  As we increase $s$ from 0, the training RSS will

        1.  Increase initially, and then eventually start decreasing in an inverted U shape.

        2.  Decrease initially, and then eventually start increasing in a U shape.

        3.  Steadily increase.

        4.  Steadily decrease.

        5.  Remain constant.

    2.  Repeat (a) for test RSS.

    3.  Repeat (a) for variance.

    4.  Repeat (a) for (squared) bias.

    5.  Repeat (a) for the irreducible error.

4.  Suppose we estimate regression coefficients in a linear model by minimizing
    \begin{align}
                \sum_{i=1}^{n}\bigg( y_{i} - \beta_{0} - \sum_{j=1}^{p}\beta_{j}x_{ij} \bigg)^{2} + \lambda \sum_{j=1}^{p}\beta_{j}^{2}
            \end{align}
    for a particular value of $\lambda$. For the following parts, indicate which of the options is correct and explain.

    1.  As we increase $s$ from 0, the training RSS will

        1.  Increase initially, and then eventually start decreasing in an inverted U shape.

        2.  Decrease initially, and then eventually start increasing in a U shape.

        3.  Steadily increase.

        4.  Steadily decrease.

        5.  Remain constant.

    2.  Repeat (a) for test RSS.

    3.  Repeat (a) for variance.

    4.  Repeat (a) for (squared) bias.

    5.  Repeat (a) for the irreducible error.

5.  It is well-known that ridge regression tends to give similar coefficient values to correlated variables, whereas the lasso may give quite different coefficient values to correlated variables. We will now explore this property in a very simple setting.

    Suppose that $n = 2$, $p = 2$, $x_{11} = x_{12}$, $x_{21} = x_{22}$. Furthermore, suppose that $y_{1} +y_{2} = 0$ and $x_{11} +x_{21} = 0$ and $x_{12} +x_{22} = 0$, so that the estimate for the intercept in a least squares, ridge regression, or lasso model is zero: $\hat{\beta_{0}} = 0$.

    1.  Write out the ridge regression optimization problem in this setting.

    2.  Argue that in this setting, the ridge coefficient estimates satisfy $\hat{\beta_{1}} = \hat{\beta_{2}}$.

    3.  Write out the lasso optimization problem in this setting.

    4.  Argue that in this setting, the lasso coefficients $\hat{\beta_{1}}$ and $\hat{\beta_{1}}$ are not unique---in other words, there are many possible solutions to the optimization problem in (c). Describe these solutions.

6.  Using the bayesian formulation given below, derive the ridge and lasso formulations
    \begin{align}
                p(\beta|X,Y) \propto f(Y|\beta,X)p(\beta|X) = f(Y|\beta,X)p(\beta)
            \end{align}

    1.  Suppose $y_{i} = \beta_{0} + x_{i}^{T}\beta + \epsilon_{i}$ where $\epsilon_{i}$ is normal with mean $0$ and variance $\sigma^{2}$. Calculate the likelihood of the data.

    2.  Assume the following prior for $\beta$: $\beta_{1},\ldots,\beta_{p}$ are independent identically distributed with the distribution $p(\beta) = \frac{1}{2b}\exp(-\mid \beta \mid/b)$. Write the posterior for $b$ in this setting.

    3.  Argue that the lasso estimate is the *mode* of the posterior on $\beta$.

    4.  Now assume that the $\beta$ are independently and identically distributed with the mean $0$ and variance $c$. Find the posterior of the $\beta$ in this case.

    5.  Argue that the ridge regression estimate is both the mode and mean for $\beta$ under this distribution.

### Answers

1.  1.  Best subset model will have the lowest training RSS as it looks over all possible subsets of models.

    2.  Best subset model will typically overfit and thus forward or backward stepwise models will have lower test RSS.

    3.  1.  True as we add variables to the last model.

        2.  True as we remove variables from the last model.

        3.  False as this is not necessary. The paths chosen are independent.

        4.  False.

        5.  False as the set of variables can be completely independent.

2.  1.  iii as lasso is less flexible (some coefficients are zero) which decreases variance with an increase in bias.

    2.  iii as it is similar to lasso in terms of purpose of use.

    3.  ii as non-linear models make less assumptions and are more flexible. This reduces bias at expense of variance.

3.  1.  Refer to [image]({{ "/notes/machine_learning/chapters/linear_model_selection_regularization/shrinkage.html#variable-selection-property-of-lasso-regression" | relative_url }}). As we increase s, we are expanding the region of allowed $\beta$. Hence, we are moving closer to the least squares fit which gives minimum training RSS.

    2.  We have high bias with a constant model. As $s$ increases, the test RSS initially decreases and then begins into increase as we keep relaxing the model, giving a U shape.

    3.  Constant model has zero variance. It increases as we relax the model (increase $s$).

    4.  By bias variance tradeoff, bias reduces as $s$ increases.

    5.  It is always constant.

4.  1.  As $\lambda$ increases, the model becomes more constrained and training RSS increases.

    2.  At $\lambda$ the model has minimum training RSS and high test RSS. As $\lambda$ increases, test RSS initially decreases until it is high for large $\lambda$.

    3.  As the model becomes less and less flexible to a constant model, the variance keeps decreasing.

    4.  By bias variance tradeoff, bias will keep increasing (it's minimum for least squares fit).

    5.  By definition, it remains constant.

5.  1.  The data points after substituitions become $((x_{11}, x_{11}), y_{1})$ and $((-x_{11}, -x_{11}), -y_{1})$. The optimization functhion then becomes
        \begin{align}
                        RSS &= \sum_{i=1}^{n}(y_{i} - \sum_{j=1}^{p} \beta_{j}x_{ij})^{2} + \lambda \sum_{j=1}^{p}\beta_{j}^{2}\newline
                          &= 2(y_{1}-x_{11}(\beta_{1}+\beta_{2}))^{2} + \lambda(\beta_{1}^{2} + \beta_{1}^{2})
                    \end{align}

    2.  Taking partial derivates with $\beta_{1}$ and $\beta_{2}$,
        \begin{align}
                        4(y_{1} - x_{11}(\beta_{1} + \beta_{2}))(-x_{11}) + 2\lambda \beta_{1} &= 0\newline
                        4(y_{1} - x_{11}(\beta_{1} + \beta_{2}))(-x_{11}) + 2\lambda \beta_{2} &= 0
                    \end{align}
        which gives $\beta_{1} = \beta_{2}$.

    3.  In a similar fashion to above, the final optimization is
        \begin{align}
                         RSS = 2(y_{1}-x_{11}(\beta_{1}+\beta_{2}))^{2} + \lambda(\mid \beta_{1} \mid + \mid \beta_{1} \mid)
                    \end{align}

    4.  Taking partial derivates with $\beta_{1}$ and $\beta_{2}$,
        \begin{align}
                        4(y_{1} - x_{11}(\beta_{1} + \beta_{2}))(-x_{11}) + 2\lambda \frac{\mid \beta_{1} \mid}{\beta_{1}} &= 0\newline
                        4(y_{1} - x_{11}(\beta_{1} + \beta_{2}))(-x_{11}) + 2\lambda \frac{\mid \beta_{2} \mid}{\beta_{2}} &= 0
                    \end{align}
        which gives $\frac{\mid \beta_{1} \mid}{\beta_{1}} = \frac{\mid \beta_{2} \mid}{\beta_{2}}$, clearly not a unique solution.

6.  1.  For any $y_{i}$, the distribution given $X$ and $\beta$ is normal since $y_{i}$ = constant + Normal. The constant is $\beta_{0} + x_{i}\beta$ and the variance is $\sigma^{2}$.
        \begin{align}
                        f(Y|X,\beta) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^{2}}}\exp(-\frac{(y_{i}-\beta_{0}-x_{i}\beta)^{2}}{2\sigma^{2}})
                    \end{align}

    2.  The prior for $\beta$ will simply be the product of all the $\beta_{i}$. The posterior thus becomes
        \begin{align}
                        p(\beta|X,Y) &= f(Y|X,\beta)\prod_{j=1}^{p}\frac{1}{2b}exp{-\frac{\mid \beta_{j} \mid}{b}}\newline
                        \ln(p(\beta|X,Y)) &= \ln((\frac{1}{\sqrt{2\pi \sigma^{2}}})^{n} (\frac{1}{2b})^{p}) + \sum_{i=1}^{n} -\frac{(y_{i}-\beta_{0}-x_{i}\beta)^{2}}{2\sigma^{2}} + \sum_{j=1}^{p} -\frac{\mid \beta_{j} \mid}{b}
                    \end{align}
        Removing constants and adjusting (includling $-1$), maximizing above equation is same as minimizing
        \begin{align}
                        \sum_{i=1}^{n} (y_{i}-\beta_{0}-x_{i}\beta)^{2} + \frac{2\sigma^{2}}{b}\sum_{j=1}^{p} \mid \beta_{j} \mid
                    \end{align}
        which is the Lasso regression optimization function with $\lambda = 2\sigma^{2}/b$.

    3.  $\beta$ obtained as a result of maximizing the posterior $p(\beta|X,Y)$ is the *mode* of that distribution and also happens to be the solution of the lasso regressin optimization function.

    4.  The posterior is similar in form to the one derived above with minor changes
        \begin{align}
                        p(\beta|X,Y) &= f(Y|X,\beta)\prod_{j=1}^{p}\frac{1}{2c^{2}}exp{-\frac{\beta_{j}^{2}}{2c^{2}}}\newline
                        \ln(p(\beta|X,Y)) &= \ln((\frac{1}{\sqrt{2\pi \sigma^{2}}})^{n} (\frac{1}{2c^{2}})^{p}) + \sum_{i=1}^{n} -\frac{(y_{i}-\beta_{0}-x_{i}\beta)^{2}}{2\sigma^{2}} + \sum_{j=1}^{p} -\frac{\beta_{j}^{2}}{2c^{2}}
                    \end{align}

    5.  Maximizing the above posterior is same as minimizing
        \begin{align}
                        \sum_{i=1}^{n} (y_{i}-\beta_{0}-x_{i}\beta)^{2} + \frac{2\sigma^{2}}{b}\sum_{j=1}^{p} \beta_{j}^{2}
                    \end{align}
        which is a quadratic. The log of posterior is itself a parabola. The $\beta$ that maximizes the posterior is not only the mode of that distribution, but also the mean (due to the symmetry). And coincidentally, it will also minimize the ridge regression optimization function given above.

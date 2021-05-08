---
title: "Boosting"
---

## Boosting

Boosting is a general tecnique that can be applied to multiple statistical learning techniques and not just decision trees. Like Bagging, boosting is also trained on multiple data sets derived from the training data, but instead of building independent trees on different data sets, **boosting is a sequential process that builds trees on modified versions of the original data set**.


Given a model, boosting will try to fit a tree on the residuals obtained by the model instead of the response $Y$. The model is then updated by adding this tree and the residuals are calculated again. **Trees in boosting are typically small, just a few terminal nodes** controlled by the parameter $d$ and we allow the tree to fit the areas where improvement is needed in a slow manner. Shrinkage parameter $\lambda$ allows to further slow down this process allowing for a variety of trees.


Boosting has three parameters

1.  $B$, the number of trees. Unlike bagging, large $B$ can overfit although slowly. Right value of $B$ can be determined through cross validation.

2.  Shrinkage parameter $\lambda$ which controls how slowly the model is learnt and is a small positive number in the range 0.1 to 0.001 typically. Very smal $\lambda$ can require a very large $B$ to achieve a good performance.

3.  The number of splits $d$ in a single tree. Typically $d=1$ is used and referred to a stump. Higer value signifies higher interaction between the variables. When using stumps, the model is simply additive since we are using a single variable in each of the trees.

Boosting algorithm is as follows

1.  Set the residuals $r_{i} = y_{i}$ and the model $\hat{f}(x) = 0$.

2.  For $b = 1, \cdots, B$ repeat

    1.  Fit the model $\hat{f}^{b}(x)$ with $d$ splits on the data $(X,r)$

    2.  Update the model
        \begin{align}
                         \hat{f}(x) \leftarrow \hat{f}(x) + \lambda \hat{f}^{b}(x)
                     \end{align}

    3.  Update the residuals
        \begin{align}
                         r_{i} \leftarrow r_{i} - \lambda \hat{f}^{b}(x)
                     \end{align}

3.  Return the boosted model
    \begin{align}
                 \hat{f}(x) = \sum_{b=1}^{B} \lambda \hat{f}^{b}(x)
             \end{align}

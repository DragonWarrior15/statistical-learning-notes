---
title: "Distances and Dissimilarity Measures"
---

## Distances and Dissimilarity Measures

Clustering aims to group observations similar observations in the same group, while dissimilar observations fall in different groups. To achieve this mathematically, we need to define a way to measure dissimilarity between observations. If we have $N$ observations with $p$ variables, then
\begin{align}
        D(x_{a}, x_{b}) = \sum_{j=1}^{p}d_{j}(x_{aj}, x_{bj})
    \end{align}

where $D$ is a symmetric similarity matrix of size $N \times N$. To get this for any pairs of values, we sum up the similarity measure along all the variables. Most algorithms need this matrix to be symmetric and if that is not the case, replace $D$ with $(D + D^{T})/2$ will help.


The most common choice for $d_{j}$ is squared distance, but it can also be replaced with the absolute difference. The desirable properties of any such measure is that the values should be positive and monotonically increasing.

##### Quantitative Variables

are the simplest to deal with. We can define a real valued monotonically increasing function in several possible ways
\begin{align}
        d_{j}(x_{aj}, x_{bj}) &= \lvert x_{aj} - x_{bj} \rvert\newline
        d_{j}(x_{aj}, x_{bj}) &= (x_{aj} - x_{bj})^{2}\newline
        D(x_{a}, x_{b}) &= \frac{\sum_{j=1}^{p} (x_{aj} - \overline{x}\_{a})(x_{bj} - \overline{x}\_{b})}{\sqrt{\sum_{j=1}^{p} (x_{aj} - \overline{x}\_{a})^{2}} \sqrt{\sum_{j=1}^{p} (x_{bj} - \overline{x}\_{b})^{2}}}, \quad \overline{x}\_{a} = \frac{1}{p}\sum_{j=1}^{p} x_{aj}
    \end{align}

If we have standardized the observations, the last equation will simply be similar to squared distance, $\sum_{j=1}^{p} (x_{aj}-x_{bj})^{2} \propto 2(1 - \rho(x_{a}, x_{b}))$. Hence clustering based on correlation will be similar to the one based on squared distances.

Correlation based measure can be useful in retail behaviour when we want to check profiles based on the whether similar products are purchased rather than how many of them are purchased.

##### Ordinal Variables

already have a pre defined ranking order. If we number such variable with $M$ levels from $1$ to $M$, the levels are replaced with
\begin{align}
        \frac{i - 1/2}{M}, \quad i = 1, 2, \ldots, M
    \end{align}
and treat them simply as a numeric variable.

##### Categorical Variables

are handled in a slightly different manner. If the variable has $M$ levels, we create an $M \times M$ matrix $L$ such that $L{ij}$ is the required measure of dissimilarity between $i^{th}$ and $j^{th}$ variables. A common choice is to have all entries of $L$ equal 1 except the diagonals which are filled with 0. This gives equal weightage to all pairings.


For combining the different distance measures of the variables, we can use $D(x_{a}, x_{b}) = \sum_{j=1}^{p} w_{j} d_{j}(x_{aj}, x_{bj})$ with $\sum_{j=1}^{p} w_{j} = 1$ to get a weighted convex combination of the measures. Note that if the different variables are on different scales (different variances), the individual contributions will not be $w_{j}$ but rather $w_{j} Var(X_{j})$. Thus, setting $w_{j} \propto 1/Var(X_{j})$ will enable each variable getting the same weight.


In case of missing values, it is often the case that those observations are simply ignored. For categorical variables, we usually treat them as a separate category. The imputation strategy for numerical variables will vary among problems and depend on the context.

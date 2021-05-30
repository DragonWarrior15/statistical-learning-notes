---
title: "Bagging"
---

## Bagging

Decision tree suffer from a high variance. When the data is divided into smaller parts, it is quite likely to expect variance when the data set itself is changed. Bootstrap Aggregation of Bagging is a method to try to overcome this problem.


**Averaging a set of independent random variables reduces variance**. Consider $n$ random variables with the same variance $\sigma^{2}$, then the variance of their average is $\sigma^{2}/n$. Naturally, we can extend this idea to build several prediction models on different training data sets and average out their results to reduce the variance in the response.


We train $b$ different models, make predictions $\hat{f}\_{i}(x)$ using these and then average them out to get a low variance
\begin{align}
        \hat{f} = \frac{1}{B}\sum_{b=1}^{B} \hat{f}\_{b}(x)
    \end{align}

This reduction is obvious when the trees are completely independent. This is not true in majority of the cases. Since the trees are deep, we expect them to have very low bias, and similar expectations/means. The noise is introduced due to their variance. Suppose the trees come from the same distribution, but have some pairwise correlation $\rho$
\begin{align}
        E[\hat{f}\_{b}(x)] = \mu, \quad Var(\hat{f}\_{b}(x)) = \sigma^{2} = E[\hat{f}\_{b}(x)^{2}] - \mu^{2}\newline
        \rho = \frac{E[(\hat{f}\_{i}(x) - \mu)(\hat{f}\_{j}(x) - \mu)]}{\sqrt{Var(\hat{f}\_{i}(x))Var(\hat{f}\_{j}(x))}} = \frac{E[\hat{f}\_{i}(x)\hat{f}\_{j}(x) - \mu^{2}]}{\sigma^{2}}
    \end{align}
Then, variance of the average of trees
\begin{align}
        Var(\frac{1}{B} \sum_{b=1}^{B} \hat{f}\_{b}(x)) &= E[\big(\frac{1}{B} \sum_{b=1}^{B} \hat{f}\_{b}(x)\big)^{2}] - E[\big(\frac{1}{B} \sum_{b=1}^{B} \hat{f}\_{b}(x)\big)]^{2}\newline
        &= \frac{1}{B^{2}} \big(E[\sum_{b=1}^{B} \hat{f}\_{b}(x)^{2}] + \sum_{i< j}E[\hat{f}\_{i}(x)\hat{f}\_{j}(x)] \big) - \mu^{2}\newline
        &= \frac{1}{B^{2}}\big( B\mu^{2} + B(B-1)(\sigma^{2} + \mu^{2}) \big) - \mu^{2}\newline
        &= \rho \sigma^{2} + \frac{1-\rho}{B} \sigma^{2}
    \end{align}
When the number of trees is large enough, $\rho$ will decide how much the variance shrinks.


Since we do not have access to different training datasets, we will get the average using bootstraps of the original data set. Note that **trees grown on bootstrapped data sets are deep and not pruned** so that they have low bias. Even though they may have high variance, averaging will reduce it out.


**Averaging bootstrapped predictors works for regression** while we **take the majority vote in case of classification**. The overall prediction is the most commonly occurring class across the $B$ trees. Note that **using a large value of *B* will not lead to overfitting**, it should just be sufficiently large to ensure the error has come down compared to a single tree (building too many trees can take up significant time).

### Out of Bag Error

It can be shown the probability of an observation being present in a bootstrapped dataset is $1 - 1/e$ (this can be shown by considering that the probability that an observation is not present in the data set is $((1 - 1/n)^{n}$ and taking the limit $n \to \infty$). Thus, on an average, a data will only contain about $2/3$rd ($0.63$ to be exact) of the total observations in it. We can make use of the observations not used for training to estimate the error.


Any observation not part of the bootstrapped set is called **Out of Bag** and the error we are about to calculate is out of bag error. Now, we can take the $i$th observation, and get it's prediction from the sets where it was not used for training. This will be around $1/3$rd of the predictors. We can combine these results using average in case of regression or majority vote in case of classification. Thus, we have a \"test error\" for all the observations in the data.

### Variable Importance

We have been able to reduce the variance using the bagging approach, but the model is no longer interpretable due to the presence of multiple trees. We need to somehow aggregate all the trees to get this measure.


A simple workaround is to calculate the total amount the RSS (regression) or Gini Index (classification) has decreased across all the trees due to split on a particular variable. To make the values comparable, we simply take the average across $B$ trees. A large value means that the variable has high importance.

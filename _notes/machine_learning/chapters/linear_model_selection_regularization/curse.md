---
title: Curse of Dimensionality
---

## Curse of Dimensionality

Most of the methods discuss here **work well when** $\boldsymbol{n > > p}$. There can be many reasons why the model may not perform well in higher dimensions, but the major one will be the fact that as more and more dimensions are added to the model, chances of overfitting increase and so do the chances that the additional variables are simply noise.

We refer to the problem of training a model a high dimensional problem when $p > n$, or we have more data than number of predictors. Note that it is easy to obtain $R^{2} = 1$ in such a setting which consequently leads to $\hat{\sigma}^{2} \approx 0$. Metrics like $C_{p}$, AIC, BIC become useless.

Hence, in higher dimensional settings, it is important to obtain model performance on unseen data as there is a good chance of obtaining perfect results on the training set. Metrics associated with the training set can thus prove to be misleading.

##### Intuition

for the curse of dimensionality can be easily obtained in the context of KNN.

Suppose the data is uniformly distributed along any dimension considered. Let the model be built in such a way that when making predictions, it uses $10\%$ of the data along all dimensions.

In the case of a single dimension, we need $10\%$ of the data. In the case of 10 dimensions, we will need to check $10\% ^{10} = 10^{-8}\%$ of data. Clearly this number grows as we consider more and more dimensions.

Thus, as the number of dimensions grow, we require substantially more data as the data observable in the neighborhood of the point is extremely small. This illustrates the fact that in higher dimensions, having less data will lead to a poor model.

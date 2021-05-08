---
title: "Patient Rule Induction Method (PRIM)"
---

## Patient Rule Induction Method (PRIM)

The CART method tries to partition the whole input space into boxes and the aim is to make those boxes as different as possible. PRIM on the other hand, tries to find boxes which have higher response mean (or trying to find a _bump_ in the input space). This is achieved as follows

1.  A big bounding box is created containing all the data in the training set.

2.  A small fraction $\alpha$ (0.05 or 0.1) of observations are removed from one face (the higher or lower end of one of the predictors) such that the response of the mean is higher in the remaining box (_peeling_).

3.  The process is repeated under the box contains a minium number of observations.

4.  Since the approach was greedy, it is possible that some optimal box was left out. Hence, we expand the box by expanding one face at a time as long as the box response mean is increasing (_pasting_).

5.  Among this sequence of boxes, the best one is chosen via cross validation.

6.  All the data in this chosen box is removed and the process is continued with the reamining observations.

This approach works well with regression and binary classification (0-1 encoding of classes). The advantage of PRIM over CART is it's patience and slow removal of data. CART splits data too quickly using at most $log_{2}(N)$ splits, while PRIM will use roughly $-log(N)/log(1-\alpha)$ steps (this can be seen by considering the approximate steps as $N(1-\alpha)^{steps} = 1$ and solving by taking the log). The rules for any box are a set of double sided inequalities, and may make the approach less interpretable than CART.

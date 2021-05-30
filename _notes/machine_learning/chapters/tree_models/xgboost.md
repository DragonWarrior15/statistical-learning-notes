---
title: "XGBoost"
---

## XGBoost

Reference documentation for xgboost is [here](https://xgboost.readthedocs.io/en/latest/tutorials/model.html).
In this section, $N$ refers to the number of data points, $T$ to the number of trees in the ensemble, $L$ to the number of leaves.


XGBoost is extreme gradient boosting. It tries to directly optimize the supervised learning loss function
\begin{align}
     obj(\theta) = L(\theta) + \Omega(\theta)\end{align}
where the two terms are the loss function and the regularisation term. For instance, the loss function for RMSE is $\sum_{i=1}^{N} (y_{i} - \hat{y}\_{i})^{2}$. The regularisation term will control the model complexity, controlling overfitting to some extent.


An ensemble of decision trees is a good choice for the model because of their predictive power. The final prediction is simply an addition of all the trees which are part of the ensemble. Mathematically,
\begin{align}
    \hat{y}\_{i} = \sum_{t=1}^{T} f_{t}(x_{i})\end{align}
and the objective to be minimized is
\begin{align}
    obj(\theta) = \sum_{i=1}^{N} l(y_{i}, \hat{y}\_{i}) + \sum_{t=1}^{T} \Omega(f_{t})\end{align}

Lets start building the trees one by one ($T$ is not known in advance). Since the final prediction is additive, we can rewrite it in a recursive format
\begin{align}
    \hat{y}\_{i}^{(t)} = \sum_{j=1}^{t} f_{j}(x_{i}) &= \sum_{j=1}^{t-1} f_{j}(x_{i}) + f_{t}(x_{i}) \newline
    &= \hat{y}\_{i}^{(t-1)} + f_{t}(x_{i})\end{align}
Assuming we are building the $t^{th}$ tree, all the $t-1$ trees have already been built. Their predictions and structures are constant with respect to the current $t^{th}$ tree. The objective can be written as
\begin{align}
    obj(\theta) &= \sum_{i=1}^{N} l(y_{i}, \hat{y}^{(t)}\_{i}) + \sum_{j=1}^{t} \Omega(f_{j}) \newline
    &= \sum_{i=1}^{N} l(y_{i}, \hat{y}^{(t-1)}\_{i} + f_{t}(x_{i})) + \sum_{j=1}^{t-1} \Omega(f_{j}) + \Omega(f_{t}) \newline
    &= \sum_{i=1}^{N} l(y_{i}, \hat{y}^{(t-1)}\_{i} + f_{t}(x_{i})) + \Omega(f_{t}) + constant\end{align}

The new tree should be such that it optimizes this objective as much as possible. We can simplify the loss function by using its taylor expansion to the second order. Recall that for an infinitely differentiable function $f$ at $a$, the taylor expansion of $x$ near $a$ is
\begin{align}
    f(x) = f(a) + \frac{f^{\prime}(a)}{1!}(x-a) + \frac{f^{\prime \prime}(a)}{2!}(x-a)^{2} + \ldots\end{align}

In our objective function, $f$ is the loss function, $x = \hat{y}^{(t-1)}\_{i} + f_{t}(x_{i})$, and $a = \hat{y}^{(t-1)}\_{i}$. Plugging into our equation,
\begin{align}
    obj^{(t)} &= \sum_{i=1}^{N} l(y_{i}, \hat{y}^{(t-1)}\_{i} + f_{t}(x_{i})) + \Omega(f_{t}) + constant\newline
    &= \sum_{i=1}^{N} l(y_{i}, \hat{y}^{(t-1)}\_{i}) + \frac{\partial l(y_{i}, \hat{y}^{(t-1)}\_{i})}{\partial \hat{y}^{(t-1)}\_{i}} f_{t}(x_{i}) + \frac{1}{2} \frac{\partial^{2} l(y_{i}, \hat{y}^{(t-1)}\_{i})}{\partial (\hat{y}^{(t-1)}\_{i})^{2}} f_{t}^{2}(x_{i}) + \Omega(f_{t}) + constant\newline\end{align}

Representing $g$ and $h$ as the first and second derivatives respectively, and removing all terms dependent only on $\hat{y}^{(t-1)}\_{i}$ (because they are constant)
\begin{align}
    obj^{(t)} &= \sum_{i=1}^{N} g_{i} f_{t}(x_{i}) + \frac{1}{2} h_{i} f_{t}^{2}(x_{i}) + \Omega(f_{t}) + constant\end{align}

Because of the tree structure, all points in the same leaf get the same score. Let $w_{q(x_{i})} = f(x_{i})$ denote the score of the $i^{th}$ data point, where $q$ is a function that maps a data point to a leaf. For a given tree, the count of unique scores is no more than the total number of leaves.

Rewriting the objective to incorporate the score $w$
\begin{align}
    obj^{(t)} &= \sum_{i=1}^{N} g_{i} w_{q(x_{i})} + \frac{1}{2} h_{i} f_{t}^{2}(x_{i}) + \Omega(f_{t}) + constant\newline
    &= \sum_{j=1}^{L} (\sum_{i \in I_{j}} g_{i})w_{j} + \frac{1}{2}(\sum_{i \in I_{j}} h_{i})w^{2}\_{j} + \Omega(f_{t})\end{align}
where $I_{j} = \{i|q(x_{i} = j)\}$ is an indicator function denoting the set of data points which belong to the current leaf.


Now, we can write the regularisation part of the loss function to incorporate the tree structure. A tree is complex if it has too many leaves, or the weights of any leaf are too high. A good choice that works well in practice is
\begin{align}
    \Omega(f_{t}) = \gamma L + \frac{1}{2}\lambda \sum_{j=1}^{L} w_{j}^{2}\end{align}
where $\gamma$ will control the complexity of the tree, and $\lambda$ denotes how much weightage we give to the regularisation part of the loss. Incorporating this into the objective,
\begin{align}
    obj^{(t)} &= \sum_{j=1}^{L} (\sum_{i \in I_{j}} g_{i})w_{j} + \frac{1}{2}(\sum_{i \in I_{j}} h_{i})w^{2}\_{j} + \gamma L + \frac{1}{2}\lambda \sum_{j=1}^{L} w_{j}^{2}\newline
    &= \sum_{j=1}^{L} (\sum_{i \in I_{j}} g_{i})w_{j} + \frac{1}{2}(\sum_{i \in I_{j}} h_{i})w^{2}\_{j} + \frac{1}{2}\lambda w_{i}^{2} + \gamma L\end{align}

Since all the weights are independent of each other (independently obtained), the objective for a particular leaf can be written as
\begin{align}
    obj_{j} &= (\sum_{i \in I_{j}} g_{i})w_{j} + \frac{1}{2}(\sum_{i \in I_{j}} h_{i})w^{2}\_{j} + \frac{1}{2}\lambda w_{i}^{2}\newline
    &= (\sum_{i \in I_{j}} g_{i})w_{j} + \frac{1}{2}(\sum_{i \in I_{j}} h_{i} + \lambda)w^{2}\_{j}\newline
    &= G_{j} w_{j} + \frac{1}{2} (H_{j} + \lambda)w_{j}^{2}\newline
    where, G_{j} &= \sum_{i \in I_{j}} g_{i}\newline
    H_{j} &= \sum_{i \in I_{j}} h_{i}\end{align}

This is a quadratic in $w_{j}$ and the optimal value is
\begin{align}
    w^{\ast}\_{j} = -\frac{G_{j}}{H_{j} + \lambda}\end{align}

which can be evaluated if we know the first and second derivatives of the loss function. This way, custom loss functions can also be optimized if these two are known in advance.


The objective at these optimal values of $w$ become
\begin{align}
    obj^{\ast} = &= \sum_{j=1}^{L} G_{j}w^{\ast}\_{j} + \frac{1}{2}(H_{j}+\lambda)(w^{\ast}\_{j})^{2} + \gamma L\newline
    &= \sum_{j=1}^{L} -\frac{1}{2}\frac{G^{2}\_{j}}{H_{j} + \lambda} + \gamma L\end{align}
where, the smaller the objective, better is the tree.


Now, building the tree levelwise, the split at any level should be such that the difference between the objective at the splits and the current node is as large as possible. Terming this as gain, and denoting Left and Right as the two leaves obtained after a split,
\begin{align}
    gain &= \text{objective at current node} - \text{total objective at split nodes}\newline
    &= (-\frac{1}{2} \frac{(G_{Left} + G_{Right})^{2}}{(H_{Left} + H_{Right}) + \lambda} + \gamma) - \big( (-\frac{1}{2} \frac{G_{Left}^{2}}{H_{Left} + \lambda} + \gamma) + (-\frac{1}{2} \frac{G_{Right}}{H_{Right} + \lambda} + \gamma) \big)\newline
    &= \frac{1}{2} \bigg[ \frac{G_{Left}^{2}}{H_{Left} + \lambda} + \frac{G_{Right}}{H_{Right} + \lambda} - \frac{(G_{Left} + G_{Right})^{2}}{(H_{Left} + H_{Right}) + \lambda} \bigg] -\gamma\end{align}

We could write $G$ in the current node as $G_{Left} + G_{Right}$ since it is the sum of $g$ across all data points, which is the same as total sum of $g$ for the left and right trees. The same is true for $H$.


To find the optimum split, we can precalculate the values of $g$ and $h$ for all the points in the current node, and then do a scan from left to right on the values of a given variable to check the value of gain across different splits and locate the best performing one.


An important observation here is that $\lambda$ comes in denominator. Thus, if its value is high, the weights will automatically become low. Further, if the gain is not higher than $\gamma$, adding the split to the tree is not beneficial. This automatically does some pruning while building the tree.

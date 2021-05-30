---
title: "Regression Trees"
---

## Regression Trees

The algorithm behind building trees consists of two basic steps

1.  Divide the predictors $X_{1}, X_{2}, \ldots, X_{n}$ into $J$ **distinct** and **non-overlapping** regions $R_{1}, R_{2}, \ldots, R_{J}$.

2.  For making a prediction in the region $R_{j}$, simply take the **response mean** of all the data points following in that region.

With the above definition, the loss becomes
\begin{align}
        RSS = \sum_{j=1}^{J} \sum_{i \in R_{J}} (y_{i} - \bar{y}\_{R_{J}})^{2}
    \end{align}
But minimizing this loss is infeasible in practice as the total number of possible partitions are too large !


To overcome this, we build the trees in a greedy top down approach called **recursive binary splitting**. This method aims to find the best possible split at each level in a greedy manner.


### The Algorithm

To start off, the alogithm will try to split the data into two regions $\{X|X_{j} < s\}$ and $\{X|X_{j} \geq s\}$ using the values of predictor $X_{j}$ and the search is performed across all the predictors to choose the one which minimizes the RSS. Mathematically
\begin{align}
        R_{1}(j,s) = \{X|X_{j} < s\} \text{ and } R_{2}(j,s) = \{X|X_{j} \geq s\}\newline
        \minimize_{j, s} \sum_{i:x_{i} \in R_{1}} (y_{i} - \bar{y}\_{R_{1}})^{2} + \sum_{i:x_{i} \in R_{2}} (y_{i} - \bar{y}\_{R_{2}})^{2}
    \end{align}
where $\bar{y}\_{R_{1}}$ and $\bar{y}\_{R_{2}}$ are the response mean in the region $R_{1}$ and $R_{2}$ respectively.


The same algorithm is run recursively. The only change made after the first split is that we now work independently on two separate regions. For each region, we will not be able to consider all the possible values of $s$ since the region has been restricted. Otherwise, the RSS term will remain the same.


The process is stopped when a pre-determined stopping criteria is reached, such as minimum node size or depth (typically the tree is grown to a large depth and then pruned). For making a prediction, we will first determine the region in which the test observation falls and then make the prediction based on the mean of the training samples in this region (which has already been calculated while building the tree).


At the first split, $O(pNlog(N))$ cost is needed to sort all the predictors. Then at each split, another $O(pNlog(N))$ cost must be spent to find the best predictor among all the predictors. Further, this cost will be much higher in case we use multiple splits at each level instead of binary splits. The multiple splits can anyways be captured in multiple levels of a binary tree. Hence we stick with binary trees due to easy and efficieny of implementation and computations.

### Tree Pruning

The tree build using above strategy can have good results on the training set, but will yield poor performance on the test set due to the high complexity. A better strategy is to build **short trees which are less complex and produce lower variance at cost of little bias** and are more interpretable.


A simple strategy can be to build only when there is a decrease in RSS above a threshold. This approach can be short-sighted as some future good branches can be missed.


Tree pruning is to **build a large tree and then shrink it back to obtain a subtree**. The RSS of a subtree can be found via cross validation. This approach is expensive for all possible subtrees.


**Cost complexity Pruning** or **weakest link pruning** is an approach to overcome this problem. For a non-negative parameter $\alpha$, there exists a subtree $T$ of the large tree $T_{0}$ such that the following is minimized
\begin{align}
        RSS = \sum_{m=1}^{\vert T \vert} \sum_{i:x_{i}\in R_{m}} (y_{i} - \bar{y}\_{R_{m}})^{2} + \alpha \vert T \vert
    \end{align}
where $\vert T \vert$ is the number of terminal nodes in the tree. The formulation is similar to lasso and here we are controlling the complexity of the tree via a parameter $\alpha$. Larger the $\alpha$, the less number of terminal nodes there would be in the tree.


The same formula is valid for any of the internal nodes/subtrees also. Hence, for a given $\alpha$, we start pruning the tree starting with the terminal node that has the lowest reduction in the error metric (also called weakest link pruning). For a given $\alpha$ we obtain a sequence of subtrees and select the one with the minimum overall cost.


The algorithm can then be summarized as follows

1.  Use *binary recursive splitting* to obtain a large tree on the data set. Stop only when at a terminal node, the number of observations is less than a minimum.

2.  Apply *cost complexity pruning* in order to obtain a sequence small trees $T$ and choose the best $T_{\alpha}$ with the minimum cost associated with the parameter $\alpha$.

3.  Use K-fold cross validation to choose $\alpha$. For each of the folds $k = 1, 2, \ldots, K$

    1.  Repeat steps 1 and 2 excluding the data from the $k$th fold to obtain a family of subtrees as a function of $\alpha$.

    2.  Evaluate the mean predicted validation error as a function of $\alpha$.

        Choose the value of $\alpha$ that minimizes the average error across all the folds.

4.  Select the substree $T_{\alpha}$ from step 2 (trained on the whole dataset) that corresponds to the chosen value of $\alpha$.

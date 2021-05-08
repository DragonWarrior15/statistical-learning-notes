---
title: "Classification Trees"
---

## Classification Trees

Here we predict a qualitative variable and will report the **most occurring class in the region**. Since we are almost always also interested in the probabilistic aspects of the prediction, we also consider **the proportion of the classes occurring in a region**.

### The Algorithm

The algorithm is almost similar to the regression trees but instead of RSS, we need to use something that is related to class proportions and frequencies. Different types of metrics are available

*   **classification error rate** $= 1 - \max_{k}\hat{p}\_{mk}$ where $\hat{p}\_{mk}$ is the proportion of the $k$th class in the $m$th region. However, in practice, this metric is not sufficient to grow the trees.

*   **Gini Index**

    $G = \sum_{k=1}^{K} \hat{p}\_{mk} (1 - \hat{p}\_{mk}) = 1 - \sum_{k=1}^{K} p_{k}^{2}$ for a given region. In the case of binary classification, this formula becomes $G = 2p(1-p)$ where $p = p(Y=1 \vert X)$. Clearly, $G$ is close to zero when the node is pure, i.e. most of the observations come from the same class. Gini index is also know as a measure of **purity** since it's low value implies predominance of a single class in the node.

*   **Entropy** $D = \sum_{k=1}^{K} -\hat{p}\_{mk} \log(\hat{p}\_{mk})$ for a region. Entropy takes value close to zero if the class probabilities are close to $0$ or $1$. Gini index and Entropy are somewhat similar numerically.

In addition to these impurity measures, we also need to weight the two left and right nodes based on the number of observations $N_{L}$ and $N_{R}$, since purifying a large node is preferable than ultra purifying a small node.


Gini Index and entropy are preferable when going a tree because they are differentiable and thus friendly to numerical optimization. Also, entropy is slightly computationally expensive to compute due to the logarithm. Hence, most packages will prefer gini index over entropy.

For pruning a tree, all three work and misclassification rate is frequently used.

#### Categorical Predictors

The classes of a categorical predictor can be ordered based on the mean of the response (in case of classification trees, the mean of response is simply the fraction of 1s in that class). To use in a tree, we simply use this transformed version similar to continuous variable. The best split point is chosen and all classes with higher response mean fall on one side and the remaining on the other. This simple trick helps avoid checking all possible spilts with differing number of classes on each side (Proof can be found in Breiman et al. (1984) and Ripley (1996)). Larger number of classes help find better split point but also have a higher risk of overfit since examples in a particular class might become less.

#### High Variance

High variance is inherent to trees due to the nature of their construction. Slight changes in the data can cause an entirely different tree to be built. Errors at any level are propagated to all the levels below. This can cause instability in making interpretation and prediction. Bagging is an approach that helps alleviate the problem of variance at a slight cost of interpretability.

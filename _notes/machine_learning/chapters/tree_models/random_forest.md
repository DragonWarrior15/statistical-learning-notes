---
title: "Random Forest"
---

## Random Forest

Random forests overcome the problem of **decorrelation** in bagging. The trees built using bagging are similar because if there is a strong predictor, we expect it to dominate the splits in each of the trees and give similar trees.


From the variance equation derived in [bagging]({{ "/notes/machine_learning/chapters/tree_models/bagging.html" | relative_url}}), with large number of trees $B$, the aim is to reduce $\rho$ to get significant reduction in $\sigma^{2}$. **Random Forests achieve decorrelation by using only a subset of variables for each split (typically $m = \sqrt{p}$)**. This subset is chosen randomly at each split to ensure that the trees differ enough in structure to give less correlated predictions. **The performance improvement through random forests is solely the result of variance reduction** since each individual tree is achieving low bias.


Similar to bagging, **random forests will not overfit if we increase the number of trees $B$**. Hence, the choice can be made based on whether the reduction in test error is sufficient. Although, too many trees may start to make the model too rich, causing the development of correlated trees which increases variance. Thus, the main difference between bagging and random forest is the random choice of variables at split points in random forest. Reducing $m$ will reduce the correlation between the trees. However, too much reduction in $m$ may cause an increase in bias.


As the ratio of relevant variables to noise variables in the data decreases, the gap between random forests and boosting grows because at each split, the probability of selection of random variables becomes low. However, as this probability goes up, random forest catches up to boosting quickly.


In practical use, the concepts of random forest/bagging benefit non linear estimators the most due to the low bias and high variance of individual trees.

### Algorithm

1.  For $b = 1 \text{ to } B$

    1.  Select a bootstrap sample $Z^{\*}$ of size N from the data

    2.  Recursively build the decision tree $T_{b}$ using the following rules until any of the tree constraints is broken

        1.  Select a subet of $m$ variables out of $p$

        2.  Choose the best variable for split using predefined criteria

        3.  split the node into two child nodes

2.  Output the ensemble of trees $\{T_{b}\}\_{1}^{B}$

3.  Make predictions according to the following

    -   Regression: $\hat{f}\_{rf}^{B}(x) = \frac{1}{B}\sum_{b=1}^{B} T_{b}(x)$

        By the inventors, default $p = \lfloor p/3 \rfloor$ and minimum node size of $5$

    -   Classification: $\hat{C}\_{rf}^{B}(x) =$ _majoirty vote_ $\{\hat{C}\_{b}(x) \}\_{1}^{B}$

        where $\hat{C}\_{b}(x)$ is the class prediction by a single tree and $\hat{C}\_{rf}^{B}(x)$ is the class prediction by the random forest.

        By the inventors, default $p = \lfloor \sqrt{p} \rfloor$ and minimum node size of $1$

But note that $m$ and node size are both hyperparameters and the best values will vary between datasets.


Similar to section on [out of bag error]({{ "/notes/machine_learning/chapters/tree_models/bagging.html#out-of-bag-error" | relative_url}}), we can use the samples not used for training a tree to calculate the out of bag error for that tree and consequently the forest. This can be used as an indicator to decide when to stop training.

### Variable Importance

The relative variable importance is calculated using the total improvement in split criteria across all the trees
\begin{align}
        \mathcal{I}\_{l}^{2}(T) &= \sum_{t=1}^{J-1} \hat{i}\_{t}^{2}I(node(t) = l) \quad \text{the sum only includes the splits}\newline
        \mathcal{I}\_{l}^{2} &= \frac{1}{B}\sum_{b=1}^{B} I_{l}^{2}(T_{b})
    \end{align}
where $\hat{i}\_{t}^{2}$ is the square of improvement criteria at node $t$ of the $T^{th}$ tree, and $I_{l}^{2}(T)$ is the importance at the $T^{th}$ tree. Since these are relative importance values, usually the variable with maximum importance is assigned a score of 100 and the remaining values of importances are scaled accordingly.


Another importance criteria uses the out of bag samples. Whenever a tree is grown, the oob sample is passed down the tree and the accuracy is recorded. Then, the $j^{th}$ variable is randomly permuted in this sample and the accuracy is again recorded. This decrease in accuracy is averaged across all trees to get the accuracy value for that variable. The results are finally shown as a percent of the maximum. This gives more uniform importances. Note that we are not setting a variable to zero, but randomly permuting it.

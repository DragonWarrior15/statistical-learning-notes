---
title: "Boosting Trees"
---

## Boosting Trees

The following section defines $N$ as the total number of training data points and $M$ as the total number of trees/boosting rounds.

A tree can be defined and prepared in the following manner
\begin{align}
    f(x_{i}) = \gamma_{j} \text{ if } x_{i} \in R_{j} \text{, where } R^{j} \text{ are partitions of input space}\newline
    T(x_{i}; R, \gamma) = \sum_{j=1}^{J} \gamma_{j} I(x_{i} \in R_{j})\newline
    R, \gamma = \argmin_{R, \gamma} \sum_{j=1}^{J} \sum_{x_{i} \in R_{j}} L(y_{i}, \gamma_{j})\newline
    \text{A more simpler form} \quad R, \gamma = \argmin_{R, \gamma} \sum_{i=1}^{N} L(y_{i}, T(x_{i}; R, \gamma))\end{align}

$\gamma_{j}$ for $R_{j}$ is simply the quantity that minimizes the error averaged over all $x_{i} \in R_{j}$. For regression, this is simply the mean of the node (to minimize the mean squared loss) and for classifictation, the majority class (to minimize the misclassificaion rate). To build the tree, we recursively partition the data into two regions such that the partitioning results in a decrease in the above error function.


The stagewise additive model then becomes
\begin{align}
    f_{M}(x) &= \sum_{j=1}^{J} T(x; R_{m}, \gamma_{m})\newline
    R_{m}, \gamma_{m} &= \argmin_{R_{m}, \gamma_{m}} \sum_{i=1}^{N} L(y_{i}, f_{m-1}(x_{i}) + T(x_{i}; R_{m}, \gamma_{m})) \quad \text{(1)}
\end{align}

If the regions are already known, the above equation simplifies to
\begin{align}
    \gamma_{m,j} = \argmin_{\gamma_{m,j}} \sum_{x_{i} \in R_{j}} L(y_{i}, f_{m-1}(x_{i}) + \gamma_{m,j}) \quad \text{(2)}
\end{align}

For regression problems, equation (1) is easily solvable since the minimzer of a given region is simply the average of $y$ in that region. Hence, we can scan over the variables to find the optimum split that minimizes this loss. For absolute loss, the minimizer is the median.


For classification problems with the exponential loss, this equation is same as the adaboost algorithm discussed in [adaboost]({{ "/notes/machine_learning/chapters/tree_models/adaboost.html" | relative_url }}) with the restriction that the output of any tree is $\in \{-1,1\}$.

### Gradient Descent

For any loss function for a given output function,
\begin{align}
    L(f) &= \sum_{i=1}^{N} L(y_{i}, f(x_{i}))\newline
    \mathbf{f}(x) &= \argmin_{f(x_{1}), f(x_{2}), \ldots, f(x_{N})} \sum_{i=1}^{N} L(y_{i}, f(x_{i}))\end{align}

where we have denoted $\mathbf{f}(x)$ as a vector in $\mathbb{R}^{N}$ space. Thus, minimizing the loss function is finding the minima in this $\mathbb{R}^{N}$ space. We can do this using gradient descent. Gradient descent will take multiple steps until it is able to reach the minima
\begin{align}
    \mathbf{f}\_{M}(x) = \sum_{m=1}^{M} \mathbf{h}\_{m}(x) \quad \text{where} \quad \mathbf{h}\_{m}(x) \in \mathbb{R}^{N}\end{align}

and $\mathbf{h}\_{m}(x)$ are steps taken in such a way to reduce the loss. Thus, the final $\mathbf{f}(x)$ is simply a sum of these small steps. We usually start with $\mathbf{f}(x) = \mathbf{h}\_{0}(x)$ as an initial guess.


At any point $m$, the gradient can be chosen as $\mathbf{h}\_{m} = -\rho_{m} \mathbf{g}\_{m}$ where $\rho_{m}$ is a scalar and the gradient $\mathbf{g}$ is calculated across all $i$ data points
\begin{align}
    g_{i, m} = \bigg[ \frac{\partial L(y_{i}, f(x_{i}))}{\partial f(x_{i})} \bigg]\_{f=f_{m-1}}\end{align}

The solution to $\rho_{m}$ and the update of $\mathbf{f}$ then become
\begin{align}
    \rho_{m} &= \argmin_{\rho} L(y, \mathbf{f_{m}} - \rho \mathbf{g}\_{m})\newline
    \mathbf{f}\_{m} &= \mathbf{f}\_{m-1} - \rho_{m} g_{m}\end{align}

But, the problem is that for any new data point, the gradient will not be known since the target value is not available. Hence, we try to predict this gradient using a tree and then calculate $f_{m}(x)$ to make the desired prediction. Predicting gradient is a regression problem
\begin{align}
    R, \gamma = \argmin_{r, \gamma} \sum_{i=1}^{N} (-g_{i,m} - T(x_{i}; R, \gamma))^{2}\end{align}

which has fast algorithms using regression trees. Note that the tree is built using gradient as the target, but $\gamma$ is calculated from equation (2).

### Gradient Boosting Algorithm

1.  Initialize $f_{0}(x) = \argmin_{\gamma} \sum_{i=1}^{N} L(y_{i}, \gamma)$

2.  For $m=1$ to $M$

    1.  For all points $i = (1, 2, \ldots, N)$, calculate gradient
        \begin{align}
                    g_{i, m} = \bigg[ \frac{\partial L(y_{i}, f(x_{i}))}{\partial f(x_{i})} \bigg]\_{f=f_{m-1}}
                \end{align}

    2.  Prepare a regression tree on the negative of gradients
        \begin{align}
                    R_{m}, \gamma_{m} = \argmin_{R, \gamma} \sum_{i=1}^{N} (-g_{i,m} - T(x_{i}; R, \gamma))^{2}
                \end{align}
        to get the terminal regions/nodes of the tree $R_{j}, j=1,2,\ldots,J$

    3.  Calculate the $\gamma$ on the above regions
        \begin{align}
                    \gamma_{m,j} = \argmin_{\gamma_{m,j}} \sum_{x_{i} \in R_{m,j}} L(y_{i}, f_{m-1}(x_{i}) + \gamma_{m,j})
                \end{align}

    4.  Update $f(x)$
        \begin{align}
                    f_{m}(x) = f_{m-1}(x) + \sum_{j=1}^{J} \gamma_{m,j} I(x \in R_{m,j})
                \end{align}

3.  Return $f_{M}(x)$ (and the regions if required)

The procedure is called Gradient Boosting since the procedure of boosting is applied on the gradients obtained at each step (since we are effectively building trees to correctly predict the gradient).


Further note that $\gamma$ calculated above is essentially $\rho g_{m}$ from previous gradient descent section. Thus, we first use least squares to get approximation of gradient as well as the regions of the tree, and then minimize the actual loss function to assign values to those regions/approximate correct gradient for the loss function in those regions.

### Boosting Parameters

#### Tree Size

Ideally, we would build the tree as large as possible, and then prune it. This gives trees of varying sizes along the boosting iterations and also makes the whole process computationally inefficient. To avoid this, we simply restrict the size of all trees to be the same as $J$ from the start.


The size of the tree captures the level of interactions among variables we are allowing to be represented. A decision stump only allows the direct effect of the variable to be captured. Tree of size $3$ will allow second order interactions to also be captured. Thus, $J$ should reflect the degree of interaction we permit in the model. Typically, $J>10$ is too large and rarely useful. $4 \leq J \leq 8$ should suffice in most conditions, with $J=6$ being a good starting point in such cases.

#### Number of Trees M

Clearly, increasing $M$ will keep on reducing the error on the training data. Thus, a good idea is to use a validation set and monitor the changes in validation error to determine the best value for $M$. This is analogous to early stopping in neural networks.

#### Learning Rate

Apart from controlling $M$ to prevent overfitting, we can also control a shrinkage parameter
\begin{align}
    f_{m}(x) = f_{m-1}(x) + \nu \sum_{j=1}^{J} \gamma_{m,j} I(x \in R_{m,j})\end{align}

where $\nu$ is the amount by which we are scaling the contribution of each successive tree into the final model. Typically, $\nu < 0.1$ performs really well in practice. Note that the lower we make the contribution of individual trees into the model, the longer we need to train the model. Thus, $\nu$ and $M$ have an opposite effect on each other. Typically boosting will involve small trees and large $M$ should not pose much difficulty.


Low $\nu$ values give good improvements in mean squared loss and classification loss. However, not much improvement in seen for misclassification error loss. This stagewise shrinkage for boosting trees is similar to the $L1$ penalty in some respects. The best strategy to choose $\nu$ and $M$ is to first determine $\nu$ for a fixed $M$ and then choose $M$ by early stopping. $\nu$ is also useful in stabilizing the model for training.

#### Subsampling

**Stochastic Gradient Descent** is the other name for this modified technique where at every stage when building a tree, we sample a fraction of the population ($\eta = 1/2$ or lower if large data set) with replacement (similar to bagging). This helps in reducing some variance due to the noisy trees, reduces training time, and usually gives superior results.


Usually, subsampling will work best with some shrinkage as well. Subsampling without shrinkage gives poor results.

### Interpretation

A decision tree assigns the same value to all the data points that fall in the same region. Thus, when partitioning a given region into two regions using a variable, the two new regions have two different value as outputs for data points falling in those regions. Thus, the change in the loss function using a variable as a partition is given by
\begin{align}
    \hat{i}\_{j} &= \big( \sum_{x_{i} \in R_{j, 1}} \gamma_{j,1} + \sum_{x_{i} \in R_{j, 2}} \gamma_{j,2} \big) - \sum_{x_{i} \in R_{j}} \gamma_{j}\newline
    R_{j} &= R_{j,1} \cup R_{j,2} \quad \text{is obtained by paritioning on variable $l$}\end{align}
where $\gamma$ are obtained by minimizing the loss function across the points $x_{i} \in R_{j}$. Thus, this quantity can be seen as a proxy for importance, by checking how much reduction in loss function is this variable able to bring. The partitioning is done by choosing the variable which gives the maximum reduction.


This reduction in loss is used as an indicator for importance
\begin{align}
     \mathcal{I}\_{l}^{2}(T_{m}) = \sum_{j=1}^{J-1} \hat{i}\_{j} I(v(j) = l)\end{align}
where $v(j)$ is the variable selected for split at the $j^{th}$ node, and the sum is only calculated over the $J-1$ internal nodes of the tree. The total importance across the $M$ trees becomes
\begin{align}
    \mathcal{I}\_{l}^{2} = \frac{1}{M}\sum_{m=1}^{M} \mathcal{I}\_{l}^{2}(T_{m})\end{align}

The actual importance is the square root of this value. Since the importance is relative, by convention, the most important variable is given the importance of 100, and the remaining variables are appropriately scaled with respect to this.


In case of multiple classes, we first sum the importance of a variable in a given class across all the trees, and then average out this value across the classes to get a single value.

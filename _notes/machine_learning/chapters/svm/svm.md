---
title: Support Vector Machines
---

## Support Vector Machines

Support vector machines take the idea of SVCs to the non linear boundary case. It is easier to find linear separation boundaries in higher dimensional space as the points are more farther apart. One way is to directly use the transformed feature space to train the model. The problem is that this increases computations by a huge factor due to the increased dimensionality of the features and the parameters.


SVM benefits from the kernel trick which comes into picture in the Wolfe-dual problem
\begin{align}
        L = \sum_{j=1}^{N}\lambda_{j} - \frac{1}{2} \sum_{i=1}^{N}\sum_{j=1}^{N} \lambda_{i}\lambda_{j}y_{i}y_{j}c
    \end{align}
where $h(x):\mathbb{R}^{p} \rightarrow \mathbb{R}^D$. The parameters learnt will be in the new feature space. But we can make the prediction easily by using
\begin{align}
        \beta &= \sum_{j=1}^{N} \lambda_{j}y_{j}h(x_{j})\newline
        y(x_{new}) &= \beta^{T}h(x_{new}) + \beta_{0}\newline
        &= \sum_{j=1}^{N} \lambda_{j}y_{j}h(x_{j})^{T}h(x_{new}) + \beta_{0}
    \end{align}
Notice that both training and prediction depend on the dot products of the transformed features, and not on the transformed features themselves. Furthermore, we know that only a subset of training points (which are on margin or between margins) will have the coefficient $\lambda_{j} = 0$. We know this subset from training data and computation for new points becomes quite cheap.

To compute the dot products, it is sufficient to know the kernel rather than individual transformed features
\begin{align}
        K(x_{1}, x_{2}) = h(x_{1})^{T}h(x_{2})
    \end{align}

which is cheap to compute for several functions. The kernel is easy to view as measuring similarity between points. When we use the kernel on original space, we are looking at the Pearson correlation coefficient. Also, we save a ton of computational time. Using kernels, we only need to compute the similarity between $\binom{N}{2}$ pairs of variables. On the other hand, when working in large dimensional spaces, we would have first calculated the transformed features, and then the dot products.


Popular choices of Kernels to explore when using SVM are
\begin{alignat}{2}
        \text{$d^{th}$ degree Polynomial :} &\quad K(x_{1}, x_{2}) &&= (1 + x_{1}^{T}x_{2})^{d}\newline
        \text{Radial Basis :} &\quad K(x_{1}, x_{2}) &&= exp(-\gamma \lVert x_{1} - x_{2} \rVert^{2})\newline
        \text{Neural Network :} &\quad K(x_{1}, x_{2}) &&= tanh(k_{1} x_{1}^{T}x_{2} + k_{2})
    \end{alignat}
where $\gamma>0$, $k_{1}$ and $k_{2}$ are predefined constants.


The radial basis function is special in the sense that the transformed feature space is infinite dimensional, but we do not need to work in that space. For large difference in two inputs, the kernel returns a small value, in line with the SVC principal to give low importance to the points far away.


The cost parameter $C$ serves better in the larger space. Large $C$ causes small $\epsilon$ leading to overfit in the original feature space (non-linear wiggly boundary) while smaller values of $C$ will lead to smoother boundary in the original space. The value is optimally chosen through cross validation.

### Hinge Loss

The slack variables $\epsilon$ are positive. They are $0$ when the points are correctly classified, and begin to increase the further we move away from margin in the misclassification region. Hence,
\begin{align}
        &\frac{1}{2}\lVert \beta \rVert^{2} + C\sum_{j=1}^{N}\epsilon_{j}\newline
        &\text{is equivalent to} \quad \frac{1}{2C}\lVert \beta \rVert^{2} + \sum_{j=1}^{N} max(0, 1 - y_{j}(\beta_{0} + \beta^{T}x_{j}))
    \end{align}

where we have simply divided the whole equation by $C > 0$. The term is a familiar combination of $loss + penalty$ (ridge or lasso for instance). The hinge loss is defined as $max(0, 1 - yf(x))$ for the case of SVM.

##### Multiclass classification

in $K$ classes can be done either by building $\binom{K}{2}$ classifiers and choosing the class most frequently chosen for a given point, or using $K$ one vs all classifiers, and using the one giving maximum value of $\beta_{0} + \beta^{T}x$.

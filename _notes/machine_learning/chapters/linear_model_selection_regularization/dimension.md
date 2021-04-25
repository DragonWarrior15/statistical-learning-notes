---
title: "Dimension Reduction Methods"
---

## Dimension Reduction Methods

The methods seen above achieve reduction in variance by either reducing the number of variables being used for estimation, or reduce the value of coefficients of those variables.

Dimensionality reduction uses a **linear map** to convert the original $p$ variables to $M$ variables where $M < p$.
\begin{align}
        Z_{m} &= \sum_{j=1}^{p} \phi_{jm}X_{j} \quad \text{where $\phi_{jm}$ are constants} \newline
        RSS &= \sum_{i=1}^{n} (y_{i} - (\theta_{0}+\sum_{m=1}^{M}\theta_{m}Z_{m}))^{2} \quad \text{where $\theta_{m}$ are linear regression coefficients for $Z_{m}$}
    \end{align}
This new formulation restructures the original least squares formula. The whole process now is

-   Obtain the linear map using techniques like PCA

-   Use least squares on the transformed predictors to obtain regression estimates

### Principal Components Analysis (PCA)

PCA is one of the most common methods used for dimensionality reduction. It is based on the principle of finding those directions that **maximize the variance of data**. The intuition behind finding this direction is that this separates the data best given the high variance. Hence, the performance of a classifier/regressor would be better if the training was done using the transformed predictors.


Assume that we want to find $M$ components for PCA, where $M <= p$. Then,

1.  Find the direction/projection of the data that gives the maximum variance under the constraint $\sum_{j=1}^{p}\phi_{jm}^{2} = 1$ (normalized vector) for obtaining the $m^{th}$ transformed predictor

2.  If the total components found is $< M$, repeat step 1 with the added constraint that the next component has zero correlation with the previous component

This constraint of finding components with zero correlation essentially means that in the multidimensional space, we are finding a set of **orthogonal vectors**. The order of choosing the new predictors is in decreasing order of the information they contain. Thus, the first predictor will now contain the most information.


##### Derivation of PCA

It is a good idea to **standardize/scale the variables before running PCA**. Not only is it easier to derive the components, but they are also unaffected by the scale of the individual variables (since we know that scaling a variable multiplies the variance by square of the scaler and PCA is all about finding maximum variances !). If the variables represent same/similar quantities with similar scales, scaling is not mandadtory. However, we usually have data consisting of several quantities measured on different scales and thus scaling comes in handy. Scaling can be done to get the data in $[0,1]$ or by divinding by $\sigma$ to get similar scale.


After setting the the mean of all predictors to zero and standard deviation to one, the components can be derived by considering the following optimization problem
\begin{gather}
        \maximize_{\phi_{11},\ldots,\phi_{p1}} \left\\{ \frac{1}{n} \sum_{i=1}^{n} (\sum_{j=1}^{p}\phi_{j1}x_{ij})^{2} \right\\} \text{ subject to } \sum_{j=1}^{p} \phi_{j1}^{2} = 1\newline
        \text{Or, } \maximize_{\Phi_{1}} \frac{1}{n} Z_{1}^{T}Z_{1} \text{ subject to } \sum_{j=1}^{p} \phi_{j1}^{2} = 1\newline
        \text{Where } Z_{1} = X\Phi_{1}\newline
        \text{Define the Lagrangian } L(\Phi_{1}, \lambda) = \frac{1}{n} (\Phi_{1}^{T}X^{T}X\Phi_{1}) - \lambda (\Phi_{1}^{T}\Phi_{1} - 1)\newline
        \frac{\partial L(\Phi_{1}, \lambda)}{\partial \lambda} = 0 \text{, and } \frac{\partial L(\Phi_{1}, \lambda)}{\partial \Phi_{1}} = 0 \newline
        \text{Giving, } 2\frac{1}{n}(\Phi_{1}^{T}X^{T}X) - 2\lambda \Phi_{1}^{T} = 0 \text{ and } \Phi_{1}^{T}\Phi_{1} - 1 = 0\newline
        \frac{X^{T}X}{n}\Phi_{1} = \lambda \Phi_{1}\newline
        \text{Since all } X_{i} \text{ are centered, } \frac{X^{T}X}{n} \text{ is the covariance matrix } \Sigma_{X}\newline
         (=E[(X-E[X])^{T}(X - E[X])] \text{since we want $p\times p$ dimension})\newline
        \Sigma_{X} \Phi_{1} = \lambda \Phi_{1} \text{ with } \Phi_{1}^{T}\Phi_{1} = 1\newline
    \end{gather}
Which is nothing but the **Eigenvectors of the Covariance Matrix of $X$**. Notice that the maximization is achieved through the eigenvector with the highest eigenvalue. Since $\Sigma_{X}$ is positive semi-definite, all the eigenvalues will be $\geq 0$.

Furthermore, we know that all eigenvectors are orthogonal to each other, and hence they will also satisfy the condition that all the linear mapping vectors are not correlated to each other.

If we try to find the coefficients for $Z_{2}$, we are looking at the exact same optimization, but with the additional constraint that $\Phi_{2}$ is not correlated to $\Phi_{1}$. This will yield the second eigenvector of the covariance matrix.

Hence, **the linear maps for obtaining the PCA transformations are nothing but the eigenvectors of the covariance matrix $\Sigma_{X}$ of the original data $X$**. We have a total of $p$ eigenvectors and thus, the maximum components obtainable is also $p$.

##### Explained Variance

The variance explained by the $m^{th}$ component is nothing but the ratio of variance of $Z_{m}$ and total variance of the data. Mathematically this is
\begin{align}
        \text{Explained variance of component } m &= \frac{\frac{1}{n}\sum_{i=1}^{n} (\sum_{j=1}^{p} \phi_{jm} x_{ij})^{2}}{\frac{1}{n}\sum_{i=1}{n} \sum_{j=1}{p} x_{ij}^2}\newline
                &= \frac{\frac{1}{n}Z_{m}^{T}Z_{m}}{tr(\frac{X^{T}X}{n})}\newline
                &= \frac{\Phi_{m}^{T}\frac{X^{T}X}{n}\Phi_{m}}{tr(\Sigma_{X})}\newline
    \end{align}
However, note that in the derivation, $\Phi_{m}$ is the eigenvector and thus, $(X^{T}X)\Phi_{m} = \lambda_{m}\Phi_{m}$ and $\Phi_{m}^{T}\Phi_{m} = 1$. Substituiting in the above equation,
\begin{align}
        \text{Explained variance } &= \frac{\lambda_{m}}{tr(\Sigma_{X})}\newline
        \text{or, } \text{Explained variance } &= \frac{\lambda_{m}}{\lambda_{1} + \cdots +\lambda_{p}}
    \end{align}
Where the last equation comes from the fact that the trace of a matrix is simply the sum of it's eigenvalues.

A **Scree Plot** is a plot between the explained variance and the index of the prinicple components. It's cumulative version can be used to determine the number of components to keep on the basis of how much of the total variance we want to explain. The elbow point of the Scree Plot can also help determine the components at which the explained variance drops significantly.

##### Principal Components Regression (PCR)

is simply using some $m$ out of $M$ components to perform linear regression. This approach will typically work best when a few components of the PCA sufficiently explain the whole data. This way we reduce the variance at the cost of slight change in bias. PCR can also be viewed as a continuous version of Ridge Regression.

### Partial Least Squares

This method is closely related to PCA/PCR. In the previous methods, an unsupervised approach was used to project the matrix $M$ onto a lower dimensional space. This transformation did not take $Y$, the response, into consideration. PLS will incorporate $Y$ as well for finding the transformations.

The algorithm is as follows

1.  Calculate the coefficients for the first component as the coefficient obtained by regressing $Y$ on $X_{j}$

2.  Using this component, regress $X_{j}$'s on $Z_{1}$ and get the residuals. These are the unexplained components of the variables.

3.  Calculate $Z_{2}$ using $Y$ and these residuals

4.  Repeate the process above till $M$ components are obtained

Though this procedure looks slightly more involved, it performs not better than lasso regression and PCR in practice. Although this method reduces bias, it also leads to quite an increase in variance as well, making the method not very useful.

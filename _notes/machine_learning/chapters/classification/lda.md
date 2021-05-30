---
title: "Linear Discriminant Analysis (LDA)"
---

## Linear Discriminant Analysis (LDA)

Why use LDA ?

-   When the **classes are well separated**, the parameter estimates for the **logistic regression** model are surprisingly **unstable**. **LDA** does not suffer from this problem and is relatively **stable**.

-   if **$n$ is small** and the distribution of **$X$ is approximately normal** in each of the classes, **LDA** is again **more stable** than logistic regression.

-   LDA is popular when we have **more than two classes**.

LDA first models the distribution of $X$ in each class, and then uses Bayes' rule to flip this and get $p(Y \vert X)$. When these distributions of $X$ are normal, the model is very similar in form to logistic regression.

### Model Derivation

Let the total number of classes be $K$ and the prior probability that a randomly chosen observation comes from the $k^{th}$ class be $\pi_{k} = P(Y=k)$. Also, let $f_{k}(x) = P(X=x \vert Y=k)$ denote the probability distribution function of $X$ for the data points belonging to the class $k$. By Bayes' Rule
\begin{align}
        \pi_{k} &= \frac{\text{Observations in class k}}{\text{Total observations}}\newline
        p(Y=k \vert X=x) &= \frac{P(Y=k)P(X=x \vert Y=k)}{P(X=x)}\newline
                &= \frac{P(Y=k)P(X=x \vert Y=k)}{\sum_{l=1}^{K} P(Y=l)P(X=x \vert Y=l)}\newline
                &=  \frac{\pi_{k}f_{k}(x)}{\sum_{l=1}^{K}\pi_{l}f_{l}(x)}
    \end{align}

### Gaussian Model with one Predictor

We assume the predictor to have a Gaussian distribution. For simplicity, also assume that the variances of $X$ for all the $K$ classes are also the same (fundamental assumption for linearity of decision boundary). Then,
\begin{align}
        f_{k}(x) &= \frac{1}{\sqrt{2\pi}\sigma}e^{\frac{(x-\mu_{k})^{2}}{2\sigma^{2}}}\newline
        p_{k}(x) &= \frac{\pi_{k}\frac{1}{\sqrt{2\pi}\sigma}e^{\frac{(x-\mu_{k})^{2}}{2\sigma^{2}}}}{\sum_{l=1}^{K}\pi_{l}\frac{1}{\sqrt{2\pi}\sigma}e^{\frac{(x-\mu_{l})^{2}}{2\sigma^{2}}}}
    \end{align}

For any given $x$, we notice that all $f_{k}(x)$'s have the same denominator. To assign a class, we just need to find the maximum value. Taking $\log$, removing the denominator and removing the parts corresponding to $x$ from numerator (since they are same across all classses),
\begin{align}
        \log{p_{k}(x)} \propto \log{\pi_{k}} + \frac{\mu_{k}^{2}}{2\sigma^{2}} - \frac{x\mu_{k}}{\sigma^{2}}
    \end{align}

In the case of two classes, the decision boundary can be found by equating the two $\log probabilities$ (assume the priors to be same for simplicity)
\begin{align}
        x\frac{\mu_{1}}{\sigma^{2}} - \frac{\mu_{k}^{2}}{2\sigma^{2}} &= x\frac{\mu_{2}}{\sigma^{2}} - \frac{\mu_{2}^{2}}{2\sigma^{2}} \newline
        \text{or, } x &= \frac{\mu_{1} + \mu_{2}}{2}
    \end{align}

$\mu_{k}$ and $\sigma^{2}$ need to be estimated from the data, which can be done through the following formulae ($n$ is total training examples and $n_{k}$ is total training examples from class $k$)
\begin{align}
        \hat{\mu}\_{k} &= \frac{1}{n_{k}} \sum_{i:y_{i}=k}x_{i}\newline
        \hat{\sigma}^{2} &= \frac{1}{N - K}\sum_{k=1}^{K}\sum_{i:y_{i}=k}(x-\hat{\mu}\_{k})^{2}
    \end{align}

### Multivariate Gaussian

A Multivariate Gaussian is an extension of the 1-D gaussian to multiple dimensions. Here, we assume that each of the individual dimensions is itself a Gaussian, with the different dimensions having correlation with each other, which are all specified in the correlation matrix.
\begin{align}
        X &\sim \mathcal{N}(\mu, \Sigma) \newline
        f(x) &= \frac{1}{(2\pi)^{p/2}\mid \Sigma \mid^{1/2}} \exp(-\frac{1}{2}(x-\mu)^{T}\Sigma^{-1}(x-\mu))
    \end{align}

Here, $\mu$ is the mean vector $\Sigma$ is the covariance matrix (symmetric).

Assume $\mu_{k}$ represents the mean vector for individual classes and we have a common covariance matrix across all classes. Plugging this into the LDA equation and removing the common part across all classes, the discriminant becomes
\begin{align}
        \log{p_{k}(x)} \propto \log{\pi_{k}} + x^{T}\Sigma^{-1}\mu_{k} - \frac{1}{2}\mu_{k}^{T}\Sigma^{-1}\mu_{k}
    \end{align}

To calculate the decision boundary, we simply do a pairwise equality between the discriminants of the individual classes and get the pairwise decision boundaries which are all linear.

### Quadratic Discriminant Analysis (QDA)

The assumption of same covariance matrix $\Sigma$ across all classes is fundamental to LDA in order to create the linear decision boundaries.

However, in QDA, we relax this condition to allow class specific covariance matrix $\Sigma_{k}$. Thus, for the $k^{th}$ class, $X$ comes from $X \sim \mathcal{N}(\mu_{k}, \Sigma_{k}$.

Plugging this into the classification rule to get the discriminants (removing denominators as they are common for all classes)
\begin{align}
        \delta_{k}(x) &= \log{\pi_{k}} -\frac{1}{2}\log{\mid\Sigma \mid} - \frac{1}{2}(x-\mu_{k})^{T}\Sigma_{k}^{-1}(x-\mu_{k}) \newline
        \text{Note that, } x^{T}\Sigma_{k}^{-1}\mu_{k} &= \mu_{k}^{T}\Sigma_{k}^{-1}x \text{  since $\Sigma$ is symmetric and $x^{T}\Sigma_{k}^{-1}\mu_{k}$ is scalar} \newline
        \delta_{k}(x) &= \log{\pi_{k}} -\frac{1}{2}\log{\mid\Sigma \mid} - \frac{1}{2}x^{T}\Sigma_{k}^{-1}x + x^{T}\Sigma_{k}^{-1}\mu_{k} -\frac{1}{2}\mu_{k}^{T}\Sigma_{k}^{-1}\mu_{k}
    \end{align}

Notice the term $x^{T}\Sigma_{k}^{-1}x$ that gives the classifier it's quadratic form.

However, since we are calculating individual covariance matrices for all the classes, we need to calculate more parameters than before which requires more data.

The following points about QDA vs LDA must be noted

-   QDA requires evaluation of substantially more parameters than LDA which subsequently means that more training data points must be available.

-   QDA will be superior if the decision boundaries are not linear, i.e., LDA's assumption of equal variances for all classes will not hold true which will cause LDA to have a higher bias.

-   QDA is more flexible than LDA which can reduce bias. However, bias-variance tradeoff implies that variance can be relatively higher for QDA if training examples are not sufficient.

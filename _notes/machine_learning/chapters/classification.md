---
title: "Classification"
---

# Classification

For more than two classes, it is hard to maintain the ordering between them using linear regression. For two classes however, linear regression can be used to prepare an ordering of the data (although difficult to interpret as probability themselves).

**Classification using linear regression to predict binary reponse will be same as Linear Discriminant Analysis (LDA).**


## Logistic Regression

Modelling binary response with linear regression might produce values outside the range $[0,1]$ ( and possibly negative as well). Hence we use a logistic function to compress the outputs to $[0,1]$ range.

\begin{align}
        p(Y=1 \vert X) = \frac{1}{1+e^{-(\beta_{0}+\beta_{1}X)}}\newline
        odds = \frac{p(Y=1 \vert X)}{1-p(Y=1 \vert X)} = e^{\beta_{0} + \beta_{1}X}
    \end{align}

-   The solution to this model is obtained via **Maximum Likelihood Estimation**.

-   Odds are also used to interpret probability. A low value of odds (close to $0$) indicates a low probability while a high value (close to $\inf$) indicates a high probability.

-   One unit change in $X$ will cause $\beta_{1}$ change in the $log\;odds$.

### Loss Function

**Maximum Likelihood** is used to determine the coefficients. Basic intuition is to choose such a pair of $\beta's$ that will make the predicted probability as close to the correct binary response ($0$ or $1$) as possible.

\begin{align}
        \text{Denoting} \quad p(x_{i}) &= P(Y = 1 \vert X = x_{i}) = 1/(1 + exp(-\beta^{T}x_{i}))\newline
        \text{likelihood function} &= l(\beta_{0},\beta_{1}) = \prod_{i:y_{i}=1} p(x_{i}) \prod_{i^{'}:y_{i^{'}}=0}(1-p(x_{i^{'}}))\newline
        \text{Taking logarithm, } logloss &= \sum_{i:y_{i}=1} \log p(x_{i}) + \sum_{i^{'}:y_{i^{'}}=0}\log (1-p(x_{i^{'}}))\newline
        &= \sum_{i=1}^{n} y\log p(x_{i}) + (1-y)\log (1+p(x_{i})) \tag\*{since $y = 0$ or $1$}\newline
        &= \sum_{i=1}^{n} y\beta^{T}x_{i} - log(1 + exp(\beta^{T}x_{i}))
    \end{align}
All the formulae listed here and above extend for the case of multiple variables, wherein we simply replace the sum $\beta_{0} + \beta_{1}X$ with $\beta_{0} + \beta_{1}X_{1} + \cdots + \beta_{p}X_{p}$.


For the below derivations, refer to the [appendix]({{ "/notes/machine_learning/chapters/appendix/matrix_logistic_reg.html" | relative_url }}) for complete matrix calculus
To solve for the $\beta$s, we consider the derivate of the *log likelihood*
\begin{align}
        \frac{\partial l}{\partial \beta} = \sum_{i=1}^{n} x_{i}(y_{i} - p_{i}) = 0
    \end{align}
which are $p-1$ non linear equations. We use the Newton-Raphson method and Hessian matrix for solving them
\begin{align}
        \frac{\partial^{2}l}{\partial \beta \partial \beta^{T}} &= -\sum_{i=1}^{n} x_{i}x_{i}^{T}p(x_{i})(1 - p(x_{i}))\newline
        \beta^{new} &= \beta^{old} - \bigg( \frac{\partial^{2}l}{\partial \beta \partial \beta^{T}} \bigg)^{-1} \frac{\partial l}{\partial \beta}
    \end{align}

Converting the above equations to function form for ease of obtaining solution
\begin{align}
        \frac{\partial l}{\partial \beta} &= X^{T}(y - \mathbf{p})\newline
        \frac{\partial^{2}l}{\partial \beta \partial \beta^{T}} &= -X^{T}WX\newline
        \text{where} \quad W &= diag([p(x_{1})(1-p(x_{1})), \ldots, p(x_{n})(1-p(x_{n}))])
    \end{align}

and the Newton-Raphson update becomes
\begin{align}
        \beta^{new} &= \beta^{old} + (X^{T}WX)^{-1} X^{T}(y - \mathbf{p})\newline
        &= (X^{T}WX)^{-1} X^{T}W(X\beta^{old} + W^{-1}(y - \mathbf{p}))\newline
        &= (X^{T}WX)^{-1} X^{T}Wz
    \end{align}
where $z$ is called the adjusted response (target in regression). The equation is same as equation [\[eq:linear_reg_solution\]](#eq:linear_reg_solution){reference-type="eqref" reference="eq:linear_reg_solution"} with an added weight term of $W$. Hence, this equation solves the weighted least squares problem
\begin{align}
        \beta^{new} = \argmin_{\beta} (z - X\beta)^{T}W(z - X\beta)
    \end{align}
and is known as *iteratively reweighted least squares* (IRLS). The equation converges since *log likelihood* is concave. In case of non convergence/huge jumps, reducing the step size helps.


Further, the above formulation allows us to get the distribution of $\beta$
\begin{align}
        \hat{\beta} \sim \mathcal{N}(\beta, (X^{T}WX)^{-1})
    \end{align}

Wald test, rao score test


In case of multiple classes, $y$ becomes a matrix of shape $n \times K$ and $W$ is non-diagonal, but the solution to IRLS is not simple. Methods like co-ordinate wise gradient descent works better.


### Deviance

LL denotes the log likelihood.

Deviance is a goodness of fit statistic and commonly employed for generalized linear models. It is a replacement of RSS in the context of maximum likelihood. Deviance is a bivariate function and satisfies $d(y,y) = 0$ and $d(y, u) > 0 \; \forall \; y \neq u$. For the total deviance $D(y, \hat{y})$ over a set of data with observed response $y$ and predicted response $y$, we sum up the individual deviances, $D(y, \hat{y}) = \sum_{i} d(y_{i}, \hat{y}\_{i})$.


The total deviance can be written in the log likelihood form
\begin{align}
        D(y, \hat{y}) &= -2(LL(\text{fitted model}) - LL(\text{saturated model})))\newline
                      &= -2 \times LL(\text{fitted model}) \quad \text{for logistic regression}
    \end{align}

where $\theta_{0}$ are the parameters of the fitted model, and $\theta_{s}$ are the parameters of the saturated model. A saturated model is the one where we have different parameters for each of the observations so that the model is fit exactly. $p$ is the joint probability.


##### Nested Models

is an important concept required to understand saturated models. A model is said to be nested within another model if the first model can be obtained by putting constraints on the parameters of the second model. For instance, a gaussian with $0$ mean is nested within any gaussian of single variable. Similarly, the regression $\beta_{0} + \beta_{1}x$ is nested within $\beta_{0} + \beta_{1}x + \beta_{2}x^{2}$.


Thus, the saturated model is an higher dimensional/unconstrainted version of the fitted model, and they belong to the same family of models. If we further constraint the fitted model to have a single parameter, we will call it the null model.


##### Null and Residual Deviance

are often discussed in the case of logistic regression and will be reported by a statistical software.
\begin{align}
         \text{Null Deviance} \quad &= \quad -2(LL(\text{fitted model}) - LL(\text{null model}))\newline
         \text{Residual Deviance} \quad &= \quad -2(LL(\text{fitted model}) - LL(\text{saturated model}))
    \end{align}

The coefficient of 2 allows both the deviances to have a $\chi^{2}$ distribution. Thus, the deviances can be used to calculate the *p-values* and decide whether the deviances are strongly evidenced by the data or not.


For logistic regression, the null model is an intercept only model
\begin{align}
        \text{Null Model}\; \rightarrow P(Y=1 \vert X) = \frac{1}{1 + exp(-\beta_{0})}\newline
        \beta_{0} = log \big( \frac{\text{count of 1s}}{\text{count of 0s}} \big), \quad p = \frac{1}{1 + exp(-\beta_{0})} = \text{fraction of 1s}
    \end{align}
where the $\beta_{0}$ can be intuitively obtained by setting the probabilitiy equal to fractions of 1s, or maximising the log likelihood.


The saturated model on the other hand has individual parameters for each observations and makes the perfect predictions. For this model, the likelihood is simply 1 and the LL becomes 0.

##### $\mathbf{R^{2}}$

is also defined in the context of LL as
\begin{align}
        R^{2} = \frac{LL(\text{fitted model}) - LL(\text{null model})}{LL(\text{saturated model}) - LL(\text{null model})}
    \end{align}

the numerator measures how better the model is over null model, and the denominator helps scale the $R^{2}$ between 0 (null model) and 1 (perfect model). Although very similar to $R^{2}$ from linear regression, this is defined slightly differently.

### Multiple Classes

Note that the log of odds formula above is the ratio of probability of $Y=1$ to probability of $Y=0$. Here, $Y=0$ can be seen as a reference class. Similarly, in the case of $K$ classes, we will have $K-1$ classifiers, each classifying with respect to the last class (since the decision boundary has to be between two classes) and will take the form
\begin{align}
        log \bigg( \frac{P(Y=1 \vert X=x)}{P(Y=K \vert X=x)} \bigg) &= \beta_{1,0} + \beta_{1}^{T}x\newline
        log \bigg( \frac{P(Y=2 \vert X=x)}{P(Y=K \vert X=x)} \bigg) &= \beta_{2,0} + \beta_{2}^{T}x\newline
        \vdots\newline
        log \bigg( \frac{P(Y=K-1 \vert X=x)}{P(Y=K \vert X=x)} \bigg) &= \beta_{K-1,0} + \beta_{K-1}^{T}x\newline
        \text{and} \quad \sum_{k=1}^{K} P(Y=k \vert X=x) &= 1\newline
        \text{Giving} \quad P(Y=k \vert X=x) &= \frac{exp(\beta_{k,0} + \beta_{k}^{T}x)}{1 + \sum_{j=1}^{K-1} exp(\beta_{j,0} + \beta_{j}^{T}x)} \quad \text{for $j<K$}\newline
        P(Y=K \vert X=x) &= \frac{1}{1 + \sum_{j=1}^{K-1} exp(\beta_{j,0} + \beta_{j}^{T}x)}\newline
        \text{Parameter Set} \quad \theta &= \{ \beta_{1,0}, \beta_{1}, \ldots, \beta_{K-1,0}, \beta_{K-1} \}
    \end{align}

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

{% include_relative naive_bayes.md %}

## Comparison of Classifiers

Logistic Regression and LDA are similar in the sense that they produce linear decision boundaries.

-   Logistic Regression estimates coefficients using Maximum Likelihood Estimate

-   LDA estimates parameters using the sample mean and variance

For both the models, $\log {odds}$ takes a linear form. LDA adds a strong assumption of normal distribution of the predictor variables.


Comparison of models

-   Logistic Regression is the simplest classifier one can build. It assumes linearly separated decision boundaries. It is usually used as a binary classifier. The decision boundary can be made non linear by adding transformed version of the predictors like second powers, interaction terms etc.

-   LDA is also a linear classifier, but works under the assumptions that the decision boundaries are linear and all the classes share the same covariance matrix. It works well with multiple classes. The performance can be quite bad if the underlying variables are not normally distributed.

-   QDA is a natural extension of LDA that relaxes the assumption of shared covariance matrix and allows each class to have a separate covariance matrix. This causes QDA to work well when decision boundaries have non linearity

-   KNN is a non parametric model that is the most flexible. However, we can get no indication of which predictor is important, and the model can suffer from high variance.

## Classfication Metrics

Several classification metrics are available for binary classifiers which are used based on the problem setting.

### Confusion Matrix

This matrix tabulates the number of cases we are classifying and misclassifying.

| **Confusion Matrix** | **Actual Positive** | **Actual Negative** |
| ================ | =================== | =================== |
| **Predicted Positive** | True Positive | False Positive |
| **Predicted Negative** | False Negative | True Negative |

Based on the above table, we define the following terms

-   Accuracy $= \frac{TP + TN}{P+N}$

-   Sensitivity or True Positive Rate (TPR) or Recall $= \frac{TP}{P} = \frac{TP}{TP+FN}$

-   Specificity or True Negative Rate (TNR) $= \frac{TN}{N} = \frac{TN}{FP+TN}$

-   Precision or Positive Predicted Value (PPV) $= \frac{TP}{FP+TP}$

-   False Positive Rate $= \frac{FP}{N} = \frac{FP}{FP+TN}$

-   $F_{1}$ Score $= \frac{2 * precision * recall}{precision + recall}$

### Receiver Operating Characteristics (ROC Curve)

ROC curve is plot between **True Positive Rate** and **False Positive Rate**, or equivalently, between **sensitivity/recall** and **$1 -$ specificity**. The area under the plotted curve is know as AUC score.

The curve is plot by repeatedly constructing the confusion matrix at different probability thresholds (i.e. changing the decision boundary to see how the confusion matrix changes).

ROC Curve is agnostic of the class balancing in the data set, and is thus used frequently in case of class imbalance to judge a classifier. A random classifier will have AUC of $0.5$ as at any threshold, the number of correctly and incorrectly classified points will roughly be the same. A perfect classifier will be able to segregate the population perfectly and will have the value of AUC as $1.0$.

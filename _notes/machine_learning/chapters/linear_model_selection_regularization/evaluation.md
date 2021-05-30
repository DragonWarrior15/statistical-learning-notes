---
title: "Evaluation Metrics"
---

## Metrics for evaluating Subset Models

In linear models, as we add more variables, the training error usually monotonically decreases. Test error may not behave in the same way. When training a model, the coefficients obtained are specific for minimizing the training error and hence will have less bias in comparison to the test error.

Hence, subset evaluation using training error will usually favour models with more number of variables. To overcome this

-   Correct the training error estimate to correctly calculate test error

-   Use a validation test or $k$-fold validation for better estimate of test error

### $C_{p}$ Estimate

For a least square fitted model,
\begin{align}
        C_{p} = \frac{1}{n}(RSS + 2p\hat{\sigma}^{2})
    \end{align}
$p$ is the number of predictors and $\hat{\sigma}^{2}$ is the estimate of the error associated with each observation. This is typically evaluated using the model built on all $p$ predictors.

Clearly, as $p$ increases, we are penalizing the model more to compensate for the decrease in the training RSS. When $\hat{\sigma}$ is an unbiased estimate of $\sigma$, we can show that this is infact an unbiased estimate of the test MSE.

### Akaike Information Criterion (AIC)

AIC is defined for a large class of models fit by the maximum likelihood estimate.

For least squares fit in linear models, the errors are assumed to be gaussian and thus, AIC and least squares mean the same thing. For this case
\begin{align}
        AIC = \frac{1}{n\hat{\sigma}^2}(RSS + 2p\hat{\sigma}^2)
    \end{align}
where we have omitted an additive constant for the sake of simplicity.

For least squares models, $C_{p}$ and AIC are proportional to each other.

#### Bias Corrected AIC (AICc)
When the sample size is small, there is a high probability is that a model with several parameters will overfit. To counter this, bias correction is introduced in AIC. Assuming the model is univariate, linear in parameters and has normally distributed regressors (conditioned on the regressors),
\begin{align}
    AICc = AIC + \frac{2k^{2} + 2k}{n - k - 1}
\end{align}
where $n$ is the sample size used in modelling and $k$ is the number of parameters. As $n \to \infty$, AICc $\to$ AIC as the extra penalty term converges to zero.

### Bayesian Information Criterion (BIC)

BIC is derived from a Bayesian point of view, but ends up looking similar to the above defined errors.

For least squares error without constants, the BIC is
\begin{align}
        BIC = \frac{1}{n\hat{\sigma}^{2}} (RSS + \log(n)p\hat{\sigma}^{2})
    \end{align}
Note that the $\log(n)$ term will put a heavier weight on the error term for large $p$. Hence, BIC will tend to select models with lower number of variables in comparison to say $C_{p}$.

### Adjusted $R^{2}$

Recall that $R^{2}$ is defined as $1 - RSS/TSS$. Adjusted $R^{2}$ is
\begin{align}
        Adjusted\;R^{2} = 1 - \left(\frac{RSS}{n-p-1}\right)/\left(\frac{TSS}{n-1}\right)
    \end{align}
This adjusted $R^{2}$ might increase or decrease when adding variables due to the terms corresponding to $p$. The intuition is that, after the correct number of variables have been identified, the decrease in RSS is less in comparison to the decrease in $n-p-1$ which will slightly increase the Adjusted $R^{2}$.

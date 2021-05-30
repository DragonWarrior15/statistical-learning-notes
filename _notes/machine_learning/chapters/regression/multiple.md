---
title: "Multiple Linear Regression"
---

## Multiple Linear Regression

By minimizing the sum squared error in a fashion similar to simple linear regression case, we can obtain the regression coefficients as follows ($X$ is $n \times p+1$ size with the first column containing all $1s)$
\begin{align}
    \hat{Y} &= X\hat{\beta}\newline
    MSE &= (Y-\hat{Y})^{T}(Y-\hat{Y})\newline
    \frac{\partial}{\partial \hat{\beta}} MSE &= 0 \newline
    \text{or,} \quad 0 &= \frac{\partial}{\partial \hat{\beta}} (Y^{T}Y - Y^{T}X\hat{\beta} - \hat{\beta}^{T}X^{T}Y + \hat{\beta}^{T}X^{T}X\hat{\beta})\newline
    0 &= -Y^{T}X - Y^{T}X + \hat{\beta}^{T}X^{T}X + \hat{\beta}^{T}X^{T}X\newline
    (X^{T}X)\hat{\beta} &= X^{T}Y\newline
    \hat{\beta} &= (X^{T}X)^{-1}X^{T}Y
\end{align}

We note that the coefficients are linear combinations of $Y$ and thus normally distributed themselves.
\begin{align}
{1}
    E[\hat{\beta}] &= E[(X^{T}X)^{-1}X^{T}Y] = E[(X^{T}X)^{-1}X^{T}(X\beta + \epsilon)]\newline
    &= E[\beta] + (X^{T}X)^{-1}X^{T}E[\epsilon]\newline
    &= \beta\newline
    \text{Since} \quad Cov(\mathbf{x}) &= E[(\mathbf{x} - E[\mathbf{x}])(\mathbf{x} - E[\mathbf{x}])^{T}]\text{,}\newline
    \text{and} \quad Cov(\epsilon) &= E[(\epsilon - 0)(\epsilon - 0)^{T}] = E[\epsilon \epsilon^{T}] = \sigma^{2}\newline
    Cov(\hat{\beta}) &= Cov((X^{T}X)^{-1}X^{T}Y)\newline &= E[((X^{T}X)^{-1}X^{T}(X\beta + \epsilon) - \beta)((X^{T}X)^{-1}X^{T}(X\beta + \epsilon) - \beta)^{T}]\newline
    &= (X^{T}X)^{-1}X^{T}X(X^{T}X)^{-T}E[\epsilon \epsilon^{T}]\newline
    &= (X^{T}X)^{-1}X^{T}\sigma^{2}\newline
    \hat{\beta} &\sim \mathcal{N}(\beta, (X^{T}X)^{-1}\sigma^{2})\end{align}
$\hat{\beta}$ is a linear combination of independent $Y_{i}s$ and is normally distributed. Also, note that $X^{T}X$ is symmetric and so will be it's inverse.


An unbiased estimator of $\sigma^{2}$ is
\begin{align}
    \hat{\sigma}^{2} = \frac{1}{n-p-1} \sum_{i=1}^{n} (y_{i} - \hat{y}\_{i})^{2} \text{,}\quad E[\hat{\sigma}^{2}] = \sigma^{2}\end{align}
where the denominator is chosen to make the estimator unbiased. it can be shown that
\begin{align}
    (n - p - 1) \frac{\hat{\sigma}^{2}}{\sigma^{2}} \sim \chi_{n-p-1}^{2}\end{align}

with $\hat{\beta}$ and $\hat{\sigma}^{2}$ independent random variables.

### Confidence Intervals

The mean response for any new input is also a random variable with the distributions
\begin{align}
    E[x^{T}\hat{\beta}] &= x^{T}\beta\newline
    Var(x^{T}\hat{\beta}) &= E[(\hat{\beta} - \beta)(\hat{\beta} - \beta)^{T}]\newline
    &= x^{T}(E[\hat{\beta}\hat{\beta}^{T}] - \beta\beta^{T})x = x^{T}E[(\hat{\beta} - \beta)(\hat{\beta} - \beta)^{T}]x\newline
    &= x^{T}(X^{T}X)^{-1}x \sigma^{2}\newline
    x^{T}\hat{\beta} &\sim \mathcal{N}(x^{T}\beta, x^{T}(X^{T}X)^{-1}x \sigma^{2})\end{align}

Utilizing the unbiased estimate of $\sigma^{2}$ defined above, we can get the confidence and prediction intervals as follows (using t-distribution after dividing the normal distribution of response with the estimator of $\sigma^{2}$) for $1-\alpha$ confidence
\begin{alignat}{2}
    \text{confidence interval for mean response} \quad &x^{T}\beta \quad &\in \quad &x^{T}\hat{\beta} \pm t_{\alpha/2, n-p} \sqrt{x^{T}(X^{T}X)^{-1}x \sigma^{2}}\newline
    \text{prediction interval for response} \quad &Y \quad &\in \quad &x^{T}\hat{\beta} \pm t_{\alpha/2, n-p} \sqrt{1 + x^{T}(X^{T}X)^{-1}x \sigma^{2}}
\end{alignat}

### Hypopthesis Testing

#### Single Coefficient

To test
\begin{align}
    H_{0}: \beta_{j} = 0 \quad \text{versus} \quad H_{1}: \beta_{j} \neq 0\end{align}
we utilize some of the above defined distributions
\begin{gather}
    \hat{\beta}\_{j} \sim \mathcal{N}(\beta_{j}, \sigma^{2}diag((X^{T}X)^{-1})\_{j})\newline
    (n - p - 1) \frac{\hat{\sigma}^{2}}{\sigma^{2}} \sim \chi_{n-p-1}^{2}\newline
    \frac{\hat{\beta}\_{j} - \beta_{j}}{\sigma\sqrt{diag((X^{T}X)^{-1})\_{j}}} \div \sqrt{(n - p - 1) \frac{\hat{\sigma}^{2}}{\sigma^{2}(n-p-1)}} \sim t_{n-p-1}\newline
    \text{and under null hypothesis,} \quad \frac{\hat{\beta}\_{j}}{\hat{\sigma}\sqrt{diag((X^{T}X)^{-1})\_{j}}} \sim t_{n-p-1}\newline
    \text{where} \quad \frac{\hat{\beta}\_{j}}{\hat{\sigma}\sqrt{diag((X^{T}X)^{-1})\_{j}}} \quad \text{is often called Z-score}
\end{gather}

where variance utilizes the diagonal entry of variance of $\beta$. If we know the actual variance $\sigma^{2}$, we replace it in the above equation to get a normal distribution instead. A large value of the *Z-score* will lead to the elimination of the null hypothesis meaning the coefficient is not zero. The $1-\alpha$ confidence intervals for $\beta_{j}$ then become
\begin{align}
    \beta_{j} \in \hat{\beta} \pm \hat{\sigma} t_{\alpha/2, n-p-1} \sqrt{diag((X^{T}X)^{-1})\_{j}}\end{align}

#### Group of Coefficients, F-test

Suppose we have a set of $k$ coefficients for a categorical variable and we wish to test
\begin{align}
     H_{0}: \beta_{i} = \beta_{i+1} = \cdots = \beta_{k} = 0 \quad \text{versus} \quad H_{1}: \text{at least one of} \quad \beta_{j} \neq 0, j \in (i, \ldots, k)\end{align}
Then, we use the **F-test** assuming $H_{0}$ is true
\begin{gather}
    F = \frac{(RSS_{0} - RSS_{1})/k}{RSS_{1}/(n-p-1)}\newline
    \text{where} \quad RSS_{0} = RSS \quad \text{of model without the $k$ coefficients}\newline
    \text{and} \quad RSS_{1} = RSS \quad \text{of model with all the coefficients}\newline
    F \sim F_{k, n - p - 1}
\end{gather}

### Multiple Outputs

We want to predict multiple outputs $Y_{1}, Y_{2}, \ldots, Y_{k}$ from the same set of variables. The $RSS$ then becomes
\begin{align}
    RSS = \sum_{i=1}^{n} \sum_{j=1}^{k} (y_{i,j} - \hat{y}\_{i,j})^{2} = \sum_{i=1}^{n} \sum_{j=1}^{k} (y_{i,j} - \beta_{k,0} - \sum_{u=1}^{p} \beta_{k,u}x_{i,u})^{2}\newline
    \text{Minimizing,} \quad \hat{\beta} = (X_{T}X)^{-1}X^{T}Y \quad \text{where $Y$ is a $n \times k$ matrix}\end{align}
Thus, the problem is similar to doing the linear regression independently on each of the $Y_{j}s$. One important assumption here is that the errors between different $Y_{j}$ are not correlated with each other.

### Coefficient Interpretation

The interpretation of coefficients for quantitative variables is straightforward. Further, suppose the equation has the form
\begin{align}
    y = \beta_{0} + \beta_{1}X_{1} + \beta_{2}X_{2} + \ldots + \beta_{p}X_{p} + \epsilon\end{align}

Then, $\beta_{1}$ denotes the change in $y$ that will be caused by changing the value of $X_{1}$ by 1 unit, provided all other inputs are constant. If we change two variables simultaneously, we can see their interaction together keeping the remaining variables constant.


However, this procedure is not straightforward for qualitative/categorical variables. Suppose we have one numeric variable, say age, and a variable denoting gender which we will constraint to have two values, $0$ denoting male and $1$ denoting female. The regression equation becomes
\begin{align}
    y =\beta_{age}x_{age} + \beta_{gender}x_{gender} + \epsilon = \begin{cases}
        \beta_{age}x_{age} + \beta_{gender} + \epsilon \quad &\text{if male}\newline
        \beta_{age}x_{age} + \epsilon \quad &\text{otherwise}
    \end{cases}\end{align}

Thus, $\beta_{gender} (<0)$ signifies how much $y$ is less for males compared to females. The coefficient in itself has no meaning unless compared with respect to a base value.


Suppose we were to change the convention to $-1$ for females and $1$ for males, then
\begin{align}
    y =\beta_{age}x_{age} + \beta_{gender}x_{gender} + \epsilon = \begin{cases}
        \beta_{age}x_{age} + \beta_{gender} + \epsilon \quad &\text{if male}\newline
        \beta_{age}x_{age} -\beta_{gender} + \epsilon \quad &\text{otherwise}
    \end{cases}\end{align}

Now, $2\beta_{gender}$ gives us the difference between the value of $y$ between males and females, and $\beta_{gender}$ denotes the change on either side from the base value of $\beta_{age}x_{age} + \epsilon$. This new $\beta$ should be have of the original coefficient because the real relation has stayed the same. Thus, the interpretation of coefficients changes based on how the variable gets defined.


In case of $n$ levels, we will create $n-1$ variables (since the last variable is perfectly correlated with all the remaining ones). Then, the coefficient of the $i^{th}$ level is simply the increment over the base (last) level. Note that there is no coefficient for the last level, and all the other coefficients are relative to this level.


##### Hierarchical Principle

If we include an interaction in the model, we should include all the main effects, even if their *p-values* of those coefficients are insignificant. Simply put, if $X_{1}X_{2}$ appears in the model, $X_{1}$ and $X_{2}$ should also be there. Similarly, for a categorical variable, either all the categories are present in the model, or none of them are present. It is alright to just use a single category, but then the remaining categories together constitute the base cateogory and in essence, all categories are still present in the model, albiet in a different form.


##### Importance of interactions

Suppose we build a bank balance model dependent on income, and if a person is a student or not. Basic model
\begin{align}
    y = \beta_{income}+x_{income} + \beta_{student}x_{student} + \epsilon\end{align}
The problem with this model is that for both student and non student, the effect of income is same, which is not what we want. Including interaction terms,
\begin{align}
    y = \beta_{income}+x_{income} + \beta_{student}x_{student} + \beta_{income \times student}x_{income}x_{student} + \epsilon\end{align}
which gives different dependence on income (slope) for student ($\beta_{income} + \beta_{income \times student}$) and non student $(\beta_{income})$.

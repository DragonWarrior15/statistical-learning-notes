# Answer

The likelihood of the $n$ random variables will be

$$
\begin{aligned}
        L &= \prod_{i=1}^{n} f_{X}(x_{i})\newline
        &= \bigg( \frac{2}{\lambda} \bigg)^{n} \prod_{i=1}^{n} X_{i} \exp \bigg( -\frac{1}{\lambda} \sum_{i=1}^{n} X_{i}^{2} \bigg)\newline
        \ln L &= -n \ln \bigg( \frac{\lambda}{2} \bigg) = \ln \bigg( \prod_{i=1}^{n} X_{i} \bigg) - \frac{1}{\lambda} \sum_{i=1}^{n} X_{i}^{2}\newline
        \frac{\partial \ln L}{\partial \lambda} &= -\frac{n}{\lambda} + \frac{1}{\lambda^{2}}\sum_{i=1}^{n} X_{i}^{2} = 0\newline
        \lambda_{MLE} &= \frac{1}{n} \sum_{i=1}^{n} X_{i}^{2}
    \end{aligned}
$$


To prove that it is an unbiased estimator, we need to show $E[\lambda_{MLE}] = \lambda$

$$
\begin{aligned}
        E[X^{2}] &= \int_{0}^{\infty} \frac{2x^{3}}{\lambda} \exp \bigg(-\frac{x^{2}}{\lambda} \bigg) dx\newline
        &= \int_{0}^{\infty} \lambda t e^{t} dt \: \text{putting $x^{2}/\lambda = t$}\newline
        &= \lambda\newline
        E[\lambda_{MLE}] &= \frac{1}{n} \sum_{i=1}^{n} E[X_{i}^{2}] = \lambda
    \end{aligned}
$$


To show that this is a sufficient statistic, we try to factorize the joint density function

$$
\begin{aligned}
        T(X) &= \frac{1}{n} \sum_{i=1}^{n} X_{i}^{2}\newline
        L &= \prod_{i=1}^{n} f_{X}(x_{i})\newline
        &= \bigg( \frac{2}{\lambda} \bigg)^{n} \prod_{i=1}^{n} X_{i} \exp \bigg( -\frac{1}{\lambda} \sum_{i=1}^{n} X_{i}^{2} \bigg)\newline
        &= \bigg( \prod_{i=1}^{n} X_{i} \bigg) \bigg( \bigg( \frac{2}{\lambda} \bigg)^{n} \exp \bigg( -\frac{n}{\lambda} T(X) \bigg) \bigg)\newline
        &= h(X) g(T(X), \lambda)
    \end{aligned}
$$

i.e., we were able to factorize the joint density into two functions, one which is only dependent on the sample, and the other dependent on the parameter $\lambda$ and on the sample through the statistic $\lambda_{MLE}$. By Fisher Neyman Factorization Theorem, $\lambda_{MLE}$ is a sufficient statistic.

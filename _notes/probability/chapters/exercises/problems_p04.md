---
title: "Exercises Part 4"
---

## Exercises Part 4

1.  **Estimating Binomial with CLT, 1/2 correction**

    Given a Bernoulli Process with $n = 36$ and $p = 0.5$, find $P(S_{n} \leq 21)$. [Solution]({{ "/notes/probability/chapters/exercises/a_binclt.html" | relative_url }})

1.  **Sample Variance for Normal Distribution**

    The time it takes a central processing unit to process a certain type of job is normally distributed with mean 20 seconds and standard deviation 3 seconds. If a sample of 15 such jobs is observed, what is the probability that the sample variance will exceed 12 ? [Solution]({{ "/notes/probability/chapters/exercises/a_samplevar.html" | relative_url }})

1.  **MLE Estimate**

    Suppose we observe $n$ independent and identically distributed samples $x_{1}, x_{2}, \ldots, x_{n}$ from an exponential distribution. Estimate the parameter of the exponential. [Solution]({{ "/notes/probability/chapters/exercises/a_mleestimate.html" | relative_url }})

1.  **CRLB for an exponential**

    Let $X_{1}, \ldots, X_{n}$ be a random sample from an eponential distribution with the probability density
    \begin{align}
            f_{X}(x;\theta) = \begin{cases} \frac{1}{\theta} \exp \big(-\frac{x}{\theta} \big) &\mbox{$x > 0$}\newline 0 &\mbox{otherwise} \end{cases}
        \end{align}
    where $\theta > 0$. Derive the Cramer-Rao lower bound for the variance of any unbiased estimator of $\theta$. Also prove that $T = \frac{1}{n} \sum_{i=1}^{n} X_{i}$ is the minimum variance unbiased estimator of $\theta$. [Solution]({{ "/notes/probability/chapters/exercises/a_crlb_exp.html" | relative_url }})

1.  **MLE and Proving Sufficient Statistic**

    Suppose $X_{1}, X_{2}, \ldots, X_{n}$ are from a distribution with the following distribution
    \begin{align}
            f_{X}(x) = \begin{cases} \frac{2x}{\lambda} \exp \big(-\frac{x^{2}}{\lambda} \big) &\mbox{if $x > 0$}\newline 0 &\mbox{otherwise} \end{cases}
        \end{align}
    Find the MLE estimate of $\lambda$ and show that it is unbiased and a sufficient statistic of $\lambda$.
    [Solution]({{ "/notes/probability/chapters/exercises/a_mle_sufficient_statistic.html" | relative_url }})

1.  **Bayes Estimator for Normal Distribution**

    Suppose $X_{1}, X_{2}, \ldots, X_{n}$ are from a normal distribution with unknown mean $\theta$ and known variance $\sigma_{0}^{2}$, and suppose the mean has a prior normal ditribution with mean $\mu$ and variance $\sigma^{2}$. Calculate the Bayes estimator for the mean $\theta$.
    [Solution]({{ "/notes/probability/chapters/exercises/a_bayesnormal.html" | relative_url }})

1.  **LMS Estimate**

    Given the prior $f_{\Theta \vert (\theta)}$, uniform in $[4,10]$, and $f_{X \vert \Theta}(x \vert \theta)$ is uniform in $\[\theta-1, \theta+1 \]$, estimate the posterior of $\theta$. [Solution]({{ "/notes/probability/chapters/exercises/a_lmsestimate.html" | relative_url }})

1.  **Probability Convergence**

    Let $X$ be uniformly distributed between $[-1,1]$. Let $X_{1}, X_{2},\ldots,X_{n}$ be independently and identically distributed with the same distribution as $X$. Find whether the following sequences are convergent in probability and also find the limit.

    1.  $X_{i}$

    2.  $Y_{i} = X_{i}/i$

    3.  $Z_{i} = (X_{i})^{i}$

    [Solution]({{ "/notes/probability/chapters/exercises/a_convergence.html" | relative_url }})

1.  **Age of Smokers vs Non Smokers**

    One often hears that the death rate of a person who smokes is, at each age, twice that of a nonsmoker. What does this mean? Does it mean that a nonsmoker has twice the probability of surviving a given number of years as does a smoker of the same age? [Solution]({{ "/notes/probability/chapters/exercises/a_lifesmoker.html" | relative_url }})

1.  **Simple Hypothesis Test**

    Let $X_{1}, \ldots, X_{10}$ be a random sample of heights from a $\mathcal{N}(\mu, 20^{2})$ distribution where we want to test the hypothesis $H_{0}: \mu = 30$ vs $H_{a}: \mu \neq 30$. For a significance level of $0.05$ and mean of the $10$ samples as $27$, determine if $H_{0}$ is accepted or not. [Solution]({{ "/notes/probability/chapters/exercises/a_hypothesis_test.html" | relative_url }})

1.  **Most Powerful Test for Variance**

    Let $X_{1}, \ldots, X_{5}$ be a random sample from a $\mathcal{N}(2, \sigma^{2})$ distribution where $\sigma^{2}$ is unknown. Derive the most powerful test of size $\alpha = 0.05$ for testing $H_{0}: \sigma^{2} = 4$ against $H_{1}: \sigma^{2} = 1$. [Solution]({{ "/notes/probability/chapters/exercises/a_most_powerful_test.html" | relative_url }})

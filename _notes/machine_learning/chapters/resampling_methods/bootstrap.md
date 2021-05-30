---
title: "Bootstrap"
---

## Bootstrap

A widely applicable method that helps quantify uncertainty in the estimates of a statistical model. This is especially useful when formulae don't exist to quantify this uncertainty.

To estimate the uncertainty in estimates, we repeatedly create new data sets called bootstrap samples. Here, we simply select $n$ observations from the original data set, but with replacement. This creates a slightly different version of the original data on which we train our model and get the estimates. From several bootsrapped data sets, we obtain a distribution of our estimate (a collection of estimates) whose mean and variance can help quantify the uncertainty.


### Probability of selection

Since we are sampling with replacement, notice that the chance that the $i^{th}$ observation is in the sampled data set is given by
\begin{align}
        P(not\;selection) &= (1-\frac{1}{n})^{n}\newline
        P(selection) &= 1 - (1 - \frac{1}{n})^{n}
    \end{align}
This comes using the product rule. The chance that any observation of the bootstrap sample is not equal to $i^{th}$ observation is simply $1 - \frac{1}{n}$ since we can choose any of the other $n-1$ examples.
\begin{align}
        \text{Note, } y &= \lim_{n\to\infty}(1-\frac{1}{n})^{n}\newline
                 \ln(y) &= \lim_{n\to\infty}\frac{1}{n}\ln(1-\frac{1}{n}) \newline
                        &= \lim_{n\to\infty}\frac{\ln(1-\frac{1}{n})}{\frac{1}{n}} \newline
                        &= \lim_{n\to\infty}\frac{\frac{1}{1-\frac{1}{n}} \frac{1}{n^{2}}}{-\frac{1}{n^{2}}} \quad\text{Using L'Hospital's Rule}\newline
                        &= \lim_{n\to\infty}-\frac{1}{1 - \frac{1}{n}}\newline
                        &= -1\newline
                      y &= \frac{1}{e}\newline
        \lim_{n\to\infty} P(selection) &= 1 - \frac{1}{e} \approx 0.632
    \end{align}
Hence, the probability that an observation from the original data set falls into a bootstrap sample is $63.2\%$ which suggests that the sampled data sets are sufficiently variable !

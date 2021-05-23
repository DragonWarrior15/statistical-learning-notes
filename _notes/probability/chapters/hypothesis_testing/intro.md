---
title: "Hypothesis Testing"
---

# Hypothesis Testing

Hypothesis testing is a set of procedures used to test a hypothesis about statistical parameters. Based on the results of the procedure, we decide whether to accept or reject the hypothesis. This can be as simple as deciding whether the mean of a population is more than 1 or not.


Whenever a hypothesis is accepted, it does not mean that the hypothesis is true, but rather that the data is consistent with it.


Suppose we have a population that is characterized by the distribution $F_{\theta}$ and we are interested in making statistical comments about the value of the parameters $\theta$. **The hypothesis that specifies the statement that we are going to test about the parameter is called the null hypothesis** and is denoted by $H_{0}$. Note that the statement of the null hypothesis can either comment on the exact value of the parameter, or comment on an inequality satisfied by the parameter. When the hypothesis completely specifies the distribution, it is called a *simple hypothesis* and in the other case, it is called *composite hypothesis*.


To test the hypothesis, suppose we have available with us $n$ independent samples from the population. Based on these samples, we must define a $n$ dimensional region $C$ such that if the sample falls in this region, we reject the null hypothesis and vice versa. This region $C$ is called the critical region (or the rejection region).
\begin{align}
        \text{Reject}\quad H_{0} \quad\text{if}\quad (X_{1}, X_{2}, \ldots, X_{n}) \in C\newline
        \text{Acecpt}\quad H_{0} \quad\text{if}\quad (X_{1}, X_{2}, \ldots, X_{n}) \notin C
    \end{align}

Two types of errors can result when checking a hypothesis

-   *type* $I$ *error*: Reject $H_{0}$ when it is correct

-   *type* $II$ *error*: Accept $H_{0}$ when it is incorrect

Since hypothesis testing is about checking if the given data is consistent with the hypothesis, the error we make on rejecting the hypothesis when it is correct should be low. This is consistent with the confidence intervals discussed earlier. We denote *type I error* by $\alpha$ meaning that there is only $\alpha$ chance that the hypothesis will be incorrectly rejected by the test, and is called the level of significance of the test.


**A lower significance level or lower $\alpha$ implies that we require stronger evidence against the null hypothesis to reject it.**

A classical approach while testing the parameters of a population will be to first determine a point estimator of the parameter and then determine the distribution of the said estimator. Hypothesis test will usually involve checking whether the estimator lies in a selcted region, for which we can determine the relevant confidence intervals through the distribution of the estimator.


The maximum probability of type $I$ error is also called the **size of the test**. For a simple hypothesis test
\begin{align}
        \alpha &= P(\text{Reject}\; H_{0}\; \text{when it is correct})\newline
        &= P((X_{1}, X_{2}, \ldots, X_{n}) \in C \vert H_{0})\newline
        &= \text{size of the test}
    \end{align}
For a composite hypothesis test
\begin{align}
        \alpha = sup_{h \in H_{0}} P(\text{Reject}\; H_{0} \vert h)
    \end{align}
or, the size of the test is the worst case scenario probability of a type $I$ error (we intend to minimize the type $I$ error).

Finally, the power of a test and any related measure will be defined based on the set of observables $(X_{1}, X_{2}, \ldots, X_{n})$ since the hypothesis tests depend on determining the critical region $C$ for these set of observables.


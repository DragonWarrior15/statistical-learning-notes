---
title: "Exercises Part 2"
---

## Exercises Part 2

1.  **Binomial Shooter**

    A shooter takes 10 hits in a shooting range and each shot has $p=0.2$ of hitting target independent of each other. Let $X =$ number of hits. Find

    1.  PMF of $X$

    2.  $P(\text{no hits})$

    3.  $P(\text{scoring more than misses})$

    4.  $E[X]$ and $Var(X)$

    5.  Suppose the entry is \\$3 and each shot fetches \\$2. Let $Y$ = profit. Find $E[Y]$ and $Var(Y)$.

    6.  Suppose entry is free and total reward is square of number of hits. Let $Z$ be profit. Find $E[Z]$.

    [Solution]({{ "/notes/probability/chapters/exercises/a_binshoot.html" | relative_url }})

1.  **Mosquito and Tick**

    Every second, a mosquito lands with $P = 0.5$. Once it lands, it bites with $P=0.2$. Let $X$ be the time between successive mosquito bites. Find $E[X]$ and $Var(X)$.

    Now suppose a tick comes into play independent of mosquito. It lands with $P=0.1$ and once landed, bites with $P=0.7$. Let $Y$ be the time between successive bug bites. Find $E[Y]$ and $Var(Y)$. [Solution]({{ "/notes/probability/chapters/exercises/a_mosquito.html" | relative_url }})

1.  **HH or TT**

    Given a coin with $P(H) = p$, find the $E$\[number of tosses till $HH$ or $TT$\]. [Solution]({{ "/notes/probability/chapters/exercises/a_hhtt.html" | relative_url }})

1.  **A Three Coin Game**

    Let $3$ fair coins be tossed at every turn. Given all coins and turns are independent, calculate the following (assuming success is defined as all three coins landing the same side up))

    1.  PMF of $K$, no of trials upto but not including the $2^{nd}$ success

    2.  $E$ and $Var$ of $M$, the $E[$number of tails$]$ before first success.

    [Solution]({{ "/notes/probability/chapters/exercises/a_threecoins.html" | relative_url }})

1.  **Linear Expectations**

    Bob conducts trials in a similar manner to previous problem (**A Three Coin Game**) , but with four coins. He repeatedly removes a coin at success until just a single coin remains. Calculate the Expected number of tosses till the finish of experiment. [Solution]({{ "/notes/probability/chapters/exercises/a_linexp.html" | relative_url }})

1.  **Papers Drawn with Replacement**

    Suppose there are $n$ papers in a drawer. We take one paper, sign it, and then put it back into the drawer. We take one more paper out and if it is not signed, we sign it and put it back in the drawer. If the paper is already signed, we simply put it back in the drawer. We repeat this process until all the papers are signed. Find the $E[$papers drawn till all papers are signed$]$. What is the value of this quantity as $n \to large$. [Solution]({{ "/notes/probability/chapters/exercises/a_papers.html" | relative_url }})

1.  **A Three Variable Inequality**

    Let $X$, $Y$, $Z$ be three exponentially distributed random variables with parameters $\lambda, \mu,$ and $\nu$ respectively. Find $P(X < Y < Z)$. [Solution]({{ "/notes/probability/chapters/exercises/a_threevar.html" | relative_url }})

1.  **Poisson Emails**
    You get emails according to a Poisson process at the rate of 5 messages/hour. You check email every 30 minutes. Find

    -   P(no new message)

    -   P(one new message)

    [Solution]({{ "/notes/probability/chapters/exercises/a_poissonemails.html" | relative_url }})

1.  **Poisson Fishing**

    We go fishing where we catch fishes at the rate of $0.6/hour$. We fish for two hours. If we do not catch a fish in the first two hours, we fish until the first catch. Find the following

    -   P(fish for $> 2$ hours)

    -   P(fish for $> 2$ but $< 5$ hours)

    -   P(catch at least two fish)

    -   E\[fish\]

    -   E\[Total fishing time\]

    -   $E\[\text{future fishing time} \vert \text{fished for two hours}\]$

    [Solution]({{ "/notes/probability/chapters/exercises/a_poissonfish.html" | relative_url }})

1.  **Poisson Lightbulbs**

    We have three identical but independent lightbulbs whose lifetimes are modelled by a Poisson process with parameter $\lambda$. Given that we start all the three bulbs together, find the $E[\text{time until last bulb dies out}]$. [Solution]({{ "/notes/probability/chapters/exercises/a_poissonbulb.html" | relative_url }})

1.  **Two Poisson Lightbulbs**

    Beginning at $t=0$, we begin using bulbs one at a time until failure. Any broken bulb is immediately replaced. Each new bulb is selected independently and equally likely from type A(exponential life with $\lambda = 1$) or type B(exponential life with $\lambda = 3$). Lifetimes of all bulbs are independent.

    1.  Find $E[$time until first failure$]$.

    2.  $P($no bulb failure before time $t)$.

    3.  Given that there are no failures until time t, determine the conditional probability that the first bulb used is of type A.

    4.  Find the probability that the total illumination by two type B bulbs $>$ one type A.

    5.  Suppose the process terminates after 12 bulbs fail. Determine the expected value and variance of the total illumination provided by type B bulbs while the process is in operation.

    6.  Given there are no failures until time $t$, find the expected value of time until first failure.

    [Solution]({{ "/notes/probability/chapters/exercises/a_poissonbulb2.html" | relative_url }})

1.  **Minimum of Exponentials**

    Given $n$ independent exponential random variables with different parameters, find the distribution for their minimum. [Solution]({{ "/notes/probability/chapters/exercises/a_minexp.html" | relative_url }})

1.  **A Similar Trick**

    Calculate
    \begin{align}
             \lim_{n \to \infty} \bigg[ \frac{1}{2^{n/2}\Gamma(n/2)} \int_{n + \sqrt{2n}}^{\infty} \exp \bigg( -\frac{t}{2} \bigg) t^{n/2 - 1} dt \bigg]
        \end{align}

    [Solution]({{ "/notes/probability/chapters/exercises/a_gamma_chi.html" | relative_url }})

1.  **Exponential Times**

    In a warehouse of parts, average time between requests for parts is about 10 minutes. Assume this time is exponentially distributed. Find
    1. Probability that in an hour there are at least 10 requests for parts.
    1. Porbability that 10th request in the morning requires at least two hours of waiting time.

    [Solution]({{ "/notes/probability/chapters/exercises/a_exponential_times.html" | relative_url }})

1.  **The Power of Moments**

    Let $X_{1}$ and $X_{2}$ be independent random variables that are distributed as $Gamma(3, 1/3)$ and $Gamma(5, 1)$ respectively. Let $Y = 2X_{1} + 6X_{2}$. Find the mgf and distribution of $Y$. [Solution]({{ "/notes/probability/chapters/exercises/a_power_moment.html" | relative_url }})

1.  **Careful with cdf**

    Let $X$ be normally distributed with mean 1 and variance 4. Find $P(1 < X^{2} < 9)$. [Solution]({{ "/notes/probability/chapters/exercises/a_cumul_cdf.html" | relative_url }})

1.  **Gamma to Beta**
    Suppose we have the following definitions
    \begin{align}
        X_{1} &\sim Gamma(\alpha_{1}, \lambda_{1})\newline
        X_{2} &\sim Gamma(\alpha_{2}, \lambda_{2})\newline
        Y_{1} &= \lambda_{1}X_{1} + \lambda_{2}X_{2}\newline
        Y_{2} &= \frac{\lambda_{1}X_{1}}{\lambda_{1}X_{1} + \lambda_{2}X_{2}}
    \end{align}
    where $X_{1}$ and $X_{2}$ are independent.

    Show that $Y_{1}$ and $Y_{2}$ are independent and find the distribution of $Y_{2}$. [Solution]({{ "/notes/probability/chapters/exercises/a_gamma_to_beta.html" | relative_url }})

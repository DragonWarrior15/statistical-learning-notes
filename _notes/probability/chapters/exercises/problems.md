---
title: "Exercises"
---

## Exercises

1.  **Independence in Complements**

    Given $A \perp B$, show $A \perp B^{c}$ and $A^{c} \perp B^{c}$. [Solution]({{ "/notes/probability/chapters/exercises/a_indcomp.html" | relative_url }})

1.  **Conditional Independence**

    $A,B,$ and $C$ are independent with $P(C) > 0$. Show that $A\perp B \vert C$. [Solution]({{ "/notes/probability/chapters/exercises/a_conind.html" | relative_url }})

1.  **Geometry of Meeting**

    R and J have to meet at a given place and each will arrive at the given place independent of each other with a delay of 0 to 1hr uniformly distributed. The pairs of delays are all equally likely. The first to arrive waits for 15 minutes and leaves. What is the probability of meeting ? [Solution]({{ "/notes/probability/chapters/exercises/a_geomeet.html" | relative_url }})

1.  **Expectation of Function**

    Let $X$ and $Y$ be random variables with $Y = g(X)$. Show $E[Y] = \sum_{x}g(x)p_{X}(x)$. [Solution]({{ "/notes/probability/chapters/exercises/a_expfn.html" | relative_url }})

1.  **Cumulative Distribution Function**

    A random variable X is a combination of a continuous and discrete distribution as follows
    \begin{align}
            f_{X}(x) = \begin{cases} 0.5 &\mbox{$a \leq x \leq b$}\newline
                                     0.5 &\mbox{x = 0.5}\newline
                                     0 &\mbox{otherwise} \end{cases}
        \end{align}
    Find the Cumulative Distribution of X. [Solution]({{ "/notes/probability/chapters/exercises/a_cumuldistfn.html" | relative_url }})

1.  **Number of tosses till first head**

    When tossing a fair coin, what is the $E[$\# tosses till the first H$]$. [Solution]({{ "/notes/probability/chapters/exercises/a_tossh.html" | relative_url }})

1.  **Iterated Expectation Proof**

    For discrete variables, show $E[X] = E[E[X \vert Y]]$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexpproof.html" | relative_url }})

1.  **Iterated Expectation for three variables**

    For three random variables $X$, $Y$ and $Z$, show $E[Z \vert X] = E[E[Z \vert X,Y] \vert X]$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexpthree.html" | relative_url }})

1.  **Iterated Expectation practice**

    A class has two sections denoted by the random variable $Y$. Let $X$ denote the quiz score of a student. Given that section 1 has 10 students, section 2 has 20 students, $E[X \vert Y=1] = 90, E[X \vert Y=2] = 60, Var(X \vert Y=1) = 10, Var(X \vert Y=2) = 20$, find $E[X]$ and $Var(X)$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexppractice.html" | relative_url }})

1.  **Hat Problem**

    $n$ people throw their hats in a box and then pick a hat at random. What is the expected number of people who pick their own hat ? [Solution]({{ "/notes/probability/chapters/exercises/a_hatproblem.html" | relative_url }})

1.  **Breaking a stick**

    A stick of length $l$ is broken first at $X$ uniformly chosen between $[0,l]$, and then at $Y$, uniformly chosen between $[0,X]$. Find the expected length of the shorter part. [Solution]({{ "/notes/probability/chapters/exercises/a_breakstick.html" | relative_url }})

1.  **Convolution of Exponentials**

    Suppose $X \sim exp(\lambda)$ and $Y \sim exp(\mu)$, find the probability distribution $p_{X+Y}(x)$. [Solution]({{ "/notes/probability/chapters/exercises/a_convexp.html" | relative_url }})

1.  **Triangles from a Stick**

    We have a stick of length 1. We randomly choose two points on the stick and break the stick at those points. Calculate the probability that the three pieces form a triangle. [Solution]({{ "/notes/probability/chapters/exercises/a_trianglestick.html" | relative_url }})

1.  **PMF of g(X)**

    Let $X$ be uniform in $[0, 2]$, then find the PMF of $Y = X^{3}$. [Solution]({{ "/notes/probability/chapters/exercises/a_pmffn.html" | relative_url }})

1.  **Waiting for Taxi**

    A taxi stand and bus stop near Al's home are at the same location. Al goes there and if a taxi is waiting $P=\frac{2}{3}$, he boards it. Otherwise, he waits for a taxi or bus to come, whichever is first. Taxi takes anywhere between $0$ to $10$ mins (uniform) while a bus arrives in exactly 5 mins. He boards whichever is first. Find CDF and $E$\[wait time\]. [Solution]({{ "/notes/probability/chapters/exercises/a_waittaxi.html" | relative_url }})

1.  **Bayes Theorem**

    Let $Q$ be a continuous random variable with PDF
    \begin{align}
            f_{Q}(q) = \begin{cases} 6q(1-q) &\mbox{ $0 \leq q \leq 1$}\newline
                                     0 &\mbox{ otherwise} \end{cases}
        \end{align}
    where $Q$ represents $P(success)$ for a Bernoulli $X$, i.e., $P(X=1|Q=q) = q$. Find $f_{Q|X}(q|x) \forall x \in [0,1]$ and $q$. [Solution]({{ "/notes/probability/chapters/exercises/a_bayes.html" | relative_url }})

1.  **A Normal Transformation**

    Let $X \sim \mathcal{N}(0,1)$ and $Y = g(X)$. Find $p_{Y}(y)$.
    \begin{align}
            g(t) = \begin{cases} -t &\mbox{$t \leq 0$}\newline
                                \sqrt{t} &\mbox{$t > 0$} \end{cases}
        \end{align}
    [Solution]({{ "/notes/probability/chapters/exercises/a_normaltr.html" | relative_url }})

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

    Now suppose a tick comes into play independent of mosquito. It lands with $P=0.1$ and once landed, bites with $)=0.7$. Let $Y$ be the time between successive bug bites. Find $E[Y]$ and $Var(Y)$. [Solution]({{ "/notes/probability/chapters/exercises/a_mosquito.html" | relative_url }})

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

    We go fishing where we catch fishes at the rate of $0.6/hour$. We fish for two hours. If we do not catch a fish in the first two hours, we fist until the first catch. Find the following

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

1.  **Steady State Markov Process**

    Find the steady state probabilites of the following Markov Process [Solution]({{ "/notes/probability/chapters/exercises/a_steadymarkov.html" | relative_url }}){% include image.html url="notes/probability/images/exercises_1.png" img_classes="notes-img exercises_1" indent=true %}


1.  **Absorption Probabilities**

    Calculate the absorption probabilites for state $4$ and expected time to absortion from all states. (for absorption time, assume $p_{35} = 0$ and $p_{32} = 0.5$) [Solution]({{ "/notes/probability/chapters/exercises/a_absorbmarkov.html" | relative_url }})
    {% include image.html url="notes/probability/images/exercises_2.png" description="" img_classes="notes-img exercises_2" indent=true %}


1.  **Selecting Courses with Markov Process**
    {% include image.html url="notes/probability/images/exercises_3.png" description="" img_classes="notes-img exercises_3" indent=true %}

    Consider the above markov process for changing courses. The probability being in some course tomorrow given a course today is mentioned along the edges. Suppose we start with course 6-1 (Note that course 6 is the combination of courses 6-1, 6-2 and 6-3). Calculate the following

    1.  $P($eventually leaving course 6$)$.

    2.  $P($eventually landing in course 15$)$.

    3.  $E[$number of days till leaving course 6$]$.

    4.  At every switch for 6-2 to 6-1 or 6-3 to 6-1, we buy an ice cream (but a maximum of two). Calculate the $E[$number of ice creams before leaving course 6$]$.

    5.  Suppose we end up in 15. What is the $E[$number of steps to reach 15$]$.

    6.  Suppose we don't want to take course 15. Accordingly, when in 6-1, we stay there with probability $1/2$ while other three options have equal probabilities. If we are in 6-2, probability of going to 6-1 and 6-3 are in the same ratio as before. Calculate the $E[$number of days until we enter course 9$]$.

    7.  Assuming
        \begin{align}
            P(X_{n+1}=15 \vert X_{n}=9) &= P(X_{n+1}=9 \vert X_{n}=15) = P(X_{n+1}=15 \vert X_{n}=15)\newline
            &= P(X_{n+1}=9 \vert X_{n}=9) = 1/2
        \end{align}
        what is $P(X_{n}=15)$ and $P(X_{n}=9)$ far into the future.

    8.  Suppose
        \begin{align}
            P(X_{n+1}=6-1 \vert X_{n}=9) &= 1/8 \newline
            P(X_{n+1}=9 \vert X_{n}=9) &= P(X_{n+1}=15 \vert X_{n}=15) = 7/8
        \end{align}
        what is the $E[$number of days till return to 6-1$]$.

    [Solution]({{ "/notes/probability/chapters/exercises/a_markovcourse.html" | relative_url }})

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

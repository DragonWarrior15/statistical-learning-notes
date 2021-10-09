---
title: "Poisson Process"
---

## Poisson Process

### Poisson Random Variable

A random variable $X$ is said to be $Poisson(\lambda)$ if it has the following probability distribution
\begin{align}
        p_{X}(x = k) = \begin{cases} e^{-\lambda} \frac{\lambda^{k}}{k!} &\text{ for all } x = \{ 0,\;1,\;2, \cdots \}\newline
                                    0 &\text{ otherwise} \end{cases}
    \end{align}

### Mean and Variance

Expected value is calculated as follows
\begin{align}
        E[X] &= \sum_{k=0}^{\infty} ke^{-\lambda} \frac{\lambda^{k}}{k!} = \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}\newline
        &= \lambda e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!}\newline
        E[X] &= \lambda
    \end{align}

Variance can be calculated using $Var(X) = E[X^{2}] - E[X]^{2}$
\begin{align}
        E[X^{2}] &= \sum_{k=0}^{\infty} k^{2} e^{-\lambda} \frac{\lambda^{k}}{k!} = \lambda e^{-\lambda} \sum_{k=1}^{\infty} k\frac{\lambda^{k-1}}{(k-1)!}\newline
        &= \lambda e^{-\lambda} \sum_{k=0}^{\infty} (k+1) \frac{\lambda^{k}}{k!}\newline
        &= \lambda e^{-\lambda} \big( \lambda \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!} + \sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!} \big)\newline
        &= \lambda e^{-\lambda} (\lambda e^{\lambda} + e^{\lambda})\newline
        Var(X) &= E[X^{2}] - E[X]^{2}\newline
        Var(X) &= \lambda
    \end{align}

Thus, mean and variance is the same for a Poisson variable.

### Moment Generating Function

The mean and variance are easy to derive with the moment generating function of the Poisson distribution
\begin{align}
        E[e^{tX}] &= \sum_{k=0}^{\infty} e^{tk} e^{-\lambda} \frac{\lambda^{k}}{k!} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^{t})^{k}}{k!}\newline
        \phi(t) &= e^{-\lambda} e^{\lambda e^{t}} = e^{-\lambda(1-e^{t})}
    \end{align}

Now, we can use the derivates of this function to derive the expectations
\begin{alignat}{3}
        E[X] &= \phi^{\prime}(0) &&= e^{-\lambda(1-e^{t})} \lambda e^{t} &&= \lambda\newline
        E[X^{2}] &= \phi^{\prime\prime}(0) &&= \lambda e^{-\lambda(1-e^{t}) + t} (1+\lambda e^{t}) &&= \lambda^{2} + \lambda
    \end{alignat}

### Sum of Poisson Variables

The sum of $n$ independent random variables $X_{i} \sim Poisson(\lambda_{i})$, $i = 1, \ldots, n$ is also Poisson. This can be derived with their moment generating functions
\begin{align}
        E[e^{t(X_{1} + \cdots + X_{n})}] &= E[e^{tX_{1}}\cdots e^{tX_{n}}] = E[e^{tX_{1}}]\cdots E[e^{tX_{2}}] \;\text{by independence}\newline
        &= e^{-\lambda_{1}(1-e^{t})} \cdots e^{-\lambda_{n}(1-e^{t})} = e^{-(\lambda_{1} +\cdots + \lambda_{n})(1-e^{t})}\newline
        \implies X_{1} + \cdots + X_{n} &\sim Poisson(\lambda_{1} + \cdots + \lambda_{n})
    \end{align}

### Approximation of a Binomial Random Variable

Recall the probability distribution for a binomial random variable with parameters $n$ and $p$
\begin{align}
        P(X = i) = \binom{n}{i} p^{i} (1-p)^{n-i}
    \end{align}

Let $\lambda = np$ and $n$ be large while $p$ is very small (i.e., the probability of occurrence of the event is small with a large number of trials)
\begin{align}
        P(X = i) &= \frac{n!}{(n-i)!i!} (\frac{\lambda}{n})^{i} (1-\frac{\lambda}{n})^{n-i}\newline
        &= \frac{n(n-1) \ldots (n-i + 1)}{n^{i}} \frac{\lambda^{i}}{i!} \frac{(1-\lambda / n)^{n}}{(1 - \lambda / n)^{i}}\newline
        &\approx 1 \frac{\lambda^{i}}{i!} \frac{e^{-\lambda}}{1}\newline
        P(X = i) &\approx e^{-\lambda}\frac{\lambda^{i}}{i!}
    \end{align}

where have used the limit definition of $e$, $\lim_{n \to \infty}(1 + x/n)^{n} = e$. Examples where this approximation is valid include number of misprints on a page (the probability of a word being misprinted is small, and there are a large number of words on a page), number of transistors failing on first day of use (probability of failure is small, with extremely large number of transistors being used on any day). All these examples can be assumed to follow the Poisson distribution with mean $\lambda = np$.

### Poisson Process

Poisson process also falls in the realm of random processes but is different from Bernoulli process as it is a continuous time process. This process is very commonly used to model arrival times and number of arrivals in a given time interval.
\begin{align}
        P(k, \tau) &= \text{Probability of $k$ arrivals in interval of duration $\tau$}\newline
        \sum_{k} P(k, \tau) &= 1 \; \text{for a given $\tau$}
    \end{align}
Assumptions

-   The Probability is dependent only on the length of the interval $\tau$ and not the *location* of the interval

-   Number of arrivals in disjoint time intervals are *independent*

### A Special Counting Process

A counting process $N_{t}:t \in [0,\infty)$ is a Poisson process with rate $\lambda$ if

1.  $N_{0} = 0$

2.  $N_{t}$ is composed of independent and stationary increments

3.  The number of arrivals in any time interval $\tau > 0$ has $Possion(\lambda \tau)$ distribution

Hence, for a Poisson process, the number of arrivals in any interval is dependent only on the length of that interval and not the location. Further, the number of arrivals in the interval will follow a Poisson distribution.

### Derivation from Bernoulli Process

For a very small interval $\delta$,
\begin{align}
        P(k, \delta) &= \begin{cases} 1-\lambda \delta &\mbox{$k = 0$}\newline
                                     \lambda \delta &\mbox{$k = 1$}\newline
                                     0 &\mbox{$k > 2$} \end{cases} + O(\delta^{2})\newline
        \lambda &= \lim_{\delta \to 0}\frac{P(1,\delta)}{\delta} \quad \text{arrival rate per unit time}\newline
        E[k] &= (\lambda \delta) * 1 + (1-\lambda \delta) * 0\newline
            &= \lambda \delta \newline
        \tau &= n \delta
    \end{align}

The last equation clearly implies that we can approximate the whole process as a bernoulli process where we have $n$ miniscule time intervals with at most one arrival per interval.
\begin{align}
        P(k\; \text{arrivals}) &= \binom{n}{k} p^{k} (1-p)^{n-k} \newline
            &= \binom{n}{k} (\frac{\lambda \delta}{n})^{k} (1 - \frac{\lambda \delta}{n})^{n-k}\newline
        \lambda \tau &= np \quad \text{or, arrival rate * time = E[arrivals]}\newline
        Poisson &= \lim_{\delta \to 0, n \to \infty} Bernoulli\newline
        or,\; P(k, \tau) &= \frac{(\lambda \tau)^{k} e^{-\lambda \tau}}{k!} \quad \text{$k = 0,1, \cdots$, for a given $\tau$}\newline
        where,\; \sum_{k} P(k, \tau) &= 1 \quad \text{for a given $\tau$}
    \end{align}

Let $N_{t}$ denote the no of arrivals till time t, then
\begin{align}
        E[N_{t}] &= \lambda t\newline
        Var(N_{t}) &= \lambda t\newline
        P(N(t) = k) &= e^{-\lambda t} \frac{(\lambda t)^{k}}{k!}, \; \text{for $k=0,1,2,\ldots$}
    \end{align}

### Time till kth arrival

Suppose the $k^{th}$ arrival happens at a time $t$. Then we are saying that there have been $k-1$ arrivals till time $t$ and the $k^{th}$ arrival happens at time $t$ (precisely in an interval of $[t, t+\delta]$). Let $Y_{k}$ be the required time,
\begin{align}
        f_{Y_{k}}(t)\delta &= P(t \leq Y_{k} \leq t+\delta)\newline
                    &= P(\text{$k-1$ arrivals  in $[0,t]$}) (\lambda \delta)\newline
                    &= \frac{(\lambda t)^{k-1}}{(k-1)!}e^{-\lambda t}(\lambda \delta)\newline
        f_{Y_{k}}(t) &= \frac{\lambda^{k} t^{k-1}}{(k-1)!}e^{-\lambda t} \quad \text{Erlang Distribution}\newline
        &= \frac{\lambda e^{-\lambda t}(\lambda t)^{k-1}}{\Gamma (k)}
    \end{align}
which is nothing but the pdf of a Gamma distribution.

### Time of 1st Arrival

Using the Erlang Distribution described above, we have
\begin{align}
        f_{Y_{1}}(t) = \lambda e^{-\lambda t}
    \end{align}
$Y_{k} = T_{1} + T_{2} + \cdots + T_{k}$ where all $T_{i}$ are independent and exponential distributions. And as derived above, and discussed later, the sum of independent exponential variables is a Gamma distribution.

### Renewal Process

Poisson process can be seen as a special case of a renewal process, when the interarrival times are all exponentially distributed.
\begin{alignat}{3}
        \text{Interarrival time }& \xi_{i}&& = \lambda e^{-\lambda t}\newline
        \text{Number of arrivals }& P(N_{t} = n)&& = \frac{(\lambda t)^{n}}{n!} e^{-\lambda t}\newline
        \text{Time till $n$th arrival }& P(S_{n} = t)&& = \lambda \frac{(\lambda t)^{n-1}}{(n-1)!} e^{-\lambda x} \text{ for $t > 0$}\newline
        \text{Cumulative distribution }& P(S_{n} \leq t)&& = \begin{cases} 1 - e^{-\lambda t} \sum_{k=1}^{n-1} \frac{(\lambda t)^{k}}{k!} &\mbox{if $t > 0$}\newline
        0 &\mbox{otherwise} \end{cases}
    \end{alignat}

### Merging of Poisson Processes

Merging of two Poisson processes is also a Poisson process. Consider two flasbulbs of Red and Green colours, flashing as Possion processes with rates $\lambda_{1}$ and $\lambda_{2}$. Then the process denoting the combined flashing of the two bulbs is also Poisson.

Consider a very small interval of time $\delta$. In this small interval, any of the individual bulbs can have at most one flashes (since we ignore higher order terms). Thus, the following four possibilities arise


| . | $Red$ | $\overline{Red}$ |
| - | ----- | ---------------- |
| $Green$ | $\lambda_{1} \delta \lambda_{2} \delta$ | $(1-\lambda_{1}\delta)  \lambda_{2} \delta$ |
| $\overline{Green}$ | $\lambda_{1} \delta (1-\lambda_{2}\delta)$ | $(1-\lambda_{1}\delta) (1-\lambda_{2}\delta)$ |


| . | $Red$ | $\overline{Red}$ |
| - | ----- | ---------------- |
| $Green$ | $0$ | $\lambda_{2} \delta$ |
| $\overline{Green}$ | $\lambda_{1} \delta$ | $(1-(\lambda_{1} + \lambda_{2}) \delta)$ |

The combined process (of at least one bulb flashing) $\sim Poisson(\lambda_{1} + \lambda_{2})$

\begin{align}
    P(\text{arrival happened from first process}) = \frac{\lambda_{1} \delta}{\lambda_{1} \delta + \lambda_2 \delta} = \frac{\lambda_{1}}{\lambda_{1} + \lambda_{2}}
    \end{align}

### Splitting of Poisson Process

Suppose we have a Poisson process with parameter $\lambda$ which we split into two processes up and down, with probabilities $p$ and $1-p$. The two resulting processes are also Poisson with different parameters.

Consider a small time slot of length $\delta$. Then,
\begin{align}
        P(\text{arrival in this time slot}) &= \lambda \delta\newline
        P(\text{arrival in up slot}) &= \lambda \delta p\newline
        P(\text{arrival in down slot}) &= \lambda \delta (1-p)
    \end{align}
Thus, up and down are themselves Poisson with parameters $\lambda p$ and $\lambda (1-p)$ respectively.

### Random Indcidence for Poisson

Suppose we have a Poisson process with parameter $\lambda$ running forever. We show up at a random time instant. What is the length of the chosen interarrival time (the total of the time from the last arrival to the next arrival).

Let $T_{1}^{\prime}$ denote the time that has elapsed since the last arrival and $T_{1}$ be the time till the next arrival. Note that the reverse process is also Poisson with the same parameter. Thus,
\begin{align}
        E[\text{interarrival time}] = E[T_{1}^{\prime} + T_{1}] = \frac{1}{\lambda} + \frac{1}{\lambda} = \frac{2}{\lambda}
    \end{align}

This may seem paradoxical since the time difference between any two arrivals in a Poisson process is same and it's expected length is $\frac{1}{\lambda}$, whereas we got an interval twice this length. The paradox is resolved by considering the fact that when we choose a random point in time, it is more likely to fall in an interval of larger size than the smaller ones (since probability will be proportional to the length of the interval).


Consider a separate example where we want to compare two values $E[\text{size of a family}]$ and $E[\text{size of a family of a given person}]$.

The two value will be different due to the underlying nature of the way experiment is conducted. For the first, we randomly choose families and average their sizes. Here, family of any size is equally likely to be picked. In the second case, we first pick a person from the population, get their family size, and then average the sizes of the families. Note that, this experiment is biased since the we are more likely to select people from larger families (or equivalently, it is more likely that we pick a person from a large family since the probability of picking is proportional to the family size). Hence, the second value will likely be larger and the two quantities are not equal.

### Non Homogenous Poisson Process

Sometimes, it may not be accurate to use a simple Poisson process to model arrival. For example, a restaurant will not have the same rate of influx throughout the day. This rate itself is a function of time. In such cases, we model the arrivals as Non Homogenous Poisson Process.


For such a process, we have $\lambda(t): [0,\infty) \to [0, \infty)$ and the counting process $N_{t}$ is non homogenous if the following hold

1.  $N_{0} = 0$

2.  The increments to $N_{t}$ are **independent but not stationary**

3.  For any small time interval $\delta$, the probability of more than 1 arrival in the interval is zero

The distribution of arrivals in a time interval is still Poisson, but the Poisson parameter is now dependent on the location of the interval itself (since the process does not have stationary increments)
\begin{align}
        N_{t+s} - N_{t} \sim Poisson(\int_{t}^{t+s} \lambda(\alpha) d\alpha)
    \end{align}

# Answer

Interarrival times is exponentially distributed with mean $E[X] = 10 = 1/\lambda$. Hence $\lambda = 0.1$.

1\. For part 1, we need at least 10 requests within one hour. Implies that the sum of the first 10 interarrival times should be less than 60 minutes.

$$
\begin{aligned}
    P(T_{1} + \cdots + T_{10} < 60)
\end{aligned}
$$

We know that the sum of independent exponential variables is Gamma distribution. Hence,

$$
\begin{aligned}
    P(Gamma(10, 0.1) < 60) = 0.08392
\end{aligned}
$$


2\. Similar to the above part, we need the sum of first 10 interarrival times to be more than two hours

$$
\begin{aligned}
    P(T_{1} + \cdots + T_{10} \geq 120) = P(Gamma(10, 0.1) \geq 120) = 0.24239
\end{aligned}
$$


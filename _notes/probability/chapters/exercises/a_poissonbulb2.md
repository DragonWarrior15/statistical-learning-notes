---
title: "Answer"
---

1.
    \begin{align}
                    E[\text{time till failure}] &= E[\text{time till failure} \vert A]P(A) + E[\text{time till failure} \vert B]P(B)\newline
                    &= \frac{1}{\lambda_{A}} \frac{1}{2} + \frac{1}{\lambda_{B}} \frac{1}{2}\newline
                    &= \frac{1}{2}(1 + \frac{1}{3}) = \frac{2}{3}
                \end{align}

2.  Let $C$ denote the event of no failure till time $t$. $P(C)$ for a given $\lambda$ will be $\int_{t}^{\infty} \lambda e^{-\lambda t}$. Then,
    \begin{align}
                    P(C) &= P(C \vert A)P(A) + P(C \vert B)P(B) \quad \text{Using total probability theorem}\newline
                         &= e^{-t}(\frac{1}{2}) + e^{-3t}(\frac{1}{2})\newline
                         &= \frac{1}{2}(e^{-t} + e^{-3t})
                \end{align}

3.  Let $C$ denote the event of no failure till time $t$. Then,
    \begin{align}
                    P(A \vert C) &= \frac{P(C \vert A)P(A)}{P(C)}\newline
                           &= \frac{P(C \vert A)P(A)}{P(C \vert A)P(A) + P(C \vert B)P(B)}\newline
                           &= \frac{\frac{1}{2} e^{-t}}{\frac{1}{2}(e^{-t} + e^{-3t})}\newline
                           &= \frac{1}{1 + e^{-2t}}
                \end{align}

4.  Let $T_{B1}, T_{B2}$ and $T_{A}$ denote the life times of the first B bulb, second B bulb and the A bulb respectively. First consider the solution to $P(T_{B1} + T_{B2} = t)$
    \begin{align}
                    P(T_{B1} + T_{B2} = t) &= \int_{0}^{t} P(T_{B1} = t_{1})P(T_{B2} = t - t_{1}) dt_{1} \quad\text{Using independence}\newline
                    &= \int_{0}^{t} 3e^{-3t_{1}} 3e^{-3(t - t_{1})} dt_{1}\newline
                    &= \int_{0}^{t} 9e^{-3t}dt_{1}\newline
                    &= 9te^{-3t}
                \end{align}

    Now, we can rewrite the requred probability in a slightly different format
    \begin{align}
                    P(T_{B1} + T_{B2} > T_{A}) &= P(T_{B1} + T_{B2} = t)P(T_{A} \leq t)\newline
                    &= \int_{0}^{\infty} 9te^{-3t} (\int_{0}^{t} e^{-t_{1}}dt_{1}) dt\newline
                    &= \int_{0}^{\infty} 9te^{-3t} (1 - e^{-t}) dt\newline
                    &= \int_{0}^{\infty} 9te^{-3t} - 9te^{-4t} dt\newline
                \end{align}
    Using integration by parts, $\int uv^{\prime} = uv - \int u^{\prime}v$ and choosing $u = t, v = e^{-3t}/3$,
    \begin{align}
                    P(T_{B1} + T_{B2} > T_{A}) &= \bigg[ 9[te^{-3t}]\_{0}^{\infty} - 3\int_{0}^{\infty} e^{-3t}dt -9[te^{-4t}]\_{0}^{\infty} + \frac{9}{4}\int_{0}^{\infty} e^{-4t}dt  \bigg]\newline
                    &= 0 + 1 - 0 - \frac{9}{16} = \frac{7}{16}
                \end{align}

5.  Let there be $N$ bulbs of type B out of the 12 bulbs. Clearly $N$ is a random variable and can be seen as the *successes* of choosing a given bulb as B. and the probability of choosing any $i$th bulb as B is $1/2$.

    Let the life time of any bulb of type B be $T$. Then the total lifetime of all the type B bulbs will be $NT$, which is nothing but the sum of a random number of random variables.

    \begin{align}
                    E[NT] &= E[N]E[T] = np \times \frac{1}{\lambda} = 12 \times \frac{1}{2} \times \frac{1}{3} = 2\newline
                    Var(NT) &= E[Var(NT \vert N)] + Var(E[NT \vert N]) = E[N]Var(T) + E[T]^{2}Var(N)\newline
                    &= np \times \frac{1}{\lambda^{2}} + (\frac{1}{\lambda})^{2} np(1-p) = 1
                \end{align}

6.  Let $D$ be the event that the lifetime is greater thatn $t$ or $T > t$. Then,
    \begin{align}
                    E[T \vert D] &= E[T \vert D,A]P(A \vert D) + E[T \vert D,B]P(B \vert D)\newline
                    &= t + (E[T-t \vert D,A]P(A \vert D) + E[T-t \vert D,B]P(B \vert D))\newline
                    &= t + (\frac{1}{1}P(A \vert D) + \frac{1}{3}P(B \vert D)) \quad\text{Using memoryless property}\newline
                    &= t + (\frac{1}{1 + e^{-2t}} + \frac{1}{3}(1 - \frac{1}{1 + e^{-2t}})) \quad\text{Using part 3}\newline
                    &= t + \frac{1}{3} + \frac{2}{3}\frac{1}{1 + e^{-2t}}
                \end{align}

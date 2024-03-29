---
title: "Answer"
---

A very straightforward way is to use a triple integral
\begin{align}
            P(X < Y < Z) = \int_{0}^{\infty} \int_{0}^{z} \int_{0}^{y} \lambda e^{-\lambda x} \mu e^{-\mu y} \nu e^{-\nu z} dx dy dz = \frac{\lambda \mu}{(\lambda + \mu + \nu)(\mu + \nu)}
        \end{align}
$P(X < Y < Z)$ can be broken down as $P(X < min(Y,Z)) P(Y < Z)$.

Consider just $P(Y < Z)$
\begin{align}
            P(Y < Z) = \int_{0}^{\infty} \int_{0}^{z} \mu e^{-\mu y} \nu e^{-\nu z} dy dz = \frac{\mu}{\mu + \nu}
        \end{align}
Thus, when two exponential processes are considered, probaility of arrival of 1st before 2nd is simply the percentage ratio of parameters. Thus,
\begin{align}
            P(X < min(Y,Z)) &= \frac{\lambda}{\lambda + (\mu + \nu)} \quad\text{$Y$ and $Z$ can be combined as a single process}\newline
            P(Y < Z) &= \frac{\mu}{\mu + \nu}\newline
            P(X < Y < Z) &= P(X < min(Y,Z)) P(Y < Z)\newline
                        &= \frac{\lambda \mu}{(\lambda + \mu + \nu)(\mu + \nu)}
        \end{align}

where we have also used the property that minimum of exponentially distributed random variables is itself exponentially distributed.

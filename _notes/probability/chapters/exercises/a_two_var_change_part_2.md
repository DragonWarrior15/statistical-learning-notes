---
title: "Answer"
---

We will utilise Jacobians with partitioning to solve for both the parts.

For the first part, consider the following two inverses on two disjoint paritions
\begin{align}
    X &= \begin{cases}
        -\sqrt{Y} &\mbox{$-1 < x < 0$}\newline
        \sqrt{Y} &\mbox{$0 \leq x < 1$}
    \end{cases}\newline
    \implies J &= \begin{cases}
        \lvert-\frac{1}{2\sqrt{Y}}\rvert &\mbox{$-1 < x < 0$}\newline
        \lvert\frac{1}{2\sqrt{Y}}\rvert &\mbox{$0 \leq x < 1$}
    \end{cases} = \frac{1}{2\sqrt{Y}} \quad \text{throughout}\newline
    \implies f_{Y}(y) &= \frac{1}{2} \frac{1}{2\sqrt{y}} \quad \forall x
\end{align}

However, we must note that the range of $y$ is same in both the partitions. Hence, we will need to sum up the two pmf to obtain the final pmf of y.
\begin{align}
    f_{Y}(y) = \frac{1}{2} \frac{1}{2\sqrt{y}} + \frac{1}{2} \frac{1}{2\sqrt{y}} = \frac{1}{2\sqrt{y}} \quad 0 < y < 1
\end{align}

For the second part, we partition in a similar manner
\begin{align}
    X &= \begin{cases}
        -\sqrt{Y} &\mbox{$-1 < x < 0$}\newline
        \sqrt{Y} &\mbox{$0 \leq x < 3$}
    \end{cases}\newline
    \implies J &= \begin{cases}
        \lvert-\frac{1}{2\sqrt{Y}}\rvert &\mbox{$-1 < x < 0$}\newline
        \lvert\frac{1}{2\sqrt{Y}}\rvert &\mbox{$0 \leq x < 3$}
    \end{cases} = \frac{1}{2\sqrt{Y}} \quad \text{throughout}\newline
    \implies f_{Y}(y) &= \frac{1}{4} \frac{1}{2\sqrt{y}} \quad \forall x
\end{align}

Now, the range of $Y$ is different in the two partitions. Consider the following
\begin{align}
    f_{Y}(y) &= \begin{cases}
        \frac{1}{4} \frac{1}{2\sqrt{y}} &\mbox{$-1 < x < 0$ or $0 < y < 1$}\newline
        \frac{1}{4} \frac{1}{2\sqrt{y}} &\mbox{$0 \leq x < 1$ or $0 \leq y < 1$}\newline
        \frac{1}{4} \frac{1}{2\sqrt{y}} &\mbox{$1 \leq x < 3$ or $1 \leq y < 9$}
    \end{cases}
\end{align}

Wherever the partitions overlap for the values of $y$, we will add the pmf
\begin{align}
    f_{Y}(y) &= \begin{cases}
    \frac{1}{2} \frac{1}{2\sqrt{y}} &\mbox{$0 < y < 1$}\newline
    \frac{1}{4} \frac{1}{2\sqrt{y}} &\mbox{$1 \leq y < 9$}
    \end{cases}\newline
\end{align}

One can verify that the pmf indeed integrates to 1 over the entire support of y $0 < y < 9$. Another interesting observation is that the total probability over the two regions is $1/2$ since they divide the original region of $x$ into two parts as well.

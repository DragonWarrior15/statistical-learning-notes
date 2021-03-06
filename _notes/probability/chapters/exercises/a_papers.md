---
title: "Answer"
---

Note that the process till the end is a combination of multiple binomial process, such that any process lasts till the first success. Suppose we sign a paper and keep this in the drawer. Now the total signed papers in the drawer is $k$ out of $n$ and the $P($success$)$ = $\frac{n-k}{n}$ and $E[$draws till next unsigned paper$] = \frac{1}{p} = \frac{n}{n-k}$. Total draws
\begin{align}
            E &= \frac{n}{1} + \frac{n}{2} + \cdots + \frac{n}{n}\newline
             &= n(1 + \frac{1}{2} + \cdots + \frac{1}{n})\newline
            \lim_{n \to large} E &= n \log(n) 
        \end{align}

---
title: Incremental Remainders
---

### Question: Find the smallest number that leaves a remainder of 1 when divided by 2, remainder of 2 when divided by 3, and so on, upto a remainder of 9 when divided by 10. 

### Solution
Lets consider the base case of remainder of 1 when divided by 2 and remainder of 2 when divided by 3. The smallest number satisfying this 5, which is LCM(2, 3) - 1.

This idea stems from the fact that the answer can be written in the below form for positive integers
\begin{align}
    X &= 2X_{1} + 1\newline
    X &= 3X_{2} + 2\newline
    X &= 10X_{9} + 9\newline
\end{align}

which can be rearranged to be written as
\begin{align}
    X + 1 &= 2(X_{1} + 1)\newline
    X + 1 &= 3(X_{2} + 1)\newline
    X + 1 &= 10(X_{9} + 1)\newline
\end{align}

Meaning, the answer we are looking for is LCM(2, 3, .., 10) - 1

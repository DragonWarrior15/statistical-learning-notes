---
title: "Random Numbers"
---

## Random Numbers

We can generate random numbers using the following equation
\begin{align}
        x_{n+1} = (ax_{n} + c) mod(m)
    \end{align}
$x_{n}$ takes the values $1,2,\ldots, m-1$ and we take $x_{n}/m$ as the pseudo random number, which is uniformly distributed between $(0,1)$ for suitable choice of $a, c, m$.


### Permutation of Integers

Suppose we want to generate a permutation of integers from $1, 2, \ldots, n$ such that each of the permutations is equally likely. Assuming we have a uniform random generator $U$ with us,
\begin{align}
        P(Int(kU) + 1 = i) &= P(Int(kU) = i-1) = P(i-1 \leq kU < i)\newline
        &= P(\frac{i-1}{k} \leq U < \frac{i}{k}) = \frac{1}{k}
    \end{align}
which gives us randomly generated random integers between $1$ and $k$ with equal probability. An easy way to generate permutation is

1.  Choose a permutation $r_{1}, r_{2}, \ldots, r_{n}$ which can just be $r_{j} = j$

2.  Let $k = n$

3.  Choose a random number $U$ and let $I = Int(kU) + 1$

4.  Interchange numbers at position $k$ and $I$

5.  $k = k-1$

6.  if $k > 1$ goto step 3 else return permutation

The above algorithm can also be used to get a random subset of size $r$ from a set $1, \dots, k$ by simply running the algorithm till $k = r$ since the elements in the last $r$ positions can be selected. For $r > n/2$, we find the $k=n-r$ elements not in the subset.

---
title: "Answer"
---

Let $X$ be the number of tosses till the first coin is removed. This is a geometric random variable with $P($success$) = \frac{1}{8}$. then $E[X] = 1/p = 8$. Now $Y$ be the number of tosses till the second coin is removed (counting tosses after removal of first coin). Note that geometric random variables are memory less and what happened before the start of the *experiment* will not matter. Thus, $E[Y] = 1/(1/4) = 4$. Similarly, $Z$ is the tosses till the last coin is removed and $E[Z] = 1/(1/2) = 2$. Note that the number of tosses till the end of experiment is simply $X + Y + Z$. $E[X+Y+Z] = E[X] + E[Y] + E[Z] = 14$.

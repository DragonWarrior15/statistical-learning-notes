---
title: "Answer"
---

Note that $E[Z|X,Y]$ will be a function of both $X$ and $Y$.
\begin{align}
            E[Z|X,Y] &= \sum_{z} z p_{Z|X,Y}(z|x,y)\newline
            E[E[Z|X,Y]|X] &= \sum_{y} E[Z|X,Y]p_{X,Y|X}(x,y|x)\newline
                        &= \sum_{y} \sum_{z} z p_{Z|X,Y}(z|x,y) p_{Y|X}(y|x)\newline
                        &= \sum_{y} \sum_{z} z \frac{p_{X,Y,Z}(x,y,z)}{p_{X}(x)}\newline
                        &= \sum_{z} z \sum_{y} \frac{p_{X,Y,Z}(x,y,z)}{p_{X}(x)}\newline
                        &= \sum_{z} z \frac{p_{X,Z}(x,z)}{p_{X}(x)}\newline
                        &= \sum_{z} z p_{Z|X}(z|x)\newline
                        &= E[Z|X]
        \end{align}

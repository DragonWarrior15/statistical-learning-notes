---
title: "Gradient Descent"
---

# Gradient Descent

Gradient descent is a general technique that aims to adjust parameters of a function/model until a goal is achieved. In machine learning terms, we use a real valued loss function that tells how good or bad we are doing on a given problem. Gradient descent enables us to systematically adjust model parameters until we achieve a minima on our loss function. Gradients give the direction of maximum change of the real valued function, thus moving along such a direction will help reach us the minima the fastest.


Gradients are typically defined with respect to a scalar quantity only.


The general update equation will be
\begin{align}
    w_{n+1} = w_{n} - \alpha \frac{dL}{dw}\end{align}
where $dL/dw$ is the gradient and $\alpha$ signifies how far in that direction we need to move. Gradient gives the value and direction of the fastest increase. Hence we use a negative symbol to move in the opposite direction. $w$ is the parameter of intereset we are trying to find.


Suppose we have the problem of minimizing the function $f(x) = 2x^{2}$. We can do this directly by setting the derivative to 0
\begin{align}
    \frac{df}{dx} &= 0 = 4x\newline
    \implies x&= 0\end{align}
or we can use gradient descent recursively to calculate this point. Starting at $x=1$,
\begin{align}
     x_{1} &= x_{0} - 0.1 * (4x_{0}) = 0.6\newline
     x_{2} &= x_{1} - 0.1 * (4x_{1}) = 0.36\newline\end{align}
and so on. Gradient descent in it's vanilla form is seldom used when training neural networks. The value of learning rate $\alpha$ is critical in determining the jump size. A very small jump and we reach the minima too slow. A large jump and the gradients will keep oscillating haphazardly. The loss surface of large models is often complex, and may contain several minima. Sometimes, it is of interest to escape local minima and look for better points on this surface. Optimizers implement such complex update rules for us to overcome this problem. First let's look at how to calculate gradient of commonly encountered scenarios in deep learning.

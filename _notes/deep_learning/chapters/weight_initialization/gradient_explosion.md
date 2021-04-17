---
title: "Weights Initialization"
---

# Weights Initialization
# Exploding and Vanishing Gradients

An incorrect weights initialization can be quite problematic as it can lead to the problem of exploding or vanishing gradients. This can make the neural network not learn at all.


Consider a $L$ layered neural network, without any activations and same values for all matrices, i.e., a linear combination of $L$ matrices. The final output will be
\begin{align}
    \hat{y} &= XW^{L-1}W_{L}\end{align}
Suppose, for argument's sake, the values of matrix $W$ are slightly more than 1. When we multiply several such matrices together, $W^{L-1}$ will grow exponentially. This will cause large values of loss, and in the final layers of the network, we will get very large gradient values.


In the opposite case where the values of matrix are smaller than 1, the value of output shrinks exponentially. If we consider the gradients in the initial layers, we are looking at very small values for the gradients. This will cause the initial layers to not learn, making the whole network not learn anything at all.


Thus, the network must be correctly initialized so that it learns, and does so in a smooth and fast manner.

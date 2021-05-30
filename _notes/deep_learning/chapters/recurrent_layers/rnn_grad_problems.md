---
title: "Exploding and Vanishing Gradient"
---

## Exploding and Vanishing Gradient

Based on BPTT, it is clear that for long sequences, there will be several multiplication terms for calculating the gradients. If the individual values are all small or big, the gradient can shrink or grow rapidly. In either case, the network is not able to learn properly and may never converge. Some strategies to mitigate the problem are

-   Truncated backprop: Instead of calculating gradients on all time steps, we fix the length of the sequence and only calculate the gradients through those time steps. This reduces the possibility of multiplication of several terms.

-   Use identity matrix for initialization of weights and ReLU activation. This allows the gradient to not deviate too much from $1$, and ReLU will not let the gradient decay too fast.

-   To deal with exploding gradients, clip the gradient value to a pre-determined value. This will stabilize the learning by denying exponentially growing gradient in the network.

-   Using skip connections to allow for gradient flow. Mathematically
    \begin{align}
            y &= F(x) + x
        \end{align}
    Since we are adding the input to the output as it is, the gradient will have the constant component of $1$, allowing gradient to not become very small.

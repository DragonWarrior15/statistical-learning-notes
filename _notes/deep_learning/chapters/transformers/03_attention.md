## Attention
To solve for symmetric self attention, we begin introducing assymmetry by forming Keys, Queries and Value vectors using their own matrices that are learnt while training

$$
\begin{aligned}
K &= XW^{k}\\
Q &= XW^{q}\\
V &= XW^{v}\\
Y &= \text{Softmax}(QK^{T})V
\end{aligned}
$$

There will be bias parameters too, but we assume they are baked into the matrices themselves, with a single column of 1s added to the input matrix $X$.

### Scaled Attention
Typical formulations look as below

$$
\begin{aligned}
Y = \text{Attention}(K, Q, V) = \text{Softmax}\left[\frac{QK^{T}}{\sqrt{D}}\right]V
\end{aligned}
$$

The term $\sqrt{D}$ is based on the variance of the dot product of unit vectors with mean $0$ and variance $1$ (independent variables.)

$$
Var(a \cdot b) = \sum_{i=1}^{D} Var(a_{i}b_{i}) = \sum_{i=1}^{D} Var(a_{i}) Var (b_{i}) = \sum_{i=1}^{D} = D
$$

The third part of this equation comes from the independence of the random variables.

Hence, to transform a random variable with Variance $D$ to have a unit variance, we divide it by $\sqrt{D}$.

## Attention Heads
So far we have discussed a single attention heads. However, multiple heads are relevant at the same time. Consider natural language, where one head to relate to vocabulary, another to tense, another to prepositions etc.

We use multiple independent heads, each with its own separate learnable parameters. This is very similar to multiple filters that are used in a single layer of a Convolutional Neural Network (CNN).

Suppose we have $1, ..., H$ heads

$$
\begin{aligned}

\end{aligned}
$$
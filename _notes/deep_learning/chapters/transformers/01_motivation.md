# Transformers Motivation
Transformers are the core block of a lot of modern LLM architectures.

It is based on the core concept of attention. A network gives different weights to different types of inputs. The weights can also depend on inputs.

The name transformers basically means you _transform_ the input vectors into a set of output vectors. This output representation is essentially in a different space which captures more semantic meaning than the original space. Transfer learning is also very effective here since we have now transformed the vectors into a semantically richer space.

Because of their implementation, they are well suited for parallelization on GPUs. Meaning, we can train faster on large datasets, and also run inference quickly.

## Mathematical Formulation
Input is a set of vectors $\{x_n\}$ of dimensionality $D$.
$n = 1,...,N$ represents individual tokens.

Input is a matrix $X$ of dimensions $N \times D$.

$$\tilde{X} = \text{Transformer Layer}[X] \quad \text{where, dim}(\tilde{X}) = \text{dim}(X)$$

Multiple such layers can be stacked up to create deep networks to learn more powerful representations.

If the output is $y_{1}, ..., y_{N}$, then we want $y_{n}$ to be a linear combination of $x_{i}$ such that coefficient of important $x_{i}$ is higher and vice versa. To keep coefficients bounded, we add some constraints

$$
\begin{aligned}
y_{n} &= \sum_{m=1}^{N} a_{nm}x_{m}\\
\\
0 &\le a_{nm} \le 1\\
\sum_{m=1}^{N}a_{nm} &= 1
\end{aligned}
$$
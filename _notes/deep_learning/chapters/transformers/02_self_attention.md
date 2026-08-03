## Self Attention

### Analogy to Movie Retrieval
Each movie is whats called a _Value_. Each movie will have several associated attributes that will be called _Keys_. When a user comes in, they bring in their own set of attributes called _Query_. Librarian tries to match _Query_ with _Keys_ to retrieve the best mathing movie or _Value_ for the User.

We can also generalize this concept to continuous variables where its called _soft attention_.

### Mathematical Formulation
The most basic version can use $x_{n}$ as the value vector, the key vector and as the query vector for $y_{n}$.

The simplest approach in this case is to take the dot product, since similarity is mesasured by that

$$
\begin{aligned}
a_{nm} &= \frac{\exp({x_{n}^{T}x_{m}})}{\sum_{m'=1}^{N}\exp{(x_{n}^{T}x_{m})}}\\[4ex]
Y &= \text{Softmax}[XX^{T}]X
\end{aligned}
$$

where the _Softmax_ makes each row independently sum up to 1

Note that there is no learnable parameter in this formulation. Hence the flexibility of this formulation is low. There is one simple solution to solve this. Before ingesting in this formulation, modify $X$ by multiplying it with a matrix $U$ of learnt parameters

$$
\begin{aligned}
Y &= \text{Softmax}[XUU^{T}X^{T}]XU
\end{aligned}
$$

This is flexible, but still is symmetric. We need attention to be assumetric. Consider the example of two words chisel and tool. Every chisel is a tool hence chisel should attend strongly to tool. But every tool is not a chisel since there are several types of tools. Hence the attention of tool to chisel should not be as strong.

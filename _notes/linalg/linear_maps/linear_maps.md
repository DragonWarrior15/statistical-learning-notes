---
title: "Complex Field"
---

# Linear Maps
## Linear Maps
Let $\setv$ and $\setw$ denote two vector spaces. Then, a linear map $T$ is a function from $\setv$ to $\setw$ that satisfies the following properties
* **Additivity**
    $T(u + v) = Tu + Tv$ for all $u,v \in \setv$
* **Homogeneity**
    $T(\lambda v) = \lambda(Tv)$ for all $v \in \setv$

Some people can refer to linear maps as linear transformations. We can also see the notation $T(v)$ instead of $Tv$ to represent $T$ as an operator, although both are correct.\newline

The set of all linear maps from $\setv$ to $\setw$ is denoted by $\setlm(\setv, \setw)$. Examples of linear maps are the \textbf{identity map} (maps an element to itself, identity map $\in \setlm(\setv, \setv)$), differentiation, integration etc.\newline

An important class of linear maps is from $\field^{n}$ to $\field^{m}$ and can be denoted by the following transformation
\begin{gather}
(x_{1}, x_{2}, \ldots, x_{n}) \in \field^{n}\newline
    T(x_{1}, \ldots, x_{n}) = (A_{1,1}x_{1} + \cdots + A_{1,n}x_{n}, \ldots, A_{m,1}x_{1} + \cdots + A_{m,n}x_{n})
\end{gather}

If we are working with the basis vectors for $\setv$ and $\setw$ of same dimensions, then there exists a unique linear map such that
\begin{align}
    Tv_{j} = w_{j} \quad \forall \quad j = 1,2,\ldots,n
\end{align}
where $v$ and $w$ are basis vectors for $\setv$ and $\setw$ respectively.

<!--####################### -->
### Properties
We can define addition and scalar multiplication on the set of linear maps $\setlm(\setv, \setw)$ as follows
\begin{gather}
    (S + T)(v) = S(v) + T(v) \quad \text{and} \quad (\lambda T)(v) = \lambda(Tv)\newline
    S,T \in \setlm(\setv, \setw), \lambda \in \field, v \in \setv
\end{gather}

With the addition and multiplication operations defined, we notice that this set of linear maps $\setlm(\setv, \setw)$ is a vector space.\newline

\textbf{Product of Linear Maps}\newline
Product of linear maps is defined as follows
\begin{gather}
    (ST)(u) = S(Tu)\newline
    T \in \setlm(U, \setv), S \in \setlm(\setv, \setw), ST \in \setlm(U, \setw)
\end{gather}
for all $u \in U$. $ST$ is only defined when $T$ maps into the domain of $S$. Note that $ST \neq TS$ always. For the equality to hold, both left and right side of the equations must make sense, and the products must indeed be equal.\newline

Additionally, linear maps will satisfy several additional algebraic properties
* **Associativity**
    $(T_{1}T_{2})T_{3} = T_{1}(T_{2}T_{3})$ whenever both $T_{1}T_{2}$ and $T_{2}T_{3}$ make sense. All these three linear maps will be defined on different sets.
* **Identity**
    $TI = IT = T$ where the first identity map is on $\setv$ while the second identity map is on $\setw$ for the product of linear maps to make sense.
* **Distributive Property**
    $(S_{1} + S_{2})T = S_{1}T + S_{2}T$ and $S(T_{1} + T_{2}) = ST_{1} + ST_{2}$\newline where all the products make sense and $S_{1}, S_{2}, S \in \setlm(U, \setv)$ and $T_{1}, T_{2}, T \in \setlm(\setv, \setw)$.

<!--####################### -->
### Null Space
Null space is the subset that get mapped to 0. Mathematically
\begin{gather}
    \text{null }T = \{ v \in \setv \; \text{ such that } \; Tv = 0 \}, T \in \setlm(\setv, \setw)
\end{gather}

We can easily verify that Null space is a subspace of $\setv$ since it contains the additive identity ($T0 = 0$), is closed under addition ($T(u + v) = Tu + Tv = 0$), and closed under scalar multiplication ($T(\lambda v) = \lambda(Tv) = 0$).\newline

The dimension of the null space (number of basis vectors in the null space) is also denoted by Nullity. Some author may refer to the null space as the \textbf{Kernel} of the linear map.

<!--####################### -->
### Injective or one-to-one
A linear map is injective if it maps distinct elements of $\setv$ to distinct elements of $\setw$
\begin{align}
    T \in \setlm(\setv, \setw) \; \text{is injective if} \; Tv = Tw \Rightarrow v = w
\end{align}
for all $v \in \setv$ and $w \in \setw$.\newline

Injectivity is also equivalent to saying that the null space is a singleton set $\{0 \}$. To prove this, both $Tv = Tw \Rightarrow v = w$ and $v = w \Rightarrow Tv = Tw$ needs to be shown.


<!--####################### -->
### Range
Range of a linear map is the set of elements that are the outputs of the linear map
\begin{align}
    \text{range } T = \{ w \in \setw \text{ such that } Tv = w \text{ for some } v \in \setv\} = \{ Tv \text{ for all } v \in \setv \}
\end{align}
This range $T$ is a subspace of $\setw$.


<!--####################### -->
### Surjective or onto
A linear map is said to be surjective if range $T$ = $\setw$, i.e., every element of $\setw$ is mapped to by an element in $\setv$.

### Fundamental theorem of linear maps
Let $\setv$ is finite dimensional and $T \in \setlm(\setv, \setw)$, then
\begin{align}
    \text{dim } \setv = \text{dim null } T + \text{dim range } T
\end{align}

Suppose $\setv$ and $\setw$ are finite dimensional vector spaces with dim $\setv >$ dim $\setw$, then there is no injective linear map from $\setv$ to $\setw$. This can also be shown using the fundamental theorem of linear maps by proving dim null $T > 0$.

Further, if dim $\setv < $ dim $\setw$, then any linear map from $\setv$ to $\setw$ is not surjective. This can be shown by proving that range $T <$ dim $\setw$ using fundamental theorem of linear maps.

### Change of Bases
The following is the fundamental theorem for change of bases. For two sets of bases $u$ and $v$ of dimensions $n$ and $m$ respectively, the matrix $S_{u \to v}$ defining the transformation from $u$ to $v$ satisfies
\begin{align}
    S_{u \to v} [w]\_{u} &= [w]\_{v}\newline
    S_{u \to v} u_{j} &= s_{1j}v_{1} + s_{2j}v_{2} + \cdots + s_{mj}v_{m}
\end{align}
where $[w]\_{u}$ and $[w]\_{v}$ denote the representation of the same vector $w$ in the two bases, $u_{j}$ is the $j^{th}$ vector of the basis, $v_{2}$ is the second vector of the basis, $s_{ij}$ is the element in the $i^{th}$ row and $j^{th}$ column of the $m \times n$ matrix $S_{u \to v}$.

Then, the columns of $S_{u \to v}$ are the bases vectors $[u]\_{v}$, i.e., the elements of basis $u$ expressed in terms of $v$.

In particular, suppose we want to change from any basis to the standard basis, then $v$ represents the standard basis in the above notation. In this case, $S_{u \to v}$ is the representation of the original basis in terms of the standard basis, which implies that the columns of $S_{u \to v}$ are the original basis vectors themselves.

The inverse of $S_{u \to v}$ will be $S_{v \to u}$, i.e., the matrix for basis change from $v$ to $u$.

Consider the change of basis from $(1,1), (-1,0)$ to $(1,0), (0,1)$. The transformation matrix will be
\begin{align}
    \begin{bmatrix}
        1 &-1\newline
        1 &0
    \end{bmatrix}
\end{align}

The basis change is easier to understand in case of polynomials. Consider the basis change from $\{x+1, x-1, 2x^{2}\}$ (basis $1$) to the standard basis $\{ 1, x, x^{2} \}$ (basis $2$) is
\begin{align}
    S_{1 \to 2} = \begin{bmatrix}
        1 &-1 &0\newline
        1 &1 &0\newline
        0 &0 &2
    \end{bmatrix}
\end{align}

The inverse of this is
\begin{align}
    S_{2 \to 1} = S_{1 \to 2}^{-1} = \begin{bmatrix}
        1/2 &1/2 &0\newline
        -1/2 &1/2 &0\newline
        0 &0 &1/2
    \end{bmatrix}
\end{align}

To transform the polynomial $a + bx + c^{2}$ to basis $1$, we can use the above inverse mapping
\begin{align}
    \begin{bmatrix}
        1/2 &1/2 &0\newline
        -1/2 &1/2 &0\newline
        0 &0 &1/2
    \end{bmatrix} \begin{bmatrix}
        a\newline b\newline c
    \end{bmatrix} =
    \begin{bmatrix}
        (a+b)/2\newline (b-a)/2\newline c/2
    \end{bmatrix}
\end{align}

or, the polynomial can be represented in the new basis as $\frac{a+b}{2} (1+x) + \frac{b-1}{2}(x-1) + \frac{c}{2}(2x^{2})$. When simplified, this is $a + bx + cx^{2}$ itself.

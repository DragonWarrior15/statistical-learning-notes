---
title: "Correct Initialization"
---

# Correct Initialization

Having observed the problems with exploding and shrinking outputs, we stick with the following rules for activations of any layer

1.  The mean value should remain constant across layers (preferably $0$).

2.  The variance should be constant across the layers.

Mathematically this can be descibed as
\begin{align}
    a_{l-1} &= g_{l-1}(z_{l-1})\newline
    z_{l} &= a_{l-1}W_{l} + b_{l}\newline
    a_{l} &= g_{l}(z_{l})\newline
    E[a_{l-1}] &= E[a_{l}]\newline
    Var(a_{l-1}) &= Var(a_{l})\end{align}
We can try several different schemes for weight initialization that follow the above assumptions.

## All weights 0

This will lead to no learning at all as is clear from the formula for gradient calculation in a dense layer
\begin{align}
    \frac{dL}{dW} &= X^{T} \frac{dL}{dY} = 0\end{align}
Hence, it is a bad idea to initialize all weights to $0$. Although, in practice, the biases are all initialized to $0$.

## All weights 1

This causes the problem of symmetry. The gradients of all the weights become same from the formula
\begin{align}
    \frac{dL}{dW} &= X^{T} \frac{dL}{dY} = 0\end{align}
as for every weight in the same row, we have the same gradient. The network will get confused as to which weight to update, causing very poor learning. The same problem exists whenever we set all the weights to same value (even $0$).

## Uniform Distribution

Since we want the mean of the activations to be close to $0$, we will choose a uniform distribution with mean of $0$. We can choose the lower and upper limit of the distribution to be any high or low value. But, this creates a problem of exploding or vanishing gradient. A general rule of thumb is to have
\begin{align}
    w \sim Uniform(-\frac{1}{\sqrt{n}}, \frac{1}{\sqrt{n}})\end{align}
where $n$ is the size of the inputs. This ensures small variance as the number of parameters increase. More concrete bounds for the uniform distribution are discussed in next section.

## Normal Distribution

Initializing weights from standard normal distribution and scaling the inputs in the same range also causes exploding and vanishing gradients. Initializing weights from a normal distribution does seem like a good option (helps maintain the variance across layers), but we need to carefully choose the variance to have stable gradients.


To avoid gradient explosion or shrinkage, the following must hold
\begin{align}
    E[a_{l-1}] &= E[a_{l}] = 0\newline
    Var(a_{l-1}) &= Var(a_{l})\end{align}
where centering around mean helps having stable gradients while training.

## Xavier Initialization (tanh)

Consider the $tanh$ activation function
\begin{align}
     z_{l} &= a_{l-1}W_{l} + b_{l}\newline
     a_{l} &= tanh(z_{l})\end{align}
Our initialization will have initial values close to $0$, making the output of dense layer also close to $0$. In this region, $tanh$ can be approximated by a linear function
\begin{align}
    a_{l} &= tanh(z_{l}) \approx z_{l} \quad \text{for small $z_{l}$}\end{align}

The variance equation becomes
\begin{align}
    Var(z_{l-1}) = Var(a_{l-1}) &= Var(a_{l}) = Var(z_{l})\newline\end{align}
We can compare element wise variances (note that for a single example, $z$ is just a column vector)
\begin{align}
    Var(z_{l, k}) &= Var \bigg( \sum_{j=1}^{n_{l-1}} W_{l, kj} a_{l-1, k} + b_{l, k} \bigg)\end{align}

We make the following assumptions to simplify the analysis

1.  The elements of the weights matrix are independent and identically distributed

2.  The elements of input data/activation are independent and identically distributed

3.  weights and input are independent of each other

We assume the initialization of the bias as also $0$. For any two independent random variables $X$ and $Y$
\begin{align}
    E[XY] &= E[X]E[Y]\newline
    Var(XY) &= E[X^{2}Y^{2}] - E[X]^{2}E[Y]^{2} = E[X^{2}]E[Y^{2}] - E[X]^{2}E[Y]^{2}\newline
    &= (Var(X) + E[X]^{2})(Var(Y) + E[Y]^{2}) - E[X]^{2}E[Y]^{2}\newline
    &= E[X]^{2}Var(Y) + E[Y]^{2}Var(X) + Var(X)Var(Y)\newline
    &= E[X]^{2}Var(Y) + Var(X)E[Y^{2}]
\end{align}
Using this formula
\begin{align}
    Var(z_{l, k}) &= \sum_{j=1}^{n_{l-1}} Var(W_{l, kj} a_{l-1, k})\newline
    &= \sum_{j=1}^{n_{l-1}} E[W_{l, kj}]^{2}Var(a_{l-1, k})) + E[a_{l-1, k}]^{2}Var(W_{l, kj}) + Var(W_{l, kj})Var(a_{l-1, k})
\end{align}

We have $E[w_{l}] = 0$ since we are always initializing from centered distributions (otherwise there can be the problem of exploding/vanishing gradients). Also, $E[a_{l-1}] = 0$ by our assumptions (theoretical analysis is difficult without these assumptions). Simplifying,
\begin{align}
    Var(z_{l, k}) &= \sum_{j=1}^{n_{l-1}} Var(W_{l, kj})Var(a_{l-1, k})\newline
    Var(z_{l}) &= \sum_{j=1}^{n_{l-1}} Var(W_{l})Var(a_{l-1}) = n_{l-1}Var(W_{l})Var(a_{l-1})\end{align}
since all the weights are independent and identically distributed from the same distribution. The same holds true for activations in any layer. By our assumption stated earlier, the variances across layers are same.
\begin{align}
    Var(z_{l}) &= n_{l-1}Var(W_{l})Var(a_{l-1})\newline
    \implies Var(W_{l}) &= \frac{1}{n_{l-1}}\newline
    \implies W_{l} &\sim \mathcal{N} \bigg(0, \frac{1}{n_{l-1}} \bigg)\end{align}

A more common approach is to use both input and current layer sizes in variance calculation
\begin{align}
    W_{l} &\sim \mathcal{N} \bigg(0, \frac{2}{n_{l-1} + n_{l}} \bigg)\end{align}
where we have used harmonic mean of the layer sizes.


In case we were sampling from a uniform distribution, the upper and lower bound of the uniform distribution are slightly different
\begin{align}
    Var(U(-\alpha, \alpha)) &= \frac{(\alpha -(-\alpha))^{2}}{12} = \frac{\alpha^{2}}{3}\newline
    \frac{2}{n_{l-1} + n_{l}} &= \frac{\alpha^{2}}{3}\newline
    \alpha &= \sqrt{\frac{6}{n_{l-1} + n_{l}}}\newline
    \implies W_{l} &\sim U\bigg(-\sqrt{\frac{6}{n_{l-1} + n_{l}}}, \sqrt{\frac{6}{n_{l-1} + n_{l}}}\bigg)\end{align}

## Xavier Initialization (sigmoid)

We use the approximation of sigmoid near $0$ using Taylor Series Approximation
\begin{align}
    \sigma(z) &\approx \frac{1}{2} + z\sigma(z)(1-\sigma(z)) + O(z^{2}) \approx \frac{1}{2} + \frac{1}{4}z\newline
    a_{l-1} &= \frac{1}{1 + e^{-z_{l-1}}} \approx {1}{2} + \frac{1}{4}z_{l-1}\newline
    E[a_{l-1}] &= \frac{1}{2} + \frac{1}{4}E[z_{l-1}] = \frac{1}{2}\newline
    Var(a_{l-1}) &= \frac{1}{16}Var(z_{l-1})\newline
    E[a_{l-1}^{2}] &= Var(a_{l-1}) + E[a_{l-1}]^{2} = Var(a_{l-1}) + \frac{1}{4}\end{align}

Now we calculate $Var(z_{l-1, k})$
\begin{align}
    Var(W_{l} a_{l-1}) &= E[W_{l}]^{2}Var(a_{l-1}) + Var(W_{l})E[a_{l-1}^{2}] \text{from $Var(XY)$}\newline
    &= Var(W_{l})E[a_{l-1}^{2} = Var(W_{l}) \bigg(Var(a_{l-1}) + \frac{1}{4} \bigg)\newline
    Var(z_{l-1}) &= n_{l-1}Var(W_{l})E[a_{l-1}^{2}] = Var(W_{l}) \bigg(Var(a_{l-1}) + \frac{1}{4} \bigg)\newline
    \implies 16 Var(a_{l}) &= n_{l-1} Var(W_{l}) \bigg(Var(a_{l-1}) + \frac{1}{4} \bigg)\end{align}

We input normalized data to our model. Hence, we expect $Var(a) = 1$ at least through the first pass. This assumption is necessary to simplify the above equation
\begin{align}
    Var(W_{l}) &= \frac{64}{5 n_{l-1}} = \frac{12.8}{n_{l-1}}\end{align}
some literature might use $16$ instead of $12.8$


Using both the input and current layer weights
\begin{align}
    Var(W_{l}) &= \frac{2 \times 12.8}{n_{l-1} + n_{l}}\newline
    W_{l} &\sim \mathcal{N} \bigg(0, \frac{25.6}{n_{l-1} + n_{l}} \bigg)\end{align}

If we initialize with a Uniform distribution,
\begin{align}
    Var(U(-\alpha, \alpha)) &= \frac{\alpha^{2}}{3}\newline
    \frac{2 \times 12.8}{n_{l-1} + n_{l}} &= \frac{\alpha^{2}}{3}\newline
    \alpha &= \sqrt{\frac{76.8}{n_{l-1} + n_{l}}}\newline
    W_{l} &\sim U\bigg(-\sqrt{\frac{76.8}{n_{l-1} + n_{l}}}, \sqrt{\frac{76.8}{n_{l-1} + n_{l}}} \bigg)\end{align}

## He Kaiming Initialization (ReLU)

When the activation function is ReLU, the assumption that activations have mean zero will not hold. From $Var(z_{l, k})$
\begin{align}
    Var(z_{l, k}) &= \sum_{j=1}^{n_{l-1}} E[W_{l, kj}]^{2}Var(a_{l-1, k})) + E[a_{l-1, k}]^{2}Var(W_{l, kj}) + Var(W_{l, kj})Var(a_{l-1, k})\newline
    &= \sum_{j=1}^{n_{l-1}} E[a_{l-1, k}]^{2}Var(W_{l, kj}) + Var(W_{l, kj})Var(a_{l-1, k})\newline
    &= \sum_{j=1}^{n_{l-1}} Var(W_{l, kj})(E[a_{l-1, k}]^{2} + Var(a_{l-1, k}))\newline
    &= \sum_{j=1}^{n_{l-1}} Var(W_{l, kj}) E[a_{l-1, k}^{2}]\newline
    &= n_{l-1}Var(W_{l}) E[a_{l-1}^{2}]
\end{align}
since all weights are from the same distribution, and all activations are from same distribution. Let's focus on $E[a_{l-1}^{2}]$
\begin{align}
    E[a_{l-1}^{2}] &= E[\max(0, z_{l-1})^{2}]\newline
     &= E[\max(0, z_{l-1})^{2}|z_{l-1} \leq 0]P(z_{l-1} \leq 0) + E[\max(0, z_{l-1})^{2}|z_{l-1} > 0]P(z_{l-1} > 0)\newline
     &= 0 + E[z_{l-1}^{2}|z_{l-1} > 0]P(z_{l-1} > 0)\end{align}

Since the weights have a symmetic distribution around $0$, we can expect $z$ to also have a symmetric distribution around $0$.
\begin{align}
    P(z_{l-1} > 0) &= P(z_{l-1} \leq 0) = \frac{1}{2}\newline
    E[z_{l-1}^{2}] &= E[z_{l-1}^{2}|z_{l-1} \leq 0]\frac{1}{2} + E[z_{l-1}^{2}|z_{l-1} > 0]\frac{1}{2}\newline
    &= E[z_{l-1}^{2}|z_{l-1} > 0] \quad \text{since $z$ has symmetric distribution}\newline
    E[a_{l-1}^{2}] &= E[z_{l-1}^{2}|z_{l-1} > 0]P(z_{l-1} > 0) = \frac{1}{2}E[z_{l-1}^{2}]\newline
    Var(z_{l-1}) &= E[z_{l-1}^{2}] - E[z_{l-1}]^{2} = E[z_{l-1}^{2}] \quad E[z]=0\newline
    E[a_{l-1}^{2}] &= \frac{1}{2}Var(z_{l-1})\end{align}

Since elements of $W_{l}$ have a normal distribution, with a certain degree of confidence, we can expect $z_{l}$ to also have a normal distribution around mean, but with a different variance
\begin{align}
    \text{Let } \sigma^{2} &= Var(z_{l-1})\newline
    E[a_{l-1}] &= \int_{-\inf}^{\inf} \max(0, z_{l-1})P(z_{l-1}) = \int_{0}^{\inf} z_{l-1}\frac{1}{\sqrt{2 \pi \sigma^{2}}} exp \bigg(-\frac{z_{l-1}^{2}}{2 \sigma^{2}}\bigg) dz\newline
    \text{Let } y &= -\frac{z_{l-1}^{2}}{2 \sigma^{2}}\newline
    E[a_{l-1}] &= \int_{0}^{\inf} -\frac{\sigma}{\sqrt{2\pi}} y dy = \frac{\sigma}{\sqrt{2\pi}}\newline
    Var(a_{l-1}) &= E[a_{l-1}^{2}] - E[a_{l-1}]^{2} = Var(z_{l-1})(\frac{1}{2} - \frac{1}{2\pi})\newline
    \implies \frac{Var(a_{l})}{Var(a_{l-1})} &= \frac{Var(z_{l})}{Var(z_{l-1})}\end{align}

Hence, the second assumption that the variance of activations is same, is equivalent to saying variance of inputs to activation are same.

Note that these derivations will need to be slightly modified in case of other variants of ReLU. Going back to the calculation of variance for current layer
\begin{align}
    Var(z_{l, k}) &= n_{l-1}Var(W_{l}) E[a_{l-1}^{2}] = \frac{n_{l-1}}{2}Var(W_{l})Var(z_{l-1})\newline
    \implies Var(z_{l}) &= \frac{n_{l-1}}{2}Var(W_{l})Var(z_{l-1})\newline
    Var(W_{l}) &= \frac{2}{n_{l-1}}\newline
    \implies W_{l} &\sim \mathcal{N}\bigg(0, \frac{2}{n_{l-1}}\bigg)\end{align}

When using both the layers number of weights
\begin{align}
    W_{l} &\sim \mathcal{N}\bigg(0, \frac{4}{n_{l-1} + n_{l}}\bigg)\end{align}

For uniform distribution
\begin{align}
    W_{l} &\sim U\bigg(\sqrt{-\frac{12}{n_{l-1} + n_{l}}}, \sqrt{\frac{12}{n_{l-1} + n_{l}}} \bigg)\end{align}

For the case of othe ReLU variants like PReLU (Parametric ReLU), we can continue with equation $Var(a_{l-1, k})$. For a parameter $\alpha$,
\begin{align}
    Var(z_{l, k}) &= Var(z_{l}) = n_{l-1}Var(W_{l}) E[a_{l-1}^{2}]\newline
    a_{l-1} &= \max(0, z_{l-1}) + \alpha \times \min(0, z_{l-1})\newline
    E[a_{l-1}^{2}] &= E[(\max(0, z_{l-1}) + \alpha \times \min(0, z_{l-1}))^{2}]\newline
    &= E[z_{l-1}^{2}|z_{l-1} > 0]P(z_{l-1} > 0) + E[\alpha^{2} z_{l-1}^{2}|z_{l-1} \leq 0]P(z_{l-1} \leq 0)\end{align}

By using symmetry argument for $z$ (around 0), $P(z_{l-1} > 0)
= \frac{1}{2}$,
\begin{align}
    E[a_{l-1}^{2}] &= \frac{1}{2}(E[z_{l-1}^{2}]  + \alpha^{2} E[z_{l-1}^{2}])\newline
    &= \frac{1}{2}(1 + \alpha^{2})Var(z_{l-1})\newline
    \implies Var(z_{l, k}) &= \frac{n_{l-1}}{2}(1 + \alpha^{2})Var(W_{l})Var(z_{l-1})\newline
    Var(W_{l}) &= \frac{2}{n_{l-1}(1 + \alpha^{2})} \newline
    W_{l} &\sim \mathcal{N}\bigg(0, \frac{2}{n_{l-1}(1 + \alpha^{2})}\bigg)\end{align}
Setting $\alpha = 0$ is the same as ReLU and $\alpha = 1$ is same as linear activation.


When using both input and current layer weights,
\begin{align}
    W_{l} &\sim \mathcal{N}\bigg(0, \frac{4}{(n_{l-1} + n_{l})(1 + \alpha^{2})}\bigg)\end{align}

In case we were sampling from a uniform distribution, the upper and lower bound of the uniform distribution are slightly different
\begin{align}
    Var(U(-bound, bound)) &= \frac{bound^{2}}{3}\newline
    \frac{4}{(n_{l-1} + n_{l})(1 + \alpha^{2})} &= \frac{bound^{2}}{3}\newline
    bound &= \sqrt{\frac{24}{(n_{l-1} + n_{l})(1+ \alpha^{2})}}\newline
    \implies W_{l} &\sim U\bigg(-\sqrt{\frac{24}{(n_{l-1} + n_{l})(1+ \alpha^{2})}}, \sqrt{\frac{24}{(n_{l-1} + n_{l})(1+ \alpha^{2})}}\bigg)\end{align}

## Summary

The following table summarizes different initializations for different activations

| **Activation Function** | **Normal Distribution** | **Uniform Distribution** |
| ======================= | ======================= | ======================== |
| **tanh** | $\mathcal{N}\bigg(0, \frac{2}{n_{l-1} + n_{l}}\bigg)$ | $U\bigg(-\sqrt{\frac{6}{n_{l-1} + n_{l}}}, \sqrt{\frac{6}{n_{l-1} + n_{l}}}\bigg)$ |
| **sigmoid** | $\mathcal{N} \bigg(0, \frac{25.6}{n_{l-1} + n_{l}} \bigg)$ | $U\bigg(-\sqrt{\frac{76.8}{n_{l-1} + n_{l}}}, \sqrt{\frac{76.8}{n_{l-1} + n_{l}}} \bigg)$ |
| **ReLU** | $\mathcal{N}\bigg(0, \frac{4}{n_{l-1} + n_{l}}\bigg)$ | $U\bigg(-\sqrt{\frac{12}{n_{l-1} + n_{l}}}, \sqrt{\frac{12}{n_{l-1} + n_{l}}} \bigg)$ |
| **PReLU** | $\mathcal{N}\bigg(0, \frac{4}{(n_{l-1} + n_{l})(1 + \alpha^{2})}\bigg)$ | $U\bigg(-\sqrt{\frac{24}{(n_{l-1} + n_{l})(1+ \alpha^{2})}}, \sqrt{\frac{24}{(n_{l-1} + n_{l})(1+ \alpha^{2})}}\bigg)$ |

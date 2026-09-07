# Autoencoders
These models learn representations of data that are useful for one or more subsequent applications. They are also called as auto associative neural networks.

They usually have the same number of outputs as inputs, and also have an intermediate layer/representation $z(x)$, also called the hidden representation. Thus, the full transformation can be written as 

$$x \to z(x) \to y(z)$$

where the first half of the transformation is an encoder, while the latter is a decoder.

The goal is to get $y$ (the output) as close to $x$ (the input) as possible, or minimize the error between the two.

The trivial solution for the above is where the network just learns to copy the input to the output. To force the network to learn non-trivial and interesting representations, we can do one of the below
- Restrict the dimensionality of $z(x)$ to be less than that of $x$ or constraint $z$ to be sparse
- Task the network with reconstruction where the input is corrupted by adding noise, or some parts/features of the input are masked

## Deterministic Autoencoders
### Linear Autoencoders
Consider a network with an input layer of $D$ units, a hidden layer of $M$ ($\lt D$) units, and an output layer of $D$ units. The goal is to reconstruct the input as closely as possible. Since $M \lt D$, it is never possible to perform perfect reconstruction and the MSE across all the dimensions and data examples can be used to learn the network weights.

If the activations are linear, the error will have a global minimum and the hidden layer learns a projection onto the $M$ dimensional subspace spanned by the first $M$ principal components (PCA) of the data. However, it must be noted that these need not be normalized or othogonal.

If activations are non-linear, the minimum error solution is still given by the projection onto the principal components subspace.

There is no advantange in 2-layer networks over deterministic finite time complexity techniques like PCA, SVD etc.

### Deep Autoencoders
We retain our architecture from the previous section, but add more hidden layers.  The output unit is still linear, but the other hidden layers can now be a combination of linear and\or non-linear activations.

This is similar to learning two mapping functions, one from $D \to M$, and another from $M \to D$.

Due to non-linear activations, mappings learnt are now very general, and not restricted to PCA like mappings. However, error function is now not quadratic in the weights, but needs non-linear optimization. This can have difficulty due to local optima as well.

### Sparse Autoencoders
We use L1 regularization to force sparsity, causing an effective reduction in dimensionality

$$
\begin{aligned}
\tilde{E}(w) = E(w) + \lambda\sum_{k=1}^{K}|z_{k}|
\end{aligned}
$$

where $E(w)$ is the unregularized error. Note here the $L_{1}$ regularization is applied on all activations of one of the hidden layers. This is in contrast to the usual application of $L_{1}$ regularization where it is applied on the parameters of the network.

### Denoising Autoencoders
This is one of the approaches to force a model to learn interesting patterns in teh data. We take the input vector $x_{n}$ and corrupt it with noise to give $\tilde{x}_{n}$. Next, we feed this to the autoencoder to get the output $y(\tilde{x}_{n}, w)$ and we try to minimize the error between this output and the noise free input $x_{n}$.

The noise can take two forms
- Take a fraction of inputs ($0 \leq v \leq 1$) and set the value to zero
- Add an independent gaussian noise (zero mean) to all the input features, with scale of the gaussian deterimined relative to the input feature

Through denoising, in applications like images, network learns to understand how nearby pixels are correlated.

### Masked Autoencoders
Language models like BERT learn rich internal representations of natural language through self supervision using randomly masked inputs.

Consider the same idea in images. We mask certain patches and ask the network to predict those patches. The error is calculated only on those patches. Its an encoder-decoder style of architecture where the decoder is discarded post training, and the encoder representations are used in downstream tasks.

Typically for a well trained model, the percentage of masked tokens is close to 75%, compared to just 15% in BERT. This is because of the differences in distributions of data for an image and text.

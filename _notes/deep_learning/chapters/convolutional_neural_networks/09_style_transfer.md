## Style Transfer
The task is to generate a synthetic image $G$ which matches closely in content to an image $C$ and in style to an image $S$.

Define the error as
$$
\begin{aligned}
E(G) = E_{content}(G, C) + E_{style}(G, S)
\end{aligned}
$$

We start with a randomly initialized image $G$ and optimize the above loss function using gradient descent to get $G$.

To match content, the pre activations of the network for both $G$ and $C$ at a particular layer should be similar (since we want both to contain similar features).

$$
\begin{aligned}
E_{content}(G, C) = \sum_{i,j,k}\big[a_{ijk}(G) - a_{ijk}(C)\big]^{2}
\end{aligned}
$$

where $a_{ijk}$ represent the activations. We use a simple sum squared error.

The choice of layer is subjective. Earlier layers matching lower level features, while the later ones measure higher level features.

For matching styles, information across channels in a layer should co-occur. For example, vertical edges of orange color. Different channels in a layer will hold this information.

$$
\begin{aligned}
F_{kk'} = \sum_{i=1}^{I}\sum_{j=1}^{J}a_{ijk}(G)a_{ijk'}(G)
\end{aligned}
$$

This is a correlation score for two channels $k$ and $k'$ and the sum is calculated across the entire image. We calculate this across multiple combinations of channels to get the error

$$
\begin{aligned}
E_{style}(G, S) = \frac{1}{(2IJK)^{2}}\sum_{k=1}^{K}\sum_{k'=1}^{K}\big[ F_{kk'}(G) - F_{kk'}(S) \big]^{2}
\end{aligned}
$$

More pleasing results are obtained by averaging across multiple layers, using a cofficient $\lambda_{l}$ which is adjusted emperically.

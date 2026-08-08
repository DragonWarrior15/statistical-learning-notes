## Adversarial Attacks
We modify the input image by a small value such that the change in the image is imperceptible to the human eye

$$
\begin{aligned}
\vec{x}' = \vec{x} + \epsilon \times sign(\nabla_{x}E(\vec{x},t))
\end{aligned}
$$

where $t$ is the true label. Remember, in gradient descent, we move in the opposite direction of the largest gradient. In this formulation, we take the sign of the gradient and move in that direction, effectively doing a _gradient ascent_ and increasing the _loss_ of the network, or making an input that forces it to make mistake.

$E$ can be the negative log likelihood for a given trained neural network.

This is called the fast gradient sign method. We keep $\epsilon$ small. It may seem that this is due to the network overfitting, but similar perturbations apply to other trained network variants as well.

Similar adversarial results are possible with less flexible linear models as well.

It is also possible to create physical artefacts such that a regular, uncorrupted image with the artefacts gives erroneous predictions when given to a trained neural network.

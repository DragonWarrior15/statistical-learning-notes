## Convolution Operation

Following shows an example of a convolution operation. The $2 \times 2$ matrix is shared across the entire $3 \times 3$ matrix during the operation.

$$
\begin{aligned}
\begin{bmatrix}a & b & c\\d & e & f\\g & h & i\end{bmatrix}
\ast
\begin{bmatrix}j & k \\l & m\end{bmatrix}
=
\begin{bmatrix}aj+bk+dl+em & bj+ck+el+fm\\dj+ek+gl+hm & ej+fk+hl+im\end{bmatrix}
\end{aligned}
$$

### Padding
Convolutions will typically produce an output of smaller size than the input. If we want a similar sized output as input, we can pad the full image before running the convolution.

Typical pad choice is $0$ after subtracting the mean of intensity of each pixel, so that the padding represents the average intensity of the image.

We also typically choose odd values for filter size ($M \times M$) so that there is a central pixel to anchor on.

### Strided Convolutions
Suppose the image is sized $J \times K$ and we use filters of size $M \times M$ such that $M << min(J, K)$. Typically, convolutions work by shifting the filter one pixel at a time. This means the output size is roughly the same as input (and exactly same in case padding is used).

Instead, we can use strides which means the filter is moved in larger steps. If the stride length is $S$, the reduction in output is roughly by a factor of $S$.

### Multidimensional Convolutions
Suppose the input as 3 channels (R, G, B) and is of size $J \times K \times C$. In this case, the convolution filter is of size $M \times M \times C$ and will produce an output with a single channel.

But we can use multiple independent filters similar to how weights of a layer in neural network learn different things. The output will then have channel count $C_{out}$ and the filter we will be using will be of size $M \times M \times C_{out}$.

We can also use filters of size $1 \times 1 \times C_{out}$ to keep similar information in image and reduce the number of channels.

Each convolutional layer is described by a filter of dimensions $M \times M \times C_{in} \times C_{out}$ in which the number of independent weight and bias parameters total to $(M^{2}C_{in} + 1)C_{out}$.

### Pooling
A convolutional layer encodes translational invariance, i.e., if a small patch of pixels representing the receptive field of a hidden unit moves, the output also shifts accordingly.

This is a good property for tasks like object detection. But for tasks like classification, we want the output to be invariant to these translations of input.

However, we do want the network to learn hierarchical structures and the relationships between different features (like eyes, nose and ears for a face) to form higher level composites, and we want invariance to these small structures.

This can be achieved usig pooling applied to the convolution output layer.

#### Max Pooling
A common example of pooling is max pooling which is a fixed operation with no learnable parameters. This has an associated input receptive field and strides. It is useful in reducing the input size as well.

Max pooling preserves the information related to presence of a certain feature in input map and its strength, but discars some of the positional information.

#### Average Pooling
Average pooling also exists where we want to take average information instead of max. These all introduce some degree of local translation invariance.

Pooling is applied independently to each channel of an input, preserving the number of channels in the output.

Variable size inputs can be worked on by pooling to reduce the input size. Because, we would have trained the intermediate layers of the network in a fixed size.

A CNN will have multiple layers of convolution and pooling operations, and in the end we have a fully connected layer to make the final predictions, typical of a classification task. The CNN mainly acts as a feature extracter, and the fully connected network helps learn the relationship between the feature and some output.

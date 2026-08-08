## Vision Transformers
Because of the success of the transformer architecture, it has also been adopted to other modes of communication like images, audio etc.

As long as we can tokenize the input and decode the output, the same architecture is suitable.

### Pixel Sequences
For images, an obvious approach is to conver image into a sequence of pixels. However, the operations have a quadratic growth with sequence size.

### Patches of Image
Hence, we use patches of size P. An image of dimensions $H \times W \times C$ gets converted to a sequence of size $N \times CP^{2}$ where $N = HW/P^{2}$.

Alternatively, we can also use outputs of a model like ResNet. These outputs can be fed directly to the transformer.

ResNet 18 encoder can down sample an image by a factor of 8 in both $H$ and $W$, giving a reduction of over 64 times overall.

Positional encodings for images are typically learnt, and the input size is kept fixed.

Although transformers need to learn image properties from scratch, they achieve higher acuracy as more training data becomes available.

### Image Representations
Image representations using continuous distributions works well with discriminative tasks. However, for generative tasks, dicrete distributions are preferred as continuous ones lead to blurry images.

Furthermore, with images, the number of possible combinations of pixels with 8-bit representations of each channel is very large. For a single pixel, the possibilities are $(2^{8})^{3}$: 8 bits per channel and a total of 3 channels.

To overcome this, we use a codebook of vectors, which is a set of vectors $C$ and we choose the one that is closest to our image patch

$$
\begin{aligned}
x_{n} \to \arg\min_{c_{k} \in C} \lVert x_{n} - c_{k} \rVert^{2}
\end{aligned}
$$

We are essentially replacing $x_{n}$ of dimensions $D$ with the closest $c_{k}$ also of dimension $D$, but $|C| << D$.

Now we follow the similar route from language modelling: at each step, the network predicts the probability distribution over $|C|$ tokens or codebook vectors, and we use this to represent that pixel.

Same concept is applicable to patches of image. We can generate a code book by using $K$ means clustering to find the $K$ candidate to use for the codebook.

However, vector quantization (done here) is a non differentiable operation. In this case, we simply use pass through gradient which essentially means the gradient flows through unchanged.

Note that the patches discussed everywhere above are 2D. We flatten the patch to a 1D array instead so that it becomes a vector, and we use these vectors as inputs.. similar to how embeddings were used in case of natural language.

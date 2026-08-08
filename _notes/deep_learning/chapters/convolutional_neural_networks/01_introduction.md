# Convolutional Neural Networks
CNN (Convolutional Neural Networks) can be viewed as a sparsely connected multilayer network with parameter sharing and are designed to encode invariances and equivariances specific to image data.

Invariance: The output does not alter if you alter the input. Consider scaling or rotating the image. If the image was of a dog, it continues to be of a dog.

Equivariance: The outputs alter by a similar amount as the input, if the input is transformed. Consider moving an image. Suppose the image had a dog, and the dog by 10 pixels horizontally and vertically. The feature map learnt by the CNN will also move by a similar amount.

Transformers are more popular and competitive to CNNs.

## Different computer vision tasks
- Classification (into a fixed set of categories)
- Object Detection
- Image Segmentation
- Caption Generation
- Image Synthesis
- Inpainting (Object Removal)
- Style Transfer
- Depth Prediction
- Scene Reconstruction

## Image Representation
An image is represented by 3 channels (Red, Green and Blue, also popularly called as RGB). Each channel has a color represented typically by 8 bits (there are more rich representations, like 10 bit and 12 bit colors).

Typical Neural network will require a lot of parameters and will ignore local correlations between pixels: Pixels that are close by have different properties compared to far off ones. Closer pixels are more likely to have similar colors and intensities compared to those further away.

This gives rise to the fact that if we generate images by complete random sampling, there is essentially a zero chance of generating a useful image.

## What we want from this architecture
We want to learn four concepts: hierarchy, locality, equivariance and invariance.

Hierarchy exists naturally in images. For instance, face is composed of eyes, eyes of iris and so on. We would want the network to learn smaller local features first and composite them as we go deep into the network to form higher level features.

A CNN filter or kernel is like a matrix operation on a patch of image

$$
\begin{aligned}
ReLU(W^{T}x + W_{o})
\end{aligned}
$$

We want the maximum signal from this. ReLU naturally allows that with $W_{o}$ forming a threshold.

This filter simply answers which parts of the image gives the largest response. This is useful for feature detection. For example, the filter could represent a simple horizontal edge detector. This is a useful feature extractor in initial layers of the network, which can be combined in deeper layers to form higher order features.

## Equivariance
This concept extends to equivariance. We want this feature to do a feature detection in the same way in different parts of the image because it is impractical to have the same feature at all possible locations in the image.

Using the same filter weights across the entire image solves this problem, giving us kind of a sparse network so to say.

## VGG-16 Architecture
Input is a $224 \times 224 \times 3$ image over which we have convolutional layers ($\times 2$) of size $3 \times 3 \times 3 \times 64$ and each convolutional layer has a ReLU activation followed by a max pooling operation to preserve channels and reduce input size.

As we go deeper, we continue to use convolutions of the same size ($3 \times 3$) with ReLU activations and keep doubling the number of channels in the output. More and more channels help capture feature related information and also ensure that as we are compressing the image, the information is not lost too rapidly.

Towards the end, we have 3 fully connected layers, 2 of which have ReLU activation, while the last one has a softmax activation (for classification).

This amounts to around ~138 million indepdendently learnable parameters, out of which ~103 million are in the first fully connected layer. FCN has the highest parameters with lesser receptive fields, while the initial convolutions have the highest receptive field but the lowest number of parameters.

Earlier architectures had fewer convolutional layers and bigger filters. However, a similar effect can be achieved by using small filters and more layers. The advantage of latter is that we have fewer parameters.

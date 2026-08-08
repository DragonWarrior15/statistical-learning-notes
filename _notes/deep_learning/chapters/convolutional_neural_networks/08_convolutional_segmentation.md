## Convolutional Segmentation
Consider a very basic approach: Run a CNN centered at each pixel to give a softmax output for each pixel. then we can assign a single class to each pixel based on the highest probability. We can assign colors to each class, and color the image to represent regions.

This is a very slow process. A faster appraoch is to use filters of size $1 \times 1$ and use multiple such layers to increase computation speed. Output is of same size as the input image, but the number of channels equals the number of classes. Training such a network is difficult as it would need multiple layers to understand the complex internal representations, given the fact that such small filters will have very narrow receptive fields, defeating the entire purpose of using filters in the first place. The deeper network would need to work harder to understand these spatial relationships, which larger filter would automatically provide.

### Up-Sampling
A typical CNN tries to downsample an imapge while increasing the number of channels. This allows it to capture higher order fetures while capturing more information in the channels. Thisi process keeps the number of parameters in the network manageable.

We can do the same process in reverse to obtain an output of the same dimensions as the input. This is like a compress-decompress architecture.

Some nuances to consider here. For un-pooling, its easy to do for average pooling. We simply put the same value in all the boxes when upsamping. For max-pooling, there are two options
- put the value at the left top, and fill remaining values with zeros
- when downsampling, note the position of the largest element; have a corresponding equivalent upsampling step, and put the value at the same recorded place; other positions have the value 0

### U-net architecture
It is similar to up-sampling with a difference. Core concept is that during each upsampling stage, the upsampled decoder feature map is concatenated with the feature map from the corresponding encoder stage. This is kind of like a skip connection.

This is done so that spatial information from the image is retained. This retaining of spatial information is useful in cases like image segmentation, but not that important in image classification problems.

Note that here we concatenate the input feature map during decoder stage along the channel dimensions. We deliberately dont add the input and output feature maps together to retain the maximum information possible. This skip connection is the main difference from the up-sampling approach.

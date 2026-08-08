## Layer Visualizations
### Mammallian Visual Cortex
Mammallian visual cortex has simple cells which respond to orientation of edges. This can be modelled by Gabor filters.

There are more and more complex cells in the visual cortex that respond to even higher levels of abstraction and are invariant to shifting of these higher level features.

### Visualizing First Layer
The first layer of CNN is easy to visualize since it can be directly studied by which patches of image are giving higher activation in general.

The weights of the first layer are similar to Gabor filters, detecting edges in different orientations. But this does not mean we have successfully mimicked the mammallian visual cortex. But rather, the network has learned a statistical property of the image, namely the edges.

### Visualizing Deeper Layers
To visualize deeper layers, we can tkae large sets of images and for each filter, we can record which types/parts of images are causing high activation/response.

One study with a 5 layered CNN followed by 2 FCN layers on the ImageNet dataset showed layer 2 onwards we start to learn more and more complex shapes/textures. Layer 3 has stuff like wheels and finally we have entire objects being recognized.

### Saliency Maps
These are computed using gradient and softmax activations, and are used to understand which parts of an image are most useful in giving the final class label. They can be visualized as heatmaps on the input image, corresponding to the region giving highest response for the output label.

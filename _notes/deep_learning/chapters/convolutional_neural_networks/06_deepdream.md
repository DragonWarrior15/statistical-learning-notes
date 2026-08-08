## Deepdream
The concept is to identify which nodees in a particular layer of the network respond strongly to a particular image, and then modify the image to amplify those responses.

Suppose we know the pre activation to that node (obtained by forward pass of the image); we assume that to be the target variable and run back propagation from there.

Then, we modify the input image by a small amount, taking a step in the direction of gradient descent (to boost optimization of particular activations). Note, there is no network training here, only modifying the input image accordingly.

This technique has ben used for dreamy artwork generation in practice.

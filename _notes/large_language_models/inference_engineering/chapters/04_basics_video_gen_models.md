## Video Generation Models
Architecture is very similar to image generaiton models. These have roughly 3 to 5 times more parameters than image generation counterparts, and encode 10 to 100 times more information in the latent space.

Naive approach is to generate video frame by frame. The issue with this approach is that the error is compounding frame by frame, and video goes off rails quickly.

Modern models hold the entire video in latent space and modify it on each denoising step, where each frame attends to every other frame and is updated in forward pass. The latent space encodes the full video in dimension $X \times Y \times T$ where $T$ is time (or number of frames to be more precise).

Video models typically run on a batch of size 1, and a single request is typically served over a node of multiple GPUs. They also take roughly 50 denoising steps for video generation.

Self forcing is a technique that combines a global view of quality with an iterative approach to generation.

The bottleneck remains to be attention and it is the most expensive component.

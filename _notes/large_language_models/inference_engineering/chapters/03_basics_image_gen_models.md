## Image Generation Inference Mechanics
Image generation typically consists of a pipeline of models instead of using a single model. The task here is to generate an image based on a text input.
- Text Encoder: Converts the input sequence of tokens into instructions that the image generation model can understand
- Denoising Model: Heart of the pipeline and is responsible for iterating from noise to an image based on the prompt
- Variational Auto Encoder (VAE): Converts the denoising model output from the latent space to the image/pixel space

Beyond the base model, there are additional capabilities to this pipeline
- LoRAs: Lightweight fine tunes to change the style and enhance quality
- ControlNets: Outlines and edges to steer the output images to match broad shapes and colors

### Latent Space
Entire image generation pipeline is in the latent space. A typical image maybe $1024 \times 1024$ pixels, which is over a million pixels. Denoising model needs to attend to the entire image in parallel, which is infeasible in this case.

Latent space is a low dimensional representation of an image. It might be just $128 \times 128$, which is 1% of the pixel space and easier to work with.

Latent soace is initialized with random noise initially. In each step, this entire space is updated. For good image models, around 30-50 steps are sufficient to create high quality image.

Within each step, two forward passes are done, one direct and one conditional on the prompt. These generations are then combined based on a guidance scale. Thus a 50 step generation actually involves 100 forward passes.

### Inference Arguments
The below inference arguments are used to control image generation
- Prompt: What the image should look like
- Negative Prompt: Styles or objects the image should not contain
- Steps: The number of steps, a tradeoff between quality and latency; its used for the denoising model
- Guidance Scale: Controls the balance between creativity and prompt adherence, and is an integer value typically 4
- Image Size: Usually a selection from a fixed menu of resolutions and aspect ratios

### Architecture
Model architecture is based on diffusion transfomers. Instead of processing a sequence of embeddint representations of discrete tokens, these process the image data. They look at the image in patches.

While training text to image models, input image is fetch in overlapping patches of size $2 \times 2$ or $4 \times 4$, which are then embedded into latent space. Inference works in the opposite direction, with latent space transformed back into the pixels once image generation is finalized.

The architecture is built of a pipeline of text encoder, denoiser and VAE.

### SDXL
Stable diffusion XL (SDXL) is an old architecture that is still relevant today. It has two diffusion models for the denoising step, a base and a refiner model. The base model goes from noise to unrefined latent space, while the refiner refines this latent representation to ensure prompt adherence and adds details.

Modern models outperform SDXL with more capable models at each step of the pipeline, upto 5x in number of parameters.

Research to go from diffusion models to LLMs is underway. While diffusion models produce outputs of a typically fixed size, LLMs can generate sequences of variable sizes due to their autoregressive nature.

### Few Step Image Generation Models
These models use 8 or fewer steps in the denoising model, and are out of the box around 80%-90% faster. There are two primary methods for creating these models
- Latent Consistency: Train the model to predict the target latent image directly, and repeat the prediction 2-4 times for enhancing the quality
- Distillation: Use adversarial and/or progressive distillation to train a small model to emulate a larger one in fewer inference steps

Distillation is more common. Members of open source community will create distillation versions in addition to quality and style oriented LoRAs.

These models are useful for real time applications and latency sensitive use cases.

## Motivation
Some definitions
- Closed models: Proprietary models whose weights are not released to the public
- Open models: Weights are available publicly, usually under the MIT license (although some may restrict commercial usage)

Over time, the gap between closed and open models has drastically reduced. Meaning, companies can now own their deployments of open models, offering a plethora of advantages
- Latency: Closed model APIs are optimized for throughput, while open models can be optimized for real time applications
- Availability: Closed models, if stuck at two nines of availability, mean that dedicated open model deployments can lead to four nines of deployment or better
- Cost: Open models are usually upto 80% less expensive than closed models at scale

There are two parts to a generative AI lifecycle
- Training: Process of learning model weights from data
- Inference: Serving generative AI models in production

Inference of classic ML models is straightforward: lightweight CPUs do the job.

For generative AI models, GPU clusters are needed to efficiently serve the models.

Below are a couple of runtime model performance improvement techniques
- Batching: Run multiple requests in parallel, weaving them together on a token by token basis to increase throughput
- Caching: Re-use the KV cache, the cached results of attention algorithm, between requests that share prefixes
- Quantization: Lower the precision of select pieces of model to access more compute and reduce memory burden
- Speculation: Generate and Validate draft tokens to produce more than one token per forward pass during decode
- Parallelism: Efficiently leverage more than one GPU to accelerate large models without introducing new bottlenecks
- Disaggregation: Separate the two phases of inference, prefill and decode, onto independently scaling workers

One needs to look at how to scale inference from a single GPU to multiple GPUs. When that is not sufficient (due to high volume of requests), we move on to getting multi region deployments. Here, we need to ensure optimal usage across all clusters and regions.

Examples of inference engines are vLLM, SGLang, TensorRT-LLM. The software stack typically involves PyTorch and CUDA. Lot of low level optimizations are also used to improve inference efficiency and throughput.

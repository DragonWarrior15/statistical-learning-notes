## Inference Bottlenecks
There are two aspects of GPU hardware
- Compute: The number of floating point operations per second that a GPU can achieve (FLOPS)
- Memory Bandwidth: The number of bytes a GPU can move per second

We want optimization in the sense of balancing between the two, and one of those should not be sitting idle at any point of time.

In most cases, inference systems have below two bottlenecks
- LLM Prefill: KV Cache construction is compute bound
- LLM Decode: Token generation is memory bound
- Image and Video Generation are compute bound

As an example, consider batching of multiple requests during decode makes it less memory bound because processing of a batch of requests uses more compute for the same amount of memory traffic.

### Ops:Bytes Ratio
GPU speed is measured in ops/second. Memory bandwidth is measured in gb or tb/second.

As an example, consider the H100 GPU in FP16 operations. It gives 989 TeraFLOPS at 3.35 TB/s of memory bandwidth. This makes an ops:bytes ratio of roughly 295. This means that at inference, the system needs to work at roughly 295 floating point ops of every byte of memory consumed.

Arithmetic intensity is defined as work/memory traffic.

Compute Bound: Arithmetic intensity > ops:byte ratio
Memory Bound: Arithmetic intensity < ops:byte ratio

### LLM Inference Bottlenecks
- Prefill Phase: TTFT is measured; Compute bound as the entire sequence is processed in parallel
    - Loads the entire model weights at a go, followed by a series of large matrix multiplications
    - Number of calculations is higher than a single read operation, creating high arithmetic intensity
- Decode Phase: TPS is measured; Memory bound as generates one token at a time
    - This step loads weights for every token (because it is difficult to keep all the weights in memory), however matrix multiplication operations are much less expensive (matrix operations are inefficient as we are doing one token at a time)
    - Operations < Memory bandwidth, hence arithmetic intensity is low

Existence of bottleneck can be proven by comparing the arithmetic intensity of the most expensive operation to the ops:byte ratio of hardware

In both prefill and decode, attention is the most expensive operation. Arithmetic intensity of attention is dependen on both the model architecture and the implementation as well.

### Optimizing Attention
Attention is quadratic in length of input sequence. With KV cache it becomes kind of linear, but that too grows pretty quickly with sequence length.

There are two strategies for optimization here
- Implementation Improvements: Write better high performance kernels that use memory and compute efficiently
- New Algorithms: Create algorithms that scale in better than quadratic time with minimal quality loss

Flash Attention is a popular implementation
- Basic algorithm can be implemented in a handful of lines of code
- Much bigger codes are needed in practice as the implementation is very specific to the type of hardwares and will vary between different GPUs
- Works by eliminating excess reads and writes from memory and laying out attention algorithm to precisely fit GPU capability
- Especially useful for compute bound operations like prefill

Paged Attention
- KV Cache grows quickly, filling the GPU memory
- Partitions KV cache in blocks (pages) that can be accessed via a lookup table
- Means KV cache is stored across GPU in fragmented memory rather than contiguous blocks of memory

Both the above are still quadratic implementations and other optimizations try to improve underlying time and space complexities.
- Sliding Window Attention: Computes attention for a sliding window of previous $w$ tokens, turning attention from $O(N^{2})$ to $O(Nw)$, where $w$ is often 8k to 32k tokens
- Gated Attention: Various types of layers are introduced in training to allow for approximating attention for certain chunks of context in linear time, with respect to chunk length
- Linear Attention: Replaces softmax equation with a linear time algo that approximates attention
    - Standard attention is $O(N^{2})$ beacuse of the order of matrix operation $Softmax(QK^{T})V$, $Q$ and $K$ are multiplied first, creating a massive $N \times N$ matrix
    - Instead, replace Softmax with a feature map/kernel function $\phi$ and the overall operation becomes $(\phi(K)\phi(Q^{T}))V$
    - Because now we are dealing directly with multiplication of three matrices, associative property applies and we can swith the order of multiplication to $\phi(K)(\phi(Q^{T})V)$
    - $\phi(Q^{T})V$ produces a $d \times d$ matrix now, isolating $N$
    - We are essentially compressing attention into this small $d \times d$ matrix instead of the original $N \times N$ matrix
    - On every token generation, just this small matrix gets updated in place, no need to maintain an every growing KV Cache
    - However, Softmax is practically a better function as it gives better weights to important tokens, linear approximations often flatten things out
- Compressed Attention: Periodically compress context from earlier in the sequence; attention considers both the compressed context and uncompressed recent tokens
- Multilatent Attention: Approximates attention in a latent space

Intuitively, it makes sense that tokens near each other in the sequence affect each other more than tokens from much earlier.

There are also other architectures like Mamba, where selective state space model that replaces self attention with a recurrent state update is used. This achieves linear scaling on sequence length. The intuition for this lies in the Linear Attention discussed earlier.
A hybrid model mixes Mamba style blocks with transformer blocks.

### Other categories of optimization
Core principle of inference engineering is that the more constraints that can be introduced in the system, better performance can be achieved.

More traffic means that more preformance optimization is possible (while keeping unit economics reasonable). Higher model parallelism across GPUs, KV aware routing, dynamic disaggregation only make sense when we have a large number of GPUs, often multiple nodes, serving the same model with vertical and horizontal replication.

Five key cateogories: quantization, speculation, caching, parallelism, disaggregation.

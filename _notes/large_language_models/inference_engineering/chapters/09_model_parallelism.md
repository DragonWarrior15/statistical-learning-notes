## Model Parallelism
As models are becoming larger and larger, we need bigger GPUs as well to fit th emodel into a single GPU. Since a single GPU cannot load large frontier model, we often need a node of multiple GPUs to handle this task for us.

In FP8 precision, loading a billion parameters model takes roughly a GigaByte of VRAM. We also need to consider the spave for KV cache, which can be approximated to take about 80% or more of remaining VRAM after weights.

General formula that we can use here

$
\text{VRAM required} = (\text{bits precision}/8) \times \text{parameters} \times \text{KV cache allcation}
$

The KV cache allocation is roughly taken as $1.8$.

For a DeepSeek V3 model with say 671 billion parameters, using the above equation, a full node of 8 B200 GPUs is needed (each GPU carries around 180GBs of memory).

Even for mid sized models, its important to allocate higher GPU memory so that ample space is available for KV cache, which unlocks better user facing latency.

For efficient inference scaling across multiple GPUs, we also need to consider the GPU communication overhead. This overhead may or may not play a role depending on the model size, type of parallelism and sequence lengths. There are three primary forms of parallelism as tabulated below

| Sr No | Name | Mechanism | GPU Role | When to Use |
| --- | --- | --- | --- | --- |
| 1 | Pipeline Parallelism | Splits layers of models across GPUs | Each GPU handles a stage of forward and backward pass | - Not recommended due to poor latency and utilization by the step by step pipeline<br>Only used for multi-node inference |
| 2 | Tensor Parallelism | Splits the tensors within each layer across multiple GPUS | | Needs synchronization across GPUS<br>Not suitable for multi-node inferencing<br>Generally best for low latency model if within a single node |
| 3 | Expert Parallelism | Shards the entire experts (MoE models) across different GPUs | Each expert lives within a single GPU, making expert inference fast | Requires routing between GPUs to reach multiple experts<br>Improves throughput for MoE LLMs |

GPUs within a node often communicate via NVLink/NVSwitch while nodes communicate using InfiniBand. Both offer high bandwidth, but are often only a fraction of VRAM speed. For dense models, we use Tensor Parallelism within each node while Pipeline Parallelism across nodes.
 
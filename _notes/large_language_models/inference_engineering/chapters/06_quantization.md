## Quantization
Quantization
- Improves latency (both TTFT and TPS)
- Increases system throughput
- Opens headroom for other optimizations like disaggregation, speculation and prefix caching to be more effective
- But when it goes wrong, it can materially affect the model's output quality

Models are usually trained in weights represented in FP16 (floating point 16 bit precision) format. More recently, training through 4-bit, 8-bit and similar models is also becoming popular.

Post training quantization works by changing the precision post training to lower the precision format. Suppose we cut the precision in half, this leads to
- Prefill: Compute bound prefill runs with twice the FLOPS
- Decode: Memory bound decode loads half as much data, meaning double the bandwidth

Working with quantized data does introduce overhead, so its not linearly twice as fast to go from 16 bits to 8 bits. In general, quantization down a single level of precision generally offers 30% to 50% better performance for LLMs.

Quantization does introduce the risk of precision error. Consider the value of $\pi^{2}$. The values are very different when we consider $\pi$ to be 3.14 vs just 3. most work in quantization focuses on preventing precision errors and minimizing the impact on final output.

Different number formats
- **FP16**: Floating Point 16-bit
- **MXFP4**: Mixed Precision Floating Point 4
- **INT8**: 8-bit Integer
- **FP4**: Floating point 4-bit

### Floating Point Numbers
Floating point numbers have three properties
- **Sign**: Single bit to represent whether the number is positive or negative
- **Exponent**: Set of bits that taken together, represent an exponent factor
- **Mantissa**: A set of bits that taken together, represent the base value multiplied by 2 to the exponent

Larger the floating point representation, more the range and more the precision.

### Where can Quantization be applied
Quantization can be applied at
- **Tensor Level**: Calculate a single scale factor for the entire QKV vector
- **Channel Level**: Calculate a different scale factor for each feature vector within the tensor
- **Block Level**: Within each feature vector, devide the vector into blocks of N values, and calculate a scale factor for each block

### Scale Factor
The scaling factor helps converting the floating point numbers to an equivalent lower precision representation.

Standard quantization formula
$$
q = \left\lfloor{\frac{x}{S}}\right\rfloor + Z
$$
where
- $q$ is the quantized value
- $x$ is the original floating point value
- $S$ is the scaling factor
- $Z$ is the zero point (integer representing the real world 0)

and the inverse operation will be
$$
x \approx S \times(q - Z)
$$

There are two ways to calculate the Scale Factor
- **Symmetric Quantization** (where $Z = 0$)
    - $$
      S = \frac{\max(|{x_{min}|}, |{x_{max}|})}{q_{max}}
      $$
    - Faster as math is simpler, no need to adjust for zero offset
    - Primarily used when data is centered around 0, the weights
    - Lower accuracy on skewed data
- **Asymmetric Quantization** (where $Z \ne 0$)
    - $$
      \begin{aligned}
      S &= \frac{x_{max} - x_{min}}{q_{max} - q_{min}}\\\\
      Z &= \left\lfloor\frac{-x_{min}}{S}\right\rfloor + q_{min}
      \end{aligned}
      $$
    - Slightly more complex as we need to adjust with $Z$, making it slower
    - Primarily useful when the data is skewed, activations (ReLU for instance)
    - Higher accuracy on skewed data

Note that the format MXFP8, supported by Blackwell architecture, is also called a microscaling format. It computes blockwise scale factor on every 32 parameters, reducing the impact of these number formats' lower dynamic range.

Dynamic Quantization: Certain layers or other components of the model are left in the original precision, while the others are quantized to integers with as little as one bit of precision. These usually represent average precision when reporting (example 1.58 bit quantization).

On production, stick to floating point precision, as they have high dynamic range and represent outliers better, especially for operations like softmax. Integer formats are not suitable for quality sensitive work due to their lack of dynamic range.

FP8 provide the sweet spot between quality and performance. It also provides the most flexibility when quantizing KV cache.

### Approaches
The more parameters a model has, the less sensitive it is to quantization as each individual parameter is less important. It is still important to quantize carefully.

- **Quantization Aware Training**: Training the weights and scale factors together to ensure that the final converged weights are accurate at any given position
- **Post Training Quantization**: Converting finished model weights to a new precision by computing the scale factors and preserving accuracy via calibration

We can use the NVIDIA TensorRT Model Optimizer (Model Opt) for post quantization training.

### What to Quantize ?
After picking a precision to quantize to, two decisions have to be made before post training quantization
- What parts of the mdoel need to be quantized: weights, activation, cache, attention ?
- What nomber format offers the appropriate dynamic range and granularity ?

Different components have different sensitivity to quantization. Reducing the precision of more sensitive components has a higher risk of quality degradation. See the below in the order of least to most sensitivity
- Weights: Specifically the linear layers are least sensitive to quantization, thanks to the size of the layer; however, input and output maybe left in original precision as they are more sensitive
- Activations: Intermediate outputs of activation functions are only somewhat sensitive to quantization; activation functions are rarely quantized though as they are such a tiny fraction of teh model's weights
- KV Cache: Cached values from attention calculation are moderately sensitive to quantization; KV cache fo each token is used by every subsequent token, hence quantization induced errors can compound in a sequence
- Attention: Attention layers of a model are highly sensitive to quantization, especially equations like softmax

Here, KV cache refers to the operations that have already been completed and stored. By quantization, we are only saving the memory footprint of the already calculated numbers. On the contrary, attention refers to active calculations where precision is important. Softmax is part of attention and is sensitive to changes in the input.

KV cache quantization gives additional boost to techniques like prefix caching and disaggregation. KV cache is a valuable resource. Quantizing it allows storing more of it in memory and reading it more quickly.

All but the most aggresive quantization schemes run softmax in the original precision.

A moderate approach to low precision inference uses a format like FP8 with high dynamic range if possible, a microscaling format like MXFP8 to carefully quantizae select layers, activations and often KV cache values. Even with thise high dynamic range formats, components of attention layer are rarely quantized.

### Measuring Quality Impact
Test the output quality vs original precision outputs
- **Perplexity**: Calculate perplexity score for quantized model vs original
- **Intelligence Benchmarks**: Run standard intelligence benchmarks like MMLU or SWE-bench and compare original scores
- **Custom Evals**: Run a product specific evaluation suite on quantized models and compare with the original one

The idea is to look for difference in scores that is indistinguishable from noise. Then the quantization is acceptable.

Simplest check on quality is perplexity. Give the quantized model the expected output token sequence, and calculate the likelihood of the model predicting those tokens. Higher perplexity means the model is "_surprised_" by the sequence which is not desirable. We want only a small increase in perplexity.

Quantization is a scale, not a binray decision. Every configuration of what to quantize and what not to, produces entirely different scores. For highly sensitive domains, it is preferable to not perform quantization, but rather look at other optimization techniques.

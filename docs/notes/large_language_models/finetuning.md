# Pretraining of LLMs
Typically, models like GPT have been trained on a large text corpus scraped off of the internet for the task of next token/word prediction. The model builds its own knowledge of the world and language based on this.

ChatGPT is a finetuned version of this model which has been trained on specific question/answer or task style prompts data.

Finetuning can update all model weights (full finetuning) or only a small set of parameters, as in parameter-efficient finetuning.

# Benefits of finetuning

* Can improve the consistency of the models on the specific tasks/instructions
* Reduce hallucinations, since the model is now more focused on the new data
* Gain knowledge of the concepts specific to the new data, this way prompts can avoid giving specific instructions related to the nuances of the data

## Datasets

* `Alpaca` dataset ([link](https://huggingface.co/datasets/tatsu-lab/alpaca)) is available for instruction training of pretrained language models. This can help tune the model for following instructions better.

## Data Preparation

* Useful to have **high quality**, **diverse** data that is **real** and not LLM generated. High quality data will ensure that fine tuning is effective, since the LLMs have already been trained on a giant corpus of internet text and already have knowledge of language and its structure.
* Steps
    * Collect instruction response pairs, following the guidelines above
    * Concatenate the pairs, adding a prompt template as well if required
    * Tokenize, and pad the data is needed to fit the context length
    * Split into training, validation and test sets. Use validation to choose a checkpoint and keep the test set for the final evaluation.

For supervised chat finetuning, each training example can be a conversation with system, user and assistant messages. The assistant message contains the target response during training; at inference time, supply only the system and user messages and let the model generate the response. Use the model's chat template to format the conversation.

In JSONL format, each line is a separate JSON object representing one training example. For example:

```jsonl
{"messages": [{"role": "system", "content": "Classify the request. Return only the label."}, {"role": "user", "content": "Where is my delivery?"}, {"role": "assistant", "content": "delivery_status"}]}
{"messages": [{"role": "system", "content": "Classify the request. Return only the label."}, {"role": "user", "content": "How do I return an item?"}, {"role": "assistant", "content": "return_item"}]}
```

The system and user messages provide context, while the assistant message supplies the expected output. Each line must be a complete JSON object.

## Finetuning steps

* Give the data to model, the task still remains to do the next token prediction
* Loss is calculated based on the generated and the actual token
* We backpropagate the loss through the model and update the weights, with the help of an optimizer
    * Parameters of interest for the optimizer are learning rate, learning rate scheduler etc

There are two common choices for which tokens contribute to the loss:

* **Full-sequence loss**: Train on both the prompt and the expected response tokens. This can be useful for continued language model training on text whose style or domain the model should learn. In chat data, it also trains the model to predict the prompt itself.
* **Response-only loss**: Mask the prompt tokens in the loss and train on the expected assistant response. The prompt still provides context. This is useful for instruction following and classification, where the goal is to learn the response to a given input.

Track training and validation loss and save checkpoints throughout training; compare checkpoints on the validation set before evaluating the selected one on the held-out test set.

## Evaluation

* Human expert evaluation is often the best
* A good high quality, accurate, generalized data is essential, one that has not been seen in the training data.
* Error analysis
    * Understand base model behaviour before finetuning
    * Categorize the errors, and iterate on data to fix these in the data space itself

* Some error categories
    * Misspellings
    * Output is too long
    * Repetitive

* Evaluation metrics
    * Rouge scores (unigram, bigram, n-gram)
    * Semantic similarity scores (via embedding models)
    * LLM as a judge (libraries like Ragas support these metrics)

* Tips
    * More tokens out is usually a more complex task (like writing code, chat) compared to less tokens out (like reading, agents)
    * More generic the the task or combination of tasks require a bigger model
    * Combination of multiple tasks is harder than 1 task

# Finetuning Other Methods
## PEFT
Parameter-efficient fine tuning trains a small number of additional parameters while keeping the base model weights frozen. This reduces the trainable parameter count and allows adapters to be stored separately from the base model.

## LoRA
Low-Rank Adaptation (LoRA) represents an update to a weight matrix using two smaller trainable matrices. The base weight stays frozen and the adapter learns the task-specific update. Rank controls the size of the low-rank update; target modules determine where adapters are added.

For example, to finetune with MLX, prepare chat examples as JSONL, add LoRA adapters to selected projections such as query and value, and train with an optimizer such as AdamW. Set `mask_prompt` to use response-only loss. Load a saved adapter checkpoint with the same base model to evaluate it.

For a classification task, compare the base and adapted models using the same prompt and held-out examples. Alongside accuracy and per-class or macro metrics, track the rate of outputs that are not valid labels. Invalid outputs count as incorrect, and separating this rate helps distinguish output-format improvements from improvements in choosing the right label. Save the model, prompt, adapter, split and predictions for each run so results can be reproduced and errors inspected.

# References

* [Finetuning LLMs, Deeplearning.ai](https://learn.deeplearning.ai/courses/finetuning-large-language-models/lesson/1/introduction)

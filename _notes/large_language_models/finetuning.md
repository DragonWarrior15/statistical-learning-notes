---
title: "Finetuning"
---

# Pretraining of LLMs
Typically, models like GPT have been trained on a large text corpus scraped off of the internet for the task of next token/word prediction. The model builds its own knowledge of the world and language based on this.

ChatGPT is a finetuned version of this model which has been trained on specific question/answer or task style prompts data.

Finetuning of LLMs is slightly different in the sense that all the model weights are updated rather than just same final layers.

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
    * Split into train/test sets for evaluation

## Finetuning steps
* Give the data to model, the task still remains to do the next token prediction
* Loss is calculated based on the generated and the actual token
* We backpropagate the loss through the model and update the weights, with the help of an optimizer
    * Parameters of interest for the optimizer are learning rate, learning rate scheduler etc

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
Parameter efficient fine tuning. TBA.

## LoRA
Low-Rank adaptation of LLMs.

# References
* [Finetuning LLMs, Deeplearning.ai](https://learn.deeplearning.ai/courses/finetuning-large-language-models/lesson/1/introduction)

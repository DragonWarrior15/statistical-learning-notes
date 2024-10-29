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

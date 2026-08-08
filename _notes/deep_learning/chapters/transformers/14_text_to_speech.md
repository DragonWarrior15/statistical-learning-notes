## Text to Speech
This uses the approach from VallE.

For training, we have tokens from text, whose target is the corresponding token from mel diagram or any other representation, and we also give other speech samples as input. During inference, to match a speaker, we pass the sample speech or text audio along with text, to speak and generate output audio tokens. We then decode the to generate audio.

Because of multimodal nature of transformers, we are simply extending input sequence to contain text and audio.

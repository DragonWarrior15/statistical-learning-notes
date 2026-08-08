## Working with audio data
Audio data is typically stored as the amplitude of air pressure at regular time intervals.
An equivalent representation is mel diagram, where columns represent time (left to right) and rows represent frequencies (which have been chosen subjectively for better analysis of percepted difference between frequencies).

Before transformers, mel diagrams were digested as images into a CNN for classification tasks. But these could not capture long dependencies.

Now we can use transformers on the same images to get much better perfornace. Encoder style architectures can even be used to generate audio.

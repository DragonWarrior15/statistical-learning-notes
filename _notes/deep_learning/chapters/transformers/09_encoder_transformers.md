## Encoder Transformers
- BERT (Bi directional encoding transformer) is a classic example
- Typically the entire sequence is taken as input and produces a fixed size vector as output; a vector of class probabilities for instance
- We train using a large corpus, and then finetune for the task at hand

### Training
- Unlike Decoder Transformers, there is no causal constraint here
- We all all the tokens to attend to each other, which gives this the name of bidirectional attention
- We typically modify the sequence as below for training
\<class> I \<mask> across the river to \<mask> ...
- Every sequence begins with the \<class> token; its use is explained later
- We ask the model to predict \<mask> positions outputs correctly
    - This is typically 15% of the tokens and is randomly selected
    - Out of the 15%, 80% is the \<mask> token, 10% is a random word, and the remaining 10% is the original word itself
    - This is done because fine tuning data will typically not have any \<mask> and we will instead be using full sequences
    - The target is still the correct token at the position
    - The random word helps model understand that sometimes words can be misplaced and it should refer to the global context
- Once trained, we finetune this by adding a MLP on top of outputs
    - The input dimensions to this MLP are $D \times 1$ and the output dimension is $C \times 1$ where $C$ is the number of classes over which we want to make the prediction
    - For classification, we just use the output of the \<class> token and discard the rest
    - For tasks like entity recognition, where the output at each step has to be classified, we share the same MLP weights across the entire sequence
- We usually learn all the parameters including the new MLP layer, however lot of tasks freeze the transformer layers and only calculate the MLP weights as transformer is supposed to have learnt the language representation which we want to retain
- One can also feed the transformer outputs to another sophisticated deep learning model, say for text to image synthesis

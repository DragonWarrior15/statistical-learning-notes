## Word Embeddings
These are numerical representations of words so that they can be ingested by any moddl like transformer.

### One Hot Encoding
The simplest word embeddings are simply one hot encodings. The dimension equals the size of a pre defined dictionary. The vector then consists of 1 at the position of the word in the dictionary and 0s at other places.

The problem is, this is a very high dimensionality vector, and does not even capture any semantic relationships between words.

Alternate encodings like character level one hot encoding vectors exist, but typically they capture even less meaning than words.

### Word2Vec
Suppose the dictionary size is $K$. The idea is to build on top of one hot encodings and build an embedding matrix $E$ such that
$$
\begin{aligned}
v_{n} = Ex_{n}
\end{aligned}
$$

where $x_{n}$ is of dimensions $K \times 1$ and $E$ is of dimensions $D \times K$. Here $D$ is the dimensionality of our embedding space.

There are two approaches to train and build these Word2Vec embeddings: Continuous Bag of Words (CBOW) or Skip-gram. Both require large corpus of text to train.

In CBOW, the input is the context around the word, while the output is the word itself. In Skip-gram, the input is the word while the output is the context around the word. Typically, a window of $M = 5$ is used in both the cases. These embeddings are often used as pre trained embeddings input to deep neural networks. The idea being that word representations are already avaialble, the network then starts to focus only on the relationships between the words and does not need to understand the words themselves.

Lets CBOW from a network perspective. $M=5$ means that we use $2$ words before and after our current word. First we use the emdedding matrix $E$ to conver these into embeddings, then run them through a fully connected neural network whose output is $K$ dimensional softmax, denoting the probability distribution across all the words in the dictionary. $E$ is a learnable parameter, and the loss function is the typical cross entropy loss on which word to select.

Skip-Gram involves the same mechanics, but learns context around the word from the word itself. Both approaches are easy to implement and train, giving reasonable embeddings that do capture semantic relationships as has been demonstrated with phrases like the embeddings themselves follow mathematical laws of similarity. For instance, $$\text{King} - \text{Queen} \approx \text{Man} - \text{Woman}$$.

### Character Level Embeddings
As discussed earlier, these also offer a good possibility giving low dimensional vectors. However, there are a few problems
- Sequences now become much longer, which means the compute time increases significantly
- Neural Network must learn to assemble words from characters to generate or infer semantic meaning.. this means the network has to perform this extra tasks to learn meaning first
- Words are usually more semantically meaningful than character level information

### Byte Pair Encodings
This approach gives best of both worlds. We use character level encodings instead of bytes.

In every iteration, it first finds which are the most commonly occurring pairs of characters and uses that as a token. The process keeps repeating till we have formed tokens of all characters in the corpus.

This approach is agnostic to misspellings as well since it does not depend on a strict dictionary. Hence unknown words can also be encoded without changing the dictionary at inference. The approach also has some rules defined for common base words that are always tokenized as a unit.

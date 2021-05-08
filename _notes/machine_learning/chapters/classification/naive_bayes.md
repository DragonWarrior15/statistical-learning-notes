---
title: "Naive Bayes Classifier"
---

## Naive Bayes Classifier

This is one of the simplest classifier that implements the Bayes Rule at it's core
\begin{align}
    P(Y \vert X) = \frac{P(X \vert Y)P(Y)}{P(X)}\end{align}
The algorithm is naive because it assumes that all the variables are independent and thus the joint distribution is nothing but the product of the individual distributions
\begin{align}
    P(Y \vert X) = \frac{\bigg( \prod_{i=1}^{p} P(X_{i} \vert Y) \bigg) P(Y)}{P(X)}\end{align}

Focusing on the binary case, we have
\begin{align}
    P(Y=1 \vert X) &= \frac{\bigg( \prod_{i=1}^{p} P(X_{i} \vert Y=1) \bigg) P(Y=1)}{P(X)}\newline
    P(Y=0 \vert X) &= \frac{\bigg( \prod_{i=1}^{p} P(X_{i} \vert Y=0) \bigg) P(Y=0)}{P(X)}\newline
    \frac{P(Y=1 \vert X)}{P(Y=0 \vert X)} &= \frac{\bigg( \prod_{i=1}^{p} P(X_{i} \vert Y=1) \bigg)}{\bigg( \prod_{i=1}^{p} P(X_{i} \vert Y=0) \bigg)} \frac{P(Y=1)}{P(Y=0)}\newline
\text{where} \; P(X_{i} = x_{i} \vert Y=y) &= \frac{\text{count of rows with } X_{i} = x_{i} \text{ in class } y}{\text{count of rows with } X_{i} = x_{i} \text{ across all classes}}\newline
P(Y=y) &= \text{fraction of rows with class } y\newline
1 &= P(Y=1 \vert X) + P(Y=0 \vert X)\end{align}
and the last equation can be used to get the individual values of $P(Y=1 \vert X)$ without the need to compute the joint distribution $P(X)$.

The equation to estimating $P(X_{i} = x_{i} \vert Y=y)$ works well in the case of categorical data. For continuous data, we make more assumptions for the datalike the **Gaussian Naive Bayes**
\begin{align}
     P(X_{i} = x_{i}  \vert  Y=y) = \frac{1}{\sqrt{2\pi \sigma_{y}^{2}}}exp(-\frac{(x_{i} - \mu_{y})^{2}}{2\sigma_{y}^{2}})\end{align}
and similarly, we can calculate the probabilities in other distributions like exponential etc.

### Text Document Classification

Naive Bayes is a common baseline for many textclassification tasks. Suppose we have $d$ documents, each containing a sequence of $N$ words $w_{i}$s and our aim is to classify into suppose positive ($Y=1$) and negative ($Y=0$) sentiments. We assume that each word in the document is independent, and the joint distribution is simply the product of all the individual words. The naive Bayes Model is
\begin{align}
    P(Y \vert D) = \frac{P(D \vert Y)P(Y)}{P(D)} = \frac{1}{P(D)} P(Y) \prod_{i=1}^{N} P(w_{i} \vert Y)\end{align}

$P(Y)$ as seen above is simply the proportion of documents with given sentiment in the corpus. We can ignore $P(D)$ as it is a normalization constant and we can work with the ratio $P(Y=1 \vert D)/P(Y=0 \vert D)$ and the equation $P(Y=1 \vert D) + P(Y=0 \vert D) = 1$ to calculate the requisite probabilities.
\begin{align}
    P(w_{i} \vert Y=y) = \frac{\text{count of appearances of word $w_{i}$ in documents with sentiment $y$}}{\text{Total words in the documents with sentiment $y$}}\end{align}
and counting is done with repetitions

#### Laplacian Smoothing

But in some corner cases, we might have the word only present in a single class, or the word is not present in the training data, but the testing data. In such a case, **Laplacian Smoothing** is used
\begin{align}
    P(w_{i} \vert Y=y) = \frac{\text{count of appearances of word $w_{i}$ in documents with sentiment $y$} + 1}{\text{Total words in the documents with sentiment $y$}+V}\end{align}
where we add the $1$ in the numerator to make all probabilities non zero, and add $V$, the vocabulary size (number of distinct words in the entire corpus across all clasess) to the denominator so that the probabilities sum upto $1$ (the total number of terms of the form $P(w_{i} \vert Y)$ are equal to the vocabulary size $V$; adding $1$ to the numerator everywhere forces us to add $V$ in the denominator to get a valid probability distribution).

#### Log of Odds

Since we are calculating the odds to finally get to the probabiltiy value, we can sometime work more conviniently with the $log$ values to avoid working with small probability values
\begin{align}
    log \bigg( \frac{P(Y=1 \vert D)}{P(Y=0 \vert D)} \bigg) &= log \bigg( \frac{P(Y=1)}{P(Y=0)} \bigg) + log \bigg( \frac{\prod_{i=1}^{N} P(w_{i} \vert Y=1)}{\prod_{i=1}^{N} P(w_{i} \vert Y=0)} \bigg)\newline
    \text{or, }\; log(P(Y=1 \vert D)) - log(P(Y=0 \vert D)) &= \big[ log(P(Y=1)) - log(P(Y=0)) \big] \newline &+ \big [ \sum_{i=1}^{N}log(P(w_{i} \vert Y=1)) - \sum_{i=1}^{N}log(P(w_{i} \vert Y=0)) \big]\end{align}

where the ratio $P(Y=1)/P(Y=0)$ is also called prior. The left hand side equals $0$ when the classes have equal probabilities. When this term is positive, we assign $y_{i}=1$ and vice versa. The further away this term from $0$, the more confident we are. We can even adjust the threshold to control sensitivity, accuracy etc.


#### Key Considerations

-   correlated features can lead to incorrect predictors as they can lead to inflated importance values.

-   The model is relatively straightforward and has little flexibility. Hence, it becomes important to engineer the features well. In case of text data, trying out different preprocessing techniques like removing stopwords, lemmatization, and feature engineering like ngrams, tf-idf can be of immense help.

---
title: "Long Short Term Memory (LSTM)"
---

# Long Short Term Memory (LSTM)

This more complicated architecture learns when to remember and when to forget, and builds upon the concept of gate to restrict/allow flow of information, and we have an additional cell state that serves as the unit's memory. It contains three gates

1.  Forget Gate: Decides what information to keep/forget

2.  Input Gate: Decides how much of the new informaiton should be added

3.  Output Gate: Decides how much to chages should be done to get next hidden state

Mathematically, we have the following sequence of operations
\begin{alignat}{2}
    \Gamma_{f} &= \sigma([h_{t-1}, x_{t}]W_{f} + b_{f}) &\text{forget gate}\newline
    \Gamma_{i} &= \sigma([h_{t-1}, x_{t}]W_{i} + b_{i}) &\text{input gate}\newline
    C_{t}^{\prime} &= tanh([h_{t-1}, x_{t}]W_{c} + b_{c}) \quad&\text{cell state candidate}\newline
    C_{t} &= \Gamma_{f} \odot C_{t-1} + \Gamma_{i} \odot C_{t}^{\prime} &\text{new cell state}\newline
    \Gamma_{o} &= \sigma([h_{t-1}, x_{t}]W_{o} + b_{o}) &\text{output gate}\newline
    h_{t} &= \gamma_{o} \odot tanh(C_{t}) &\text{next hidden state}
\end{alignat}

---
title: "Gated Recurrent Unit (GRU)"
---

# Gated Recurrent Unit (GRU)

No, these are not the cousins of Gru from Despicable Me ! These are a modified versions of vanilla RNN with the key difference of controlling information flow. We can adjust how much of the past information to keep and how much of the new information to add. Specifically, the model can learn to reject some time steps that may not be relevant and learn to place weightage on some older hidden states as time progresses. This is useful when dealing with long term dependencies.


To start, we now have to new calculations that are called retain and update gate
\begin{align}
    \Gamma_{r} &= \sigma \bigg( [h_{t-1}, x_{t}]W_{r} + b_{r} \bigg)\newline
    \Gamma_{u} &= \sigma \bigg( [h_{t-1}, x_{t}]W_{u} + b_{u} \bigg)\end{align}
where $\sigma$ is the sigmoid activation. This allows us to calculate coefficients that are in the range $[0,1]$ and signify what ratio of information to keep/update. Next, we calculate the hidden state incorporating these coefficients
\begin{align}
    h_{t}^{\prime} &= tanh([\Gamma_{r} h_{t-1}, x_{t}]W_{h} + b_{h})\end{align}
where $h^{\prime}$ is not the derivative, but a candidate value for the hidden state. The final hidden state is calculated as a weighted average
\begin{align}
    h_{t} &= \Gamma_{u}h_{t} + (1 - \Gamma_{u})h_{t}^{\prime}\end{align}
and the targets can be calculated as
\begin{align}
{2}
    y_{t} &= f_{y}(h_{t}W_{y} + b_{y}) \quad &&\mbox{for many outputs}\newline
    y_{T} &= f_{y}(h_{T}W_{y} + b_{y}) \quad &&\mbox{in case of single output}\end{align}

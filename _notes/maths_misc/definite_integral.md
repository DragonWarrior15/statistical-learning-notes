---
title: "Definite Integral"
---

### Question: Compute the following
\begin{align}
    \int_{0}^{\pi/2} \frac{\sin x}{\sin x + \cos x} dx
\end{align}

### Solution
Substitute $t = \pi/2 - x$, $dt = -dx$

\begin{align}
    I &= \int_{0}^{\pi/2} \frac{\sin x}{\sin x + \cos x} dx\newline
    &= \int_{\pi/2}^{0} \frac{\sin (\pi/2 - t)}{\sin (\pi/2 - t) + \cos (\pi/2 - t)} (-dt)\newline
    &= -\int_{\pi/2}^{0} \frac{\cos t}{\cos t + \sin t} dt\newline
    &= \int_{0}^{\pi/2} \frac{\cos t}{\cos t + \sin t} dt = I\newline
    \implies 2I &= \int_{0}^{\pi/2} \frac{\sin x}{\sin x + \cos x} dx + \int_{0}^{\pi/2} \frac{\cos t}{\cos t + \sin t} dt\newline
    2I &= \int_{0}^{\pi/2} \frac{\sin x + \cos x}{\sin x + \cos x} dx = \int_{0}^{\pi/2} dx\newline
    &= \frac{\pi}{2}\newline
    \implies I &= \frac{\pi}{4}
\end{align}

---
title: "Answer"
---

Start with the merged Poisson process which will denote the time till the first bulb will fail. For this process, $\lambda^{\prime} = 3\lambda$. Hence, $E[\text{first bulb fails}] = \frac{1}{3\lambda}$.
After the first bulb dies out, we are left with a process with $\lambda^{\prime} = 3\lambda$. Due to memoryless property, $E[\text{second bulb fails}] = \frac{1}{2\lambda}$ and consequently $E[\text{last bulb fails}] = \frac{1}{\lambda}$.

Note the above two times denote the time difference, i.e. the time taken for the bulb to die out after the last bulb died out. Thus, $E[\text{time until last bulb dies out}] = \frac{1}{3\lambda} + \frac{1}{2\lambda} + \frac{1}{\lambda}$

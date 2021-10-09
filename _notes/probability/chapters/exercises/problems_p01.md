---
title: "Exercises Part 1"
---

## Exercises Part 1

1.  **Independence in Complements**

    Given $A \perp B$, show $A \perp B^{c}$ and $A^{c} \perp B^{c}$. [Solution]({{ "/notes/probability/chapters/exercises/a_indcomp.html" | relative_url }})

1.  **Conditional Independence**

    $A,B,$ and $C$ are independent with $P(C) > 0$. Show that $A\perp B \vert C$. [Solution]({{ "/notes/probability/chapters/exercises/a_conind.html" | relative_url }})

1.  **Geometry of Meeting**

    R and J have to meet at a given place and each will arrive at the given place independent of each other with a delay of 0 to 1hr uniformly distributed. The pairs of delays are all equally likely. The first to arrive waits for 15 minutes and leaves. What is the probability of meeting ? [Solution]({{ "/notes/probability/chapters/exercises/a_geomeet.html" | relative_url }})

1.  **Expectation of Function**

    Let $X$ and $Y$ be random variables with $Y = g(X)$. Show $E[Y] = \sum_{x}g(x)p_{X}(x)$. [Solution]({{ "/notes/probability/chapters/exercises/a_expfn.html" | relative_url }})

1.  **Cumulative Distribution Function**

    A random variable X is a combination of a continuous and discrete distribution as follows
    \begin{align}
            f_{X}(x) = \begin{cases} 0.5 &\mbox{$a \leq x \leq b$}\newline
                                     0.5 &\mbox{x = 0.5}\newline
                                     0 &\mbox{otherwise} \end{cases}
        \end{align}
    Find the Cumulative Distribution of X. [Solution]({{ "/notes/probability/chapters/exercises/a_cumuldistfn.html" | relative_url }})

1.  **Number of tosses till first head**

    When tossing a fair coin, what is the $E[$\# tosses till the first H$]$. [Solution]({{ "/notes/probability/chapters/exercises/a_tossh.html" | relative_url }})

1.  **Iterated Expectation Proof**

    For discrete variables, show $E[X] = E[E[X \vert Y]]$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexpproof.html" | relative_url }})

1.  **Iterated Expectation for three variables**

    For three random variables $X$, $Y$ and $Z$, show $E[Z \vert X] = E[E[Z \vert X,Y] \vert X]$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexpthree.html" | relative_url }})

1.  **Iterated Expectation practice**

    A class has two sections denoted by the random variable $Y$. Let $X$ denote the quiz score of a student. Given that section 1 has 10 students, section 2 has 20 students, $E[X \vert Y=1] = 90, E[X \vert Y=2] = 60, Var(X \vert Y=1) = 10, Var(X \vert Y=2) = 20$, find $E[X]$ and $Var(X)$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexppractice.html" | relative_url }})

1.  **Hat Problem**

    $n$ people throw their hats in a box and then pick a hat at random. What is the expected number of people who pick their own hat ? [Solution]({{ "/notes/probability/chapters/exercises/a_hatproblem.html" | relative_url }})

1.  **Breaking a stick**

    A stick of length $l$ is broken first at $X$ uniformly chosen between $[0,l]$, and then at $Y$, uniformly chosen between $[0,X]$. Find the expected length of the shorter part. [Solution]({{ "/notes/probability/chapters/exercises/a_breakstick.html" | relative_url }})

1.  **Convolution of Exponentials**

    Suppose $X \sim exp(\lambda)$ and $Y \sim exp(\mu)$, find the probability distribution $p_{X+Y}(x)$. [Solution]({{ "/notes/probability/chapters/exercises/a_convexp.html" | relative_url }})

1.  **Triangles from a Stick**

    We have a stick of length 1. We randomly choose two points on the stick and break the stick at those points. Calculate the probability that the three pieces form a triangle. [Solution]({{ "/notes/probability/chapters/exercises/a_trianglestick.html" | relative_url }})

1.  **PMF of g(X)**

    Let $X$ be uniform in $[0, 2]$, then find the PMF of $Y = X^{3}$. [Solution]({{ "/notes/probability/chapters/exercises/a_pmffn.html" | relative_url }})

1.  **Change of Variables**

    Let $\mathbf{X} = (x_{1}, x_{2})$ have the following distribution function
    \begin{align}
        f_{X}(x) &= \begin{cases} 10x_{1}x_{2}^{2} &\mbox{$0 < x_{1} < x_{2} < 1$}\newline 0 &\mbox{otherwise} \end{cases}
    \end{align}

    and let $\mathbf{Y}$ be the transformed variable defined as
    \begin{align}
        Y_{1} &= \frac{X_{1}}{X_{2}}\newline
        Y_{2} &= X_{2}
    \end{align}

    Find the distribution of $\mathbf{Y}$ and the marginal distributions of $Y_{1}$ and $Y_{2}$. Also comment about their independence. [Solution]({{ "/notes/probability/chapters/exercises/a_two_var_change.html" | relative_url }})

1.  **Change of Variables Part 2**

    For the transformation $Y = X^{2}$, find the distribution of $Y$ in the following two cases

    \begin{align}
        f_{X}(x) &= \begin{cases}\frac{1}{2} &\mbox{$-1 < x < 1$}\newline 0 &\mbox{else} \end{cases}\newline
        f_{X}(x) &= \begin{cases}\frac{1}{4} &\mbox{$-1 < x < 3$}\newline 0 &\mbox{else} \end{cases}\newline
    \end{align}

    [Solution]({{ "/notes/probability/chapters/exercises/a_two_var_change_part_2.html" | relative_url }})

1.  **Waiting for Taxi**

    A taxi stand and bus stop near Al's home are at the same location. Al goes there and if a taxi is waiting $P=\frac{2}{3}$, he boards it. Otherwise, he waits for a taxi or bus to come, whichever is first. Taxi takes anywhere between $0$ to $10$ mins (uniform) while a bus arrives in exactly 5 mins. He boards whichever is first. Find CDF and $E$\[wait time\]. [Solution]({{ "/notes/probability/chapters/exercises/a_waittaxi.html" | relative_url }})

1.  **Bayes Theorem**

    Let $Q$ be a continuous random variable with PDF
    \begin{align}
            f_{Q}(q) = \begin{cases} 6q(1-q) &\mbox{ $0 \leq q \leq 1$}\newline
                                     0 &\mbox{ otherwise} \end{cases}
        \end{align}
    where $Q$ represents $P(success)$ for a Bernoulli $X$, i.e., $P(X=1|Q=q) = q$. Find $f_{Q|X}(q|x) \forall x \in [0,1]$ and $q$. [Solution]({{ "/notes/probability/chapters/exercises/a_bayes.html" | relative_url }})

1.  **A Normal Transformation**

    Let $X \sim \mathcal{N}(0,1)$ and $Y = g(X)$. Find $p_{Y}(y)$.
    \begin{align}
            g(t) = \begin{cases} -t &\mbox{$t \leq 0$}\newline
                                \sqrt{t} &\mbox{$t > 0$} \end{cases}
        \end{align}
    [Solution]({{ "/notes/probability/chapters/exercises/a_normaltr.html" | relative_url }})

1.  **Distribution using the mgf**
    Let $X_{i}$ for $i=1,\ldots,4$ be four independent identically distributed exponential random variables with rates $1$. Find the distribution of $Y = \sum_{i=1}^{4}X_{i}$. [Solution]({{ "/notes/probability/chapters/exercises/a_mgf_dist.html" | relative_url }})

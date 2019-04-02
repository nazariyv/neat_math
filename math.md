# Oh Glorious Maths

- $f(x) dx = \mathbb{P}[x \leq X < x + dx]$
  - Discretizing the pdf
- $5 \choose 2$ is
  - How many unique pairs from $5$ can you choose:

<img src="https://cdn-images-1.medium.com/max/1600/0*668VCMzhSTiYbvq3.png" style="display: block; margin: 0 auto; width:600px" />

- $f(x) \sim g(x)$ means $\lim_{x \to a} \frac{f(x)}{g(x)} = c$
- $\log_{b}(a) = c \iff b^c = a$
- Big-O sorted (from fastest to slowest; big o is the asymptotic runtime): $\mathcal{O}(1)$ (constant time), $\mathcal{O}(\log N)$ (log time; divide and conquer), $\mathcal{O}(N)$ (linear time), $\mathcal{O}(N \log N)$ (merge search), | $\mathcal{O}(N^2)$ (quadric time), $\mathcal{O}(2^N)$ (exponential time), $\mathcal{O}(N!)$, ​$\mathcal{O}(\infty)$ (flipping coin)
  - Definition: for some $n \geq n_1$, $f(n) = \mathcal{O}(g(n))$ means: $|f(n)| \leq c|g(n)|$ for some $c \in \mathbb{R}$
  - some properties. $\mathcal{O}(c + n) = \mathcal{O}(n)$ for some $c > 0$.
  - $c \mathcal{O}(n) = \mathcal{O}(n)$
  - example. Nested loop. `for (i=0; i<n; i++) { for (j=i; j<n; j++) }`. Notice that the inner loop runs:
    $n, n-1, n-2, ..., 3, 2, 1$ number of times. This is $n(n+1)/2$. Thus $\mathcal{O}(n^2)$
  - Imagine you have a sorted array. This is log time. Divide and conquer

# Oh Glorious People Who Created this

- Interneting is hard is a series of HTML & CSS tutorials that are kicking ass:
  https://internetingishard.com/html-and-css

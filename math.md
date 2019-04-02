# Oh Glorious Maths

- **Discretizing** a pdf: $f(x) dx = \mathbb{P}[x \leq X < x + dx]$
- **Combinatorics**: How many unique pairs from $5$ can you choose:
  - $5 \choose 2​$ is

<img src="https://cdn-images-1.medium.com/max/1600/0*668VCMzhSTiYbvq3.png" style="display: block; margin: 0 auto; width:600px" />

- **Permutations**: 3! = 3 * 2 * 1. How many permutations can you have? Suppose you have a banana, an apple, and a carrot. You can eat them in the following sequences: ABC, BAC, CAB, ACB, BCA, CBA; i.e. 6 in total. You start off by choosing when to eat an apple, three possibilities (you eat it first, second or third), once that is chosen, you have two possibilities of choosing when to eat a banana (if you decided to eat an apple first, then banana can be second or third; if you decided to eat an apple second, then banana can be first or last; if you choose to eat an apple last, then banana can be first or second; i.e. in each case, you have two options). Finally, once the order of eating an apple and banana is chosen, there is only one position for a carrot. Eat your veggies. 
- $f(x) \sim g(x)$ means $\lim_{x \to a} \frac{f(x)}{g(x)} = c$
- $\log_{b}(a) = c \iff b^c = a$
- **Big-O** sorted (from fastest to slowest; big o is the asymptotic runtime): $\mathcal{O}(1)$ (constant time), $\mathcal{O}(\log N)$ (log time; divide and conquer), $\mathcal{O}(N)$ (linear time), $\mathcal{O}(N \log N)$ (merge search), | $\mathcal{O}(N^2)$ (quadric time), $\mathcal{O}(2^N)$ (exponential time; going through all of the subsets of a set), $\mathcal{O}(N!)$ (finding all permutations of a string), $\mathcal{O}(\infty)$ (flipping coin). Useful <a href='<https://www.youtube.com/watch?v=zUUkiEllHG0&t=>'>video code examples</a>. 
  - Definition: for some $n \geq n_1​$, $f(n) = \mathcal{O}(g(n))​$ means: $|f(n)| \leq c|g(n)|​$ for some $c \in \mathbb{R}​$
  - some properties. $\mathcal{O}(c + n) = \mathcal{O}(n)$ for some $c > 0$.
  - $c \mathcal{O}(n) = \mathcal{O}(n)$
  - example. Nested loop. `for (i=0; i<n; i++) { for (j=i; j<n; j++) }`. Notice that the inner loop runs:
    $n, n-1, n-2, ..., 3, 2, 1$ number of times. This is $n(n+1)/2$. Thus $\mathcal{O}(n^2)$
  - Imagine you have a sorted array. This is log time. Divide and conquer

# Oh Glorious People Who Created this

- Interneting is hard - is a series of HTML & CSS tutorials that are kicking ass:
  https://internetingishard.com/html-and-css

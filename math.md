# Oh Glorious Maths

- **Discretizing** a pdf: $f(x) dx = \mathbb{P}[x \leq X < x + dx]​$
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
- How many times can you split 32 into even parts? $2^5$, $5$ times. $\log_2 (32) = 5$, that is why divide and conquer is $\mathcal{O}(\log n)$. Merge sort is $\mathcal{O}(n \log n)$ because you also do $\mathcal{O}(n)$ operations when mergin sorted arrays. (check out the code in the python scripts folder and the exercise below).



# Oh Glorious Problems (not exercises)

- **Remember**: logic is king. Make small sound logical steps when solving anything. If every step is correct, you will arrive at a solution. Do not get discouraged if you fail. Sometimes you need to try a number of approaches to solve a problem.
- 1. A census-taker knocks on a door, and asks the woman inside how
     many children she has and how old they are.
     "I have three daughters, their ages are whole numbers, and the product of the ages
     is 36," says the mother.
     "That's not enough information," responds the census-taker.
     "I'd tell you the sum of their ages, but you 'd still be stumped."
     "I wish you 'd tell me something more."
     "Okay, my oldest daughter Annie likes dogs."
     What are the ages of the three daughters? 

# Exercises (CS)

**Arrays**

1. Merge two sorted arrays:

   ```python
   arr1, arr2 = [1, 5, 9], [2, 3, 11, 18]
   len1, len2 = len(arr1), len(arr2)
   merge_sorted = []
   ix1, ix2 = 0, 0
   
   # idea is to go through element in arr1 and compare it to element in arr2
   # ix1 = 0, ix2 = 0. if arr1[ix1] >= arr2[ix2]: merge_sorted.push[arr2[ix2]] and ix2++
   # else merge_sorted.push[arr1[ix1]] and ix1++
   while (ix1 != len1 and ix2 != len2): # O(n), where n is the length of combined list
     if arr1[ix1] >= arr2[ix2]:
       merge_sorted.append(arr2[ix2]) # O(1)
       ix2 += 1 # O(1)
     else:
       marge_sorted.append(arr1[ix1])
       ix1 += 1
   
   # finalize, constant time O(1)
   if len2 > len1:
     merge_sorted += arr2[ix2:]
   elif len1 > len2:
     merge_sorted += arr1[ix1:]
   else:
     val1, val2 = arr1.pop(), arr2.pop()
     if merge_sorted[-1] == val1:
       merge_sorted.append(val2)
     else:
       merge_sorted.append(val1)
       
   # merge two sorted arrays time complexity: O(n)
   ```

   2. Find first non-repeating integer in an array. 

   ```python
   arr1 = [1, 1, 1, 2, 5, 5]
   prevVal = arr1[0]
   
   some_func:
     for ix, elem in enumerate(arr1):
       if elem != prevVal:
         return ix
       else:
         continue
       return -1
   
   # O(n) - worst case
   ```

3. Find the second minimum element of an array. Trivial, instead of having one variable for the min, have two: `min1` and `min2`.

4. Perform merge sort on $[1, 20, 3, 12, 5, 9, 10, 2]​$.

5. Rearrange negative and positive numbers such that the neg. numbers appear on the left and positive are on the right. The order should be preserved. Do not use additional data structures. Do it in $\mathcal{O}(n)​$. For $[1, 7, -5, 9, -12, 15]​$ as an example. Output is supposed to be like: $[-5, -12, 1, 7, 9, 15]​$.

   ```Python
   # pseudocode:
   # loop through each element until first negative val is found
   # pop it from the list and place it in the zeroth index
   # loop until you find second, pop it and place it in the first index
   # repeat until you are at the last index.
   
   # if the initial value is negative, great; if not, we will shift it
   # for ix = 1 until i = len(arr) - 1  O(N-1) = O(N)
   # if arr[ix] < 0:
   #		val = arr.pop(ix)  O(1)
   #		arr = arr[:prev_neg_idx] + [val] + arr[prev_neg_idx:] O(1)
   #	  prev_neg_idx += 1 O(1)
   # return
   
   # O(N)
   ```

   

# Oh Glorious People Who Created this

- Interneting is hard - is a series of HTML & CSS tutorials that are kicking ass:
  https://internetingishard.com/html-and-css

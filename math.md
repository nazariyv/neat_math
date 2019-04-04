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
  - $c \mathcal{O}(n) = \mathcal{O}(n)​$
  - example. Nested loop. `for (i=0; i<n; i++) { for (j=i; j<n; j++) }`. Notice that the inner loop runs:
    $n, n-1, n-2, ..., 3, 2, 1​$ number of times. This is $n(n+1)/2​$. Thus $\mathcal{O}(n^2)​$
  - Imagine you have a sorted array. This is log time. Divide and conquer
- How many times can you split 32 into even parts? $2^5$, $5$ times. $\log_2 (32) = 5$, that is why divide and conquer is $\mathcal{O}(\log n)$. Merge sort is $\mathcal{O}(n \log n)$ because you also do $\mathcal{O}(n)$ operations when mergin sorted arrays. (check out the code in the python scripts folder and the exercise below).

# Oh Glorious CS

- LIFO vs FIFO
  - LIFO: 1 -> 2 -> 3. [1, 2, 3]. Last in is 3, it is the first out. Then 2. Then 1.
  - FIFO: 1 -> 2 -> 3. [1, 2, 3]. First in is 1, it is the first out. Then 2. Then 3.

- Stack - an abstract data type. Follows LIFO pattern. 

  <img src="https://cdn-images-1.medium.com/max/1600/0*wTbA-8eCwNNefSlJ" style="display: block; margin: 0 auto; width:600px" />

  - basic operations are: pop, isEmpty, peek/top, push

- Queue - also a linear abstract data type like a stack. This is literally a queue. FIFO. You push to the back and pop from the top. Unlike stacks where you push to the top and pop from the top. Common operations: enqueue (inserts an element to the back), dequeue (removes an element from the start of the queue), isEmpty, top

- Linked List

- Graph

- Tree

- Trie

- Hash Table

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

5. Rearrange negative and positive numbers such that the neg. numbers appear on the left and positive are on the right. The order should be preserved. Do not use additional data structures. Do it in $\mathcal{O}(n)$. For $[1, 7, -5, 9, -12, 15]$ as an example. Output is supposed to be like: $[-5, -12, 1, 7, 9, 15]​$.

   ```
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

6. Find the min of an array
7. Find the second min of an array
8. Find the nth min of the array in O(n) time. $[10, 2, 5, 6, 11, 3, 15]​$ think about placing a $10​$: $[2,5,6,3,10,11,15]​$ <- this is a correct index for $10​$. 

```
# initial thoughts
# [10, 2, 5, 6, 11, 3, 15] -> [2,5,6,3,10,11,15]
# if you can do this, then you are done. Because 10 is in the right index.
# so loop through the whole list and place the first element in the correct position
# if the element's position is larger than m, repeat in the right half
# if the element's position is less than m, repeat in the left half
# the average case for this algorithm is O(N) !!! Because you do:
# n + n/2 + n/4 + n/8 + ... = 2n
# compare this to merge sort's n log n.
```



**Stacks**

1. Evaluate postfix expressions using a stack. Examples of postfix expressions: $5 \, 1 \, 2 + 4 \times \, + \,3 −$, $A B C \times +$, $2 3 1 \times + 9 -$

   ```
   # initial thoughts
   # i. you always perform an operation on two operands
   # ii. you push the operands into the stack as long as you have not met an operator
   # iii. ii \implies that you need to hardcode all of the operands
   # iv. once you have met the operator, perform it's operation on the two popd operands.
   # v. continue
   ```

   

2. Sort values in a stack

   ```
   # initial thoughts
   # turn a stack into a list
   # merge sort
   # turn back into a stack
   ```

   

3. Check balanced parentheses in an expression. Examples: 

   ```
   {[()]}
   {[(])}
   {{[[(())]]}}
   
   # initial thoughts
   # you need a balance map. And you need to check if the current char is is the balance of the peek. If it is then pop and continue to the next char. Trivial
   ```

**Queues**

1. Implement stack using a queue
   - Stack is like this -> (end here) 3, 2, 1 (top here) -> Where 1 was the first to come in. You push to the end. Flow out of top.
   - Queue is like this -> (end here) 3, 2, 1 (top here)  -> BUT, you push to the top. Flow out of top.

```
# You start with a queue. And need to convert it into a stack. Stack is LIFO, and queue is FIFO. So it should be a matter of turning LIFO into FIFO.
# What does this mean?
# It means that instead of putting things to the back, you put them to the top.
```

2. Reverse first k elements of the queue

```
# Initial thoughts. 
# Queue's dequeue takes the elements from the top.
# It appends to the bottom, though.
# We need to dequeue the whole queue first
# We then need to reverse the first k elements
# And queue them in this reversed order
# Queue the remaining ones in their original dequeued order

# Example
# [1, 3, 8, 0, 2]
# dequeue first 3 elements
# 2 dequeued and appended to list, 0 dequeued and appended to list, 8 dequeued and appended to list. The list is: [2, 0, 8]
# keep dequeing, but do not append to the above list: [3, 1]
# now construct a new Queue:
# [2, 0, 8] start enqueueing from the last index to the first one
# [3, 1] enqueue from 0 index to the last

This is n operations to dequeue everything and then n operations to enqueue.
O(n).
```

3. Generate binary numbers from 1 to n using a queue (*)

```
# initial thoughts
# first let's have a look at these
# 1 10 11 100 101 110 111 1000 1001 1010 1100 1101 1110 1111
# 1 2  3  4   5   6   7   8
# Check this pattern.
# You have 1. Then you have 1 with a zero and a one: 10, 11. Then you have 10 with a zero and a one. Then you have 11 with a zero and a one. etc.
# This is O(1) time.

|_ Create an empty Queue.
|_ Push first value inside it as 1.
|_ Now run a loop for n times and follow below mentioned steps
      |_ Dequeue an item and print the number
      |_ Append "0" in the dequeued number and enqueue it in the Queue.
      |_ Append "1" in the dequeued number and enqueue it in the Queue.
```

The above is super cool! And is O(n)

**Linked List**



**Graphs**

**Trees**

**Trie**

**Hash Table**



# Oh Glorious People Who Created this

- Interneting is hard - is a series of HTML & CSS tutorials that are kicking ass:
  https://internetingishard.com/html-and-css
- Linked I used for some of the exercises in the CS section: https://medium.freecodecamp.org/the-top-data-structures-you-should-know-for-your-next-coding-interview-36af0831f5e3

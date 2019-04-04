#!/usr/bin/env python3
from queue import Queue

n = 10

q = Queue()
q.enqueue("1")

while n > 0:
    n -= 1
    val = q.dequeue()
    val1 = val + "0"
    q.enqueue(val1)
    val2 = val + "1"
    q.enqueue(val2)
    print(f'n: {10 - n}, val: {val}, queue: {q.items}')

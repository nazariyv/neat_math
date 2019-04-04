#!/usr/bin/env python3
from queue import Queue
from stack import Stack

class stackFromQueue(Queue):
    def __init__(self):
        super().__init__()

    def push(self, elem):
        self.items.append(elem)

def print_stacks(elem, stack, stackFromQueue, push=True):
    msg = f'Pushing elem: {elem}' if push else f'Popping elem.'
    print(msg)
    print(f'Stack: {stack.items}')
    print(f'StackFromQueue: {stackFromQueue.items}')

if __name__ == '__main__':
    stack = Stack()
    stackFromQueue = stackFromQueue()
    stack.push(1)
    stackFromQueue.push(1)
    print_stacks(1, stack, stackFromQueue)
    stack.push(5)
    stackFromQueue.push(5)
    print_stacks(5, stack, stackFromQueue)
    stack.pop()
    stackFromQueue.dequeue()
    print_stacks('', stack, stackFromQueue, False)

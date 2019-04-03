#!/usr/bin/env python3

from stack import Stack

def evaluate_the_postfix(expression: str):
    my_stack = Stack()
    operators = ['*', '+', '-', '/']

    for char in expression:
        if char not in operators:
            my_stack.push(char)
        else:
            # evaluate
            operand1, operand2 = my_stack.pop(), my_stack.pop()
            evaluated = eval(f'{operand2} {char} {operand1}')
            my_stack.push(evaluated)

    return my_stack.pop()

if __name__ == '__main__':
    print(evaluate_the_postfix('512+4*+3-'))

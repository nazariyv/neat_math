#!/usr/bin/env python3
from linked_list import SinglyLinkedList as ll

def reverse(l: ll):
    curr = l.head
    prev = None

    while curr.next:
        next_element = curr.next
        curr.next = prev
        prev = curr
        curr = next_element

    l.head = curr
    l.head.next = prev
    return l

if __name__ == '__main__':
    l = ll()
    linked_elems = [1, 2, 3, 4]
    for elem in linked_elems:
        l.append(elem)
    print(l)
    print("Reversing")
    print(reverse(l))

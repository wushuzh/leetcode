from random import randint
from functools import reduce
from solution import ListNode, deleteDuplicates


def cons(v, tail):
    head = ListNode(v)
    head.next = tail
    return head


def mklist(*args):
    return reduce(lambda tail, v: cons(v, tail), reversed(args), None)


def printSSL(lst):
    if lst:
        print("{} -> ".format(lst), end="")
        printSSL(lst.next)
    else:
        print('None')

from functools import reduce


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'ListNode(' + str(self.val) + ')'


def printSSL(lst):
    if lst:
        print("{} -> ".format(lst), end="")
        printSSL(lst.next)
    else:
        print('None')


def cons(v, tail):
    head = ListNode(v)
    head.next = tail
    return head


def mklist(*args):
    return reduce(lambda tail, v: cons(v, tail), reversed(args), None)


def convert_array(head):
    a = []
    succ = head
    while succ:
        a.append(succ.val)
        succ = succ.next
    return a

from functools import reduce


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return 'ListNode(' + str(self.val) + ')'

    def __eq__(self, other):
        return (car(self) == car(other)) and (cdr(self) == cdr(other))

    def __iter__(self):
        ''' enable iter for ListNode, the associated functions, e.g., map
        shall only be used when debugging i.e., print purpose or testing
        solution should not use this addon feature
        '''
        curr = self
        while curr:
            yield curr
            curr = curr.next
        else:
            yield None

    def __str__(self):
        return ' -> '.join(map(repr, self))


def printSSL(lst):
    if lst:
        print("{} -> ".format(repr(lst)), end="")
        printSSL(lst.next)
    else:
        print('None')


def cons(v, tail):
    head = ListNode(v)
    head.next = tail
    return head


def car(l):
    return l.val


def cdr(l):
    return l.next


def mklist(*args):
    return reduce(lambda tail, v: cons(v, tail), reversed(args), None)


def convert_array(head):
    a = []
    succ = head
    while succ:
        a.append(succ.val)
        succ = succ.next
    return a

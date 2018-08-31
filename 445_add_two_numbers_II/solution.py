import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode


def add_two_numbers_v1(l1: ListNode, l2: ListNode) -> ListNode:
    def get_length(head_node):
        i = 0
        while head_node:
            i += 1
            head_node = head_node.next
        return i

    len1 = get_length(l1)
    len2 = get_length(l2)
    max_len = max(len1, len2)

    p = h = ListNode(0)
    while max_len:
        p.next = ListNode(0)
        p = p.next
        if max_len <= len1:
            p.val += l1.val
            l1 = l1.next
        if max_len <= len2:
            p.val += l2.val
            l2 = l2.next
        max_len -= 1

    p = h
    while p:
        q = p.next
        # fast forward if continual carry may happens
        while q and q.val == 9:
            q = q.next
        # continual carry really happens
        if q and q.val > 9:
            while p is not q:
                p.val += 1
                p = p.next
                p.val -= 10
        else:
            p = q

    return h if h.val else h.next

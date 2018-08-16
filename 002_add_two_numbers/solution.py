import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode


def add_two_numbers_v1(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    dummy = n = ListNode('dummy')
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1 + v2 + carry, 10)
        n.next = ListNode(val)
        n = n.next
    return dummy.next

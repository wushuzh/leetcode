import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode


def rm_nth_from_end_v1(head: ListNode, n: int):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

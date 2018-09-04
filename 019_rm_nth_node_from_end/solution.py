from typing import Tuple
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


def rm_nth_from_end_v2(head: ListNode, n: int):
    def index(node):
        if not node:
            return 0
        i = index(node.next) + 1
        if i > n:
            node.next.val = node.val
        return i
    index(head)
    return head.next


def rm_nth_from_end_v3(head: ListNode, n: int) -> ListNode:
    def remove(head: ListNode) -> Tuple[int, ListNode]:
        if not head:
            return 0, head
        i, head.next = remove(head.next)
        return i+1, (head, head.next)[i+1 == n]
    return remove(head)[1]

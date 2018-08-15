import sys, os
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode


def deleteDuplicates(head: ListNode) -> ListNode:
    cur = head
    while cur and cur.next:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

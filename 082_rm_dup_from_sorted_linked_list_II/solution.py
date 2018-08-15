import sys, os
sys.path.insert(0, os.path.abspath('..'))
from common.linkedlist import ListNode


def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    p, q = dummy, dummy.next

    while p and q:
        found_duplicate = False
        while q.next and q.next.val == q.val:
            found_duplicate = True
            p.next = q.next
            q = q.next

        if found_duplicate:
            p.next = q.next
        else:
            p = p.next

        q = q.next

    return dummy.next

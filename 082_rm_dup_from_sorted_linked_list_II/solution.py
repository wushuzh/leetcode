class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'ListNode(' + str(self.val) + ')'


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
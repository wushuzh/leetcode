class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'ListNode(' + str(self.val) + ')'


def deleteDuplicates(head: ListNode) -> ListNode:
    cur = head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next
        cur = cur.next
    return head

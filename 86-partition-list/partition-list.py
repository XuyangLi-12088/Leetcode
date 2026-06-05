# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_cur = before_dummy = ListNode()
        after_cur = after_dummy = ListNode()
        cur = dummy = ListNode(0, head)
        while cur.next:
            if cur.next.val < x:
                before_cur.next = ListNode(cur.next.val)
                before_cur = before_cur.next
            else:
                after_cur.next = ListNode(cur.next.val)
                after_cur = after_cur.next
            cur = cur.next

        before_cur.next = after_dummy.next

        return before_dummy.next
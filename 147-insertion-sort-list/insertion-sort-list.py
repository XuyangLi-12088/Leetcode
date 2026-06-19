# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        sorted_list = head
        cur = sorted_list.next
        while cur:
            if sorted_list.val <= cur.val:
                sorted_list = sorted_list.next
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                sorted_list.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = sorted_list.next

        return dummy.next
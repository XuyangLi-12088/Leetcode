# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two Pointers:
        if head is None:
            return head

        cur = head
        pre = None
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

        # # Recursion:
        # return self.reverse(head, None)

    def reverse(self, cur, pre):
        if cur == None:
            return pre
        
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)


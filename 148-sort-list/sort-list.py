# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)

    def mergeSort(self, head):
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left_head = head
        right_head = slow.next
        slow.next = None

        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))

    def merge(self, left, right):
        cur = dummy = ListNode()
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right

        return dummy.next




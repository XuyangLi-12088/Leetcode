# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0, head)
        while cur.next and cur.next.next:
            val = cur.next.val
            # 保留Node
            if val != cur.next.next.val:
                cur = cur.next
            # 删除Node
            else:
                while cur.next and val == cur.next.val:
                    cur.next = cur.next.next

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Fast and Slow Pointers:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

        # # Set Solutions:
        # visited = set()
        # cur = head
        # while cur:
        #     if cur in visited:
        #         return cur
        #     visited.add(cur)
        #     cur = cur.next
        # return None
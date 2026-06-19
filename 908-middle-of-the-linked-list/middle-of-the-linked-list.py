# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Solution 1:
        # current = head
        # length = 0
        # while current != None:
        #     current = current.next
        #     length += 1

        # middle = math.floor(length / 2) + 1

        # current = head
        # count = 1
        # while count != middle:
        #     current = current.next
        #     count += 1

        # return current


        # Solution 2:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
            

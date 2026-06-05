# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        # 1. 计算链表长度，并找到尾节点
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        k %= length

        # 2. 首尾相连
        tail.next = head

        # 3. 找倒数第 k+1 个节点，作为新链表的尾节点
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # 4. 断开倒数第 k+1 个节点（new_tail）和倒数第 k 个节点（new_head）
        new_head = new_tail.next
        new_tail.next = None
        return new_head
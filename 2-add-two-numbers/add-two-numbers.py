# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode() # 哨兵节点
        carry = 0 # 进位值
        while l1 or l2 or carry: # 有一个不是空节点，或者还有进位，就继续迭代
            s = carry
            if l1:
                s += l1.val # 节点值和进位加在一起
                l1 = l1.next
            if l2:
                s += l2.val # 节点值和进位加在一起
                l2 = l2.next # 下一个节点
            cur.next = ListNode(s % 10) # 每个节点保存一个数位
            carry = s // 10 # 新的进位
            cur = cur.next # 下一个节点
        return dummy.next # 哨兵节点的下一个节点就是头节点


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        min_heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i))
                lists[i] = l.next
        while len(min_heap) != 0:
            pop = heapq.heappop(min_heap)
            # create New Node
            new_node = ListNode(pop[0])
            # add to the one sorted linked list
            cur.next = new_node
            cur = cur.next
            # add the next node into min heap
            if lists[pop[1]]:
                heapq.heappush(min_heap, (lists[pop[1]].val, pop[1]))
                lists[pop[1]] = lists[pop[1]].next

        return dummy.next
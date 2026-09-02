class Node:
    def __init__(self, val, n_prev=None, n_next=None):
        self.val = val
        self.prev = n_prev
        self.next = n_next

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1

        cur = self.head.next
        cur_i = 0
        while cur_i < index:
            cur = cur.next
            cur_i += 1
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        return

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len, val)
        return
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        
        cur = self.head
        for i in range(index):
            cur = cur.next

        node = Node(val)
        cur.next.prev = node
        node.next = cur.next
        cur.next = node
        node.prev = cur
        self.len += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return
        
        pre = self.head
        for i in range(index):
            pre = pre.next

        pre.next = pre.next.next
        pre.next.prev = pre
        self.len -= 1
        return





        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
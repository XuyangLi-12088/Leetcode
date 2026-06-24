class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyCircularQueue:
    # 队列的链式存储实现:
    def __init__(self, k: int):
        self.size = k
        self.cur_size = 0
        head = Node(0)
        self.front = head
        self.rear = head
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            node = Node(value)
            self.cur_size += 1
            self.rear.next = node
            self.rear = node
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            node = self.front.next
            self.cur_size -= 1
            self.front.next = node.next
            if self.rear == node:
                self.rear = self.front
            del node
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.front.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.rear.value

    def isEmpty(self) -> bool:
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.cur_size == self.size:
            return True
        else:
            return False 

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
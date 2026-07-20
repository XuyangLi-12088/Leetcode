class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack1) != 0:
            for i in range(len(self.stack1)-1):
                self.stack2.append(self.stack1.pop())

            pop = self.stack1.pop()

            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            
            return pop

    def peek(self) -> int:
        if len(self.stack1) != 0:
            for i in range(len(self.stack1)-1):
                self.stack2.append(self.stack1.pop())

            peek = self.stack1.pop()
            self.stack2.append(peek)

            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            
            return peek

    def empty(self) -> bool:
        if len(self.stack1)==0 and len(self.stack2)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
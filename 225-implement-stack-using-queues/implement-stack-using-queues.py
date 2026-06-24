class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if len(self.q1) != 0:
            self.q1.append(x)
        elif len(self.q2) != 0:
            self.q1.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        else:
            if len(self.q1) != 0:
                for i in range(len(self.q1) - 1):
                    self.q2.append(self.q1.popleft())
                top = self.q1.popleft()
                return top
            elif len(self.q2) != 0:
                for i in range(len(self.q2) - 1):
                    self.q1.append(self.q2.popleft())
                top = self.q2.popleft()
                return top

    def top(self) -> int:
        if self.empty():
            return -1
        else:
            if len(self.q1) != 0:
                for i in range(len(self.q1) - 1):
                    self.q2.append(self.q1.popleft())
                top = self.q1.popleft()
                self.q2.append(top)
                return top
            elif len(self.q2) != 0:
                for i in range(len(self.q2) - 1):
                    self.q1.append(self.q2.popleft())
                top = self.q2.popleft()
                self.q1.append(top)
                return top

    def empty(self) -> bool:
        if len(self.q1) == 0 and len(self.q2) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
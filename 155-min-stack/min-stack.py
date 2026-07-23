class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((value, value))
        else:
            cur_min = self.stack[-1][1]
            if cur_min < value:
                self.stack.append((value, cur_min))
            else:
                self.stack.append((value, value))
        return
        
    def pop(self) -> None:
        self.stack.pop()
        return

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1][1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
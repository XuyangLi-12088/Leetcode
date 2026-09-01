class MinStack:

    # 5 4 3 6 1
    # min_stack = [(5, 5), (4, 5), (3, 4), (6, 3), (1, 3)]


    def __init__(self):
        self.min_stack = []

    def push(self, value: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append((value, value))
        else:
            self.min_stack.append((value, min(self.min_stack[-1][0], self.min_stack[-1][1])))
        return
        
    def pop(self) -> None:
        self.min_stack.pop()
        return

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        if self.min_stack[-1][0] < self.min_stack[-1][1]:
            return self.min_stack[-1][0]
        return self.min_stack[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
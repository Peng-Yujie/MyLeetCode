class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        # self.min_val = min(val, self.min_val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
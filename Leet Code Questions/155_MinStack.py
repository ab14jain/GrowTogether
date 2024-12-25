class MinStack:

    def __init__(self):
        self.stack = []*(10**7)
        self.topIdx = -1
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.minVal = min(self.minVal, val)
        self.stack.append(val)
        self.topIdx += 1    

    def pop(self) -> None:
        if self.topIdx != -1:
            popped = self.stack.pop()
            if popped == self.minVal:
                if len(self.stack) > 0:
                    self.minVal = min(self.stack)
                else:
                    self.minVal = float('inf')
            self.topIdx -= 1

    def top(self) -> int:
        if self.stack and self.topIdx > -1:
            return self.stack[self.topIdx]        
        return -1

    def getMin(self) -> int:
        if self.stack and self.topIdx != -1 and len(self.stack) > 0:            
            return self.minVal
        
        return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
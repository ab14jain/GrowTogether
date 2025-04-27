# https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
class Solution:

    def __init__(self):
        # code here
        self.stack = []
        self.min_val = float('inf')
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        self.min_val = min(self.min_val, x)
        self.stack.append(x)


    # Remove the top element from the Stack
    def pop(self):
        # code here
        if self.stack:
            self.stack.pop()
            self.min_val = min(self.stack)
            return

    # Returns top element of Stack
    def peek(self):
        # code here
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here

        if self.min_val == float('inf'):
            return -1
        else:
            return self.min_val
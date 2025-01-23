#https://www.scaler.com/academy/mentee-dashboard/class/325330/assignment/problems/11439?navref=cl_tt_lst_nm
class UserQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.capacity = 10000
        self.main_stack = []
        self.aux_stack = []
        self.top = -1
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        if self.size == self.capacity:
            return
        self.main_stack.append(x)
        self.size += 1
        self.top += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.aux_stack) == 0:
            while len(self.main_stack) > 0:
                self.aux_stack.append(self.main_stack.pop())
        self.size -= 1
        self.top -= 1

        if len(self.aux_stack) == 0:
            return -1
        return self.aux_stack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.aux_stack) == 0:
            while len(self.main_stack) > 0:
                self.aux_stack.append(self.main_stack.pop())
        
        if len(self.aux_stack) == 0:
            return -1
        return self.aux_stack[-1]
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size == 0:
            return True
        return False

# Your UserQueue object will be instantiated and called as such:
obj = UserQueue()
# obj.push(20)
# print(obj.empty())
# print(obj.peek())
# print(obj.pop())
# print(obj.empty())
# obj.push(30)
# print(obj.peek())
# obj.push(40)
# print(obj.peek())


# obj.push(10)
# obj.push(20)
# obj.push(30)
print(obj.peek())
print(obj.pop())
# param2 = obj.pop()
# param3 = obj.peek()
# param4 = obj.empty()
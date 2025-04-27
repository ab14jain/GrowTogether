# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):        
        self.Nodes = set()
        self.add_nodes(0, root)   


    def add_nodes(self, num: int, node: TreeNode):

        if node == None:
            return
        
        self.Nodes.add(num)

        if node.left:                       
            self.add_nodes(2*num + 1, node.left)
        
        if node.right:
            self.add_nodes(2*num + 2, node.right)


    def find(self, target: int) -> bool:

        if target in self.Nodes:
            return True
        
        return False
        


# Your FindElements object will be instantiated and called as such:

root = TreeNode(-1)
root.left = TreeNode(-1)
root.right = TreeNode(-1)
root.left.left = TreeNode(-1)
root.left.right = TreeNode(-1)

obj = FindElements(root)
target = 2
param_1 = obj.find(target)
print(param_1)
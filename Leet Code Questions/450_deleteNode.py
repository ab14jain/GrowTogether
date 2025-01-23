# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:

            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:

                temp = root.right

                while temp.left:
                    temp = temp.left
                
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

        return root
    



s=Solution()
root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(6)
root.left.left=TreeNode(2)
root.left.right=TreeNode(4)
root.right.right=TreeNode(7)

root = s.deleteNode(root, 3) # [5,4,6,2,null,null,7]
# s.deleteNode(root, 5) # [6,4,7,2]
# s.deleteNode(root, 2) # [6,4,7]
# s.deleteNode(root, 4) # [6,7]
# s.deleteNode(root, 6) # [7]
# s.deleteNode(root, 7) # []
# s.deleteNode(root, 1) # []

# Time complexity: O(H) where H is the height of the tree

# Space complexity: O(H) where H is the height of the tree

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

inorder(root) # 7

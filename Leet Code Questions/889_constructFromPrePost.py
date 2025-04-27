# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    pre_s = 0
    pos_s = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        

        # def construct(node, pre, post, pre_s, pre_e, post_s, post_e):

        #     if pre_s > pre_e or post_s > post_e:
        #         return None
            
        #     root_val = pre[pre_s]            
        #     post_e = postorder.index(root_val)
        #     new_node = TreeNode(root_val)
        #     node.left = construct(new_node, pre, post, pre_s+1, pre_e, post_s, post_e-1)
        #     node.right = construct(new_node, pre, post, pre_s+1, post_e, post_e+1, post_e)

        #     return node
            


        
        # root_val = preorder[0]
        # root = TreeNode(root_val)
        # pre_s = 1
        # pre_e = len(preorder)
        # post_s = 0
        # post_e = postorder.index(root_val) - 1
        # construct(root, preorder, postorder, pre_s, pre_e, post_s, post_e)
        # return root

        # if not preorder or not postorder:
        #     return None
        # root_val = preorder.pop(0)
        # root = TreeNode(root_val)

        # if not preorder or not postorder:
        #     return root
        
        # post_e = postorder.index(root_val)
        # node_count = len(postorder[:post_e])

        # root.left = self.constructFromPrePost(preorder[1:], postorder[:post_e])        
        # root.right = self.constructFromPrePost(preorder[1+node_count:], postorder[post_e+1:])


        # if not preorder or not postorder:
        #     return None

        # # Create root from the first element of preorder
        # root = TreeNode(preorder.pop(0))  # Remove the first element (root)

        # # If there are no more elements, return root
        # if not preorder or not postorder:
        #     return root
    
        # # Find the index of the left child in postorder
        # left_child = preorder[0]  # Next element in preorder
        # if left_child in postorder:
        #     left_index = postorder.index(left_child)  # Find it in postorder

        # root.left = self.constructFromPrePost(preorder, postorder[:left_index + 1])
        # root.right = self.constructFromPrePost(preorder, postorder[left_index + 1:-1])

        # return root
       
        node = TreeNode(preorder[self.pre_s])
        self.pre_s += 1

        if node.val != postorder[self.pos_s]:
            node.left = self.constructFromPrePost(preorder, postorder)
        
        if node.val != postorder[self.pos_s]:
            node.right = self.constructFromPrePost(preorder, postorder)

        self.pos_s +=1 

        return node



def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

s=Solution()
root = s.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])
print(level_order_traversal(root))



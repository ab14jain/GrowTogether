from collections import deque
from typing import Optional

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def get_swap_count(nums):
            n = len(nums)
            swaps = 0
            sorted_nums = sorted(nums)
            
            num_idx_map = {num: i for i, num in enumerate(nums)}

            for i in range(n):
                if nums[i] != sorted_nums[i]:
                    swaps += 1
                    idx = num_idx_map[sorted_nums[i]]
                    nums[i], nums[idx] = nums[idx], nums[i]
                    num_idx_map[nums[i]] = i
                    num_idx_map[nums[idx]] = idx

            return swaps
        
        queue = deque([(root)])
        swap_count = 0        
        while queue:
            nums_by_level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                nums_by_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            swap_count += get_swap_count(nums_by_level)
        return swap_count
    
# Time: O(N)
# Space: O(N)

# 1
# 2 3
# 4 5 6 7
# 8 9 10 11 12 13 14 15
# 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31


def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode 

lst = [5,4,8,11,None,13,4,7,2,None,None,None,1]
root = creatBTree(lst, 0)
print(root)
s=Solution()
s.minimumOperations(root)


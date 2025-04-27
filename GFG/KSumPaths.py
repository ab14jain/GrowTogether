class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def sumK(self,root,k):
        # code here
        
        # def ksum(node, k, currSum):
            
        #     if node == None:
        #         return 0
            
        #     currSum += node.data
            
        #     pathCount = 0
            
        #     if currSum == k:
        #         pathCount += 1
                
        #     pathCount += ksum(node.left, k, currSum)
        #     pathCount += ksum(node.right, k, currSum)
            
        #     return pathCount

        # Python Program to Count all K Sum Paths in Binary Tree
        # Using Prefix sum Technique

        # Function to find paths in the tree which have their sum equal to K
        def countPathsUtil(node, k, currSum, pSum):
            if node is None:
                return 0

            pathCount = 0
            currSum += node.data

            
            if currSum == k:
                pathCount += 1

            
            pathCount += pSum.get(currSum - k, 0)
            pSum[currSum] = pSum.get(currSum, 0) + 1

            pathCount += countPathsUtil(node.left, k, currSum, pSum)
            pathCount += countPathsUtil(node.right, k, currSum, pSum)

            pSum[currSum] -= 1

            return pathCount
        
        
        prefix_sum = {}
        return self.sumK(root, k, 0, prefix_sum)


root = Node(8)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.right = Node(2)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right.right = Node(1)

k = 7
s=Solution()
print(s.sumK(root, k))


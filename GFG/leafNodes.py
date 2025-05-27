# https://www.geeksforgeeks.org/problems/print-leaf-nodes-from-preorder-traversal-of-bst2657/1

class Solution:
	def leafNodes(self, preorder):
		# code here
		
            leaves = []
            n = len(preorder)
            stack = []

            for i in range(n-1):
                found = False
                if preorder[i] > preorder[i+1]:
                   stack.append(preorder[i])
                else:
                    while stack and preorder[i+1] > stack[-1]:
                        stack.pop()
                        found = True

                if found:
                    leaves.append(preorder[i])

            
            leaves.append(preorder[-1])

            return leaves
    

s=Solution()
print(s.leafNodes([4,2,1,3,6,5]))
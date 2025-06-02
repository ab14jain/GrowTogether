#https://www.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1

class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None

class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here


        def recurse(root, length, len_sum, max_len, max_sum):

            if root is None:
                if length > max_len[0]:
                    max_len[0] = length
                    max_sum[0] = len_sum
                elif length == max_len[0] and len_sum > max_sum[0]:
                    max_sum[0] = len_sum

                return


            recurse(root.left, length+1, len_sum+root.data, max_len, max_sum)
            recurse(root.right, length+1, len_sum+root.data, max_len, max_sum)

        max_sum = [0]
        max_len = [-float('inf')]
        recurse(root, 0, 0, max_len, max_sum )
        return  max_sum[0]


s = Solution()
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(1)
root.right.left = Node(2)
root.right.right = Node(3)
root.left.right.left = Node(6)
print(s.sumOfLongRootToLeafPath(root))

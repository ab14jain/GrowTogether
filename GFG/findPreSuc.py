class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def findPreSuc(self, root, key):
        # code here

        pre = None
        suc = None
        current = root

        while current:
            if current.data < key:
                pre = current
                current = current.right
            elif current.data > key:
                suc = current
                current = current.left
            else:
                # If key is found
                # Find predecessor (rightmost in left subtree)
                if current.left:
                    temp = current.left
                    while temp.right:
                        temp = temp.right
                    pre = temp

                # Find successor (leftmost in right subtree)
                if current.right:
                    temp = current.right
                    while temp.left:
                        temp = temp.left
                    suc = temp
                break

        return [pre, suc]
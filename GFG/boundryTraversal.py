class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None



def isLeaf(node):
    return node.left is None and node.right is None

def collectBoundaryLeft(root, res):
    if root is None:
        return

    curr = root
    while not isLeaf(curr):
        res.append(curr.data)

        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def collectLeaves(root, res):
    current = root

    while current:
        if current.left is None:
            if current.right is None:
                res.append(current.data)            
            current = current.right            
        else:            
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
                
            if predecessor.right is None:
                
                predecessor.right = current
                current = current.left
            else:
                if (predecessor.left is None) :
                    res.append(predecessor.data)
                predecessor.right = None
                current = current.right

def collectBoundaryRight(root, res):
    if root is None:
        return

    curr = root
    temp = []
    while not isLeaf(curr):
        temp.append(curr.data)

        if curr.right:
            curr = curr.right
        else:
            curr = curr.left

    res.extend(reversed(temp))

def boundaryTraversal(root):
    res = []

    if not root:
        return res
    
    if not isLeaf(root):
        res.append(root.data)

    collectBoundaryLeft(root.left, res)
        
    collectLeaves(root, res)

    collectBoundaryRight(root.right, res)

    return res
    
if __name__ == "__main__":
  
    # Hardcoded Binary tree
    #        20
    #       /  \
    #      8    22
    #     / \     \
    #    4   12    25
    #       /  \
    #      10   14
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right.right = Node(25)

    boundary = boundaryTraversal(root)
    print(" ".join(map(str, boundary)))



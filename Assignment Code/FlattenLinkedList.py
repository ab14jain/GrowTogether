
class ListNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.down=None

# @param root: ListNode
# @return ListNode
def flatten(root):       

        if root.right == None:
            return root
        
        def merge_node(head1, head2):
            p1 = head1
            p2 = head2  

            dummy = ListNode(-1)
            merged = dummy

            while p1 and p2:             
                if p1.val < p2.val:
                    merged.right = p1
                    merged = merged.right
                    p1 = p1.down
                else:
                    merged.right = p2
                    merged = merged.right
                    p2 = p2.down 
                    
            while p1:
                merged.right = p1
                merged = merged.right  
                p1 = p1.down

            while p2:
                merged.right = p2
                merged = merged.right  
                p2 = p2.down

            return dummy.right

        # result = ListNode(-1)
        # pointer = root
        # while pointer:
        #     result.right = merge_node(pointer, pointer.right)
        #     pointer = pointer.right
            

        # return result.right

        head = root
        if not head or not head.right:
            return head

        head.right = flatten(head.right)

        head = merge_node(head, head.right)

        return head

        # if root.right == None:
        #     return root
        

        # def merge_node(p1, p2):
        #     # p1 = root
        #     # p2 = root.right          

        #     dummy = ListNode(-1)
        #     merged = dummy
        #     while p1 and p2:             
        #         while p1 and p1.val < p2.val:
        #             merged.down = p1    
        #             merged = merged.down            
        #             p1 = p1.down
                    
                    
                
        #         merged.down = p2     
        #         merged = merged.down            
        #         p2 = p2.down

        #     return (dummy.down)
        
        # node1 = root
        # node2 = root.right
        # new_node = None
        # while node2:
        #     new_node = merge_node(node1, node2) 
        #     node1 = new_node
        #     node2 = node2.right

        # final_node = ListNode(-1)
        # fn = final_node
        # nn = new_node
        # while nn:
        #     fn.right = nn
        #     fn = fn.right
        #     nn = nn.down
        
        # return final_node.right
                


root = ListNode(3)
root.right = ListNode(4)
root.right.right = ListNode(20)
root.down = ListNode(7)
root.down.down = ListNode(7)
root.down.down.down = ListNode(8)
root.right.down = ListNode(11)
root.right.right.down = ListNode(22)

print(flatten(root))
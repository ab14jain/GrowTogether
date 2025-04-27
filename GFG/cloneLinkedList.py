#https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
# Link list Node
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        # code here

        # random_mp = {}
        # address_mp = {}
        # dummy = Node(-1)
        # cloned_list = dummy

        # curr = head

        # while curr:

        #     cloned_list.next = Node(curr.data)            
        #     random_mp[curr.data] = curr.random.data if curr.random else None
        #     address_mp[curr.data] = cloned_list.next
        #     cloned_list = cloned_list.next

        #     curr = curr.next

        # cloned_list = dummy.next

        # while cloned_list:
        #     cloned_list.random = address_mp[random_mp[cloned_list.data]] if random_mp[cloned_list.data] else None
        #     cloned_list = cloned_list.next


        # return dummy.next


        # random_mp = {}
        # dummy_node = Node(-1)
        # cloned_list = dummy_node

        # curr = head
        # while curr:

        #     cloned_list.next = Node(curr.data)
        #     random_mp[curr] = cloned_list.next
        #     cloned_list = cloned_list.next  
        #     curr = curr.next

        # curr = head
        # cloned_list = dummy_node.next
        # while curr:
        #     cloned_list.random = random_mp[curr.random] if curr.random else None
        #     cloned_list = cloned_list.next
        #     curr = curr.next

        # return dummy_node.next


        curr = head
        while curr:
            copy_node = Node(curr.data)
            copy_node.next = curr.next
            curr.next = copy_node
            curr = copy_node.next
            

        curr = head
        copy_curr = head.next
        while curr:
            if curr.random:
                copy_curr.random = curr.random.next  
            curr = curr.next.next
            copy_curr = copy_curr.next.next if copy_curr.next else None
        
        curr = head
        copy_list = head.next
        copy_head = copy_list
        while curr:
            curr.next = copy_list.next
            if copy_list.next:
                copy_list.next = copy_list.next.next

            curr = curr.next
            copy_list = copy_list.next


        return copy_head
            



s=Solution()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(14)
# head.next.next.next.next.next.next = Node(2)
# head.next.next.next.next.next.next.next = Node(2)
# head.next.next.next.next.next.next.next.next = Node(9)

head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head.next


# head.next.random = head
# head.next.next.random = head.next.next.next.next
# head.next.next.next.random = head.next.next 
# head.next.next.next.next.random = head.next

hd = s.cloneLinkedList(head)

while hd:
    print(hd.data, end="")
    print('-->', end="")
    print(hd.random.data) if hd.random else print("None")
    hd = hd.next
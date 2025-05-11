'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''

from collections import defaultdict


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
				
class Solution:
    def segregate(self, head):
        #code here

        # mp = defaultdict(list)
        # arr = []
        # curr = head

        # while curr:

        #     mp[curr.data].append(curr)
        #     arr.append([curr.data, curr])
        #     curr = curr.next

            
        # arr.sort(key=lambda k: k[0])
        # dummy = Node(-1)
        # p = dummy

        # for val,nod in arr:
        #     nod.next = None
        #     p.next = nod

        #     p = p.next
        # # for i in range(3):

        # #     for node in mp[i]:
        # #         node.next = None
        # #         p.next = node
                
        # #         p = p.next

        # return dummy.next
    

        if not head or not head.next:
            return head

        # Dummy nodes for three separate lists
        zeroD = Node(-1)
        oneD = Node(-1)
        twoD = Node(-1)

        # Tails for the three lists
        zero = zeroD
        one = oneD
        two = twoD

        # Traverse the original list
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next

        # Connect the three lists together
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None

        # New head
        head = zeroD.next

        return head

s=Solution()

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)
head.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next.next = Node(2)

s.segregate(head)
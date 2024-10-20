# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # i = 0
        # j = 0
        # merged= []
        # while (i < len(list1)) or (j < len(list2)):
        #     if list1[i] == list2[j]:
        #         merged.append(list1[i])
        #         merged.append(list2[j])
        #         i += 1
        #         j += 1
                
        #     elif list1[i] < list2[j]:
        #         merged.append(list1[i])
        #         i += 1
        #     else:
        #         list1.insert(i, list2[j])                
        #         j += 1
        
        # return merged

        while list1.next != None and list2.next != None:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2

        
        
        return list1 if list1.val < list2.val else list2
    



s = Solution()
print(s.mergeTwoLists([1,2,4], [1,3,4,5,6])) # [1,1,2,3,4,4]
# print(s.mergeTwoLists([], [])) # []
# print(s.mergeTwoLists([], [0])) # [0]
# print(s.mergeTwoLists([0], [])) # [0]
# print(s.mergeTwoLists([1], [0])) # [0,1]
        
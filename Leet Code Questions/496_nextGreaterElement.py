class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = []
        hashmap = {}
        result = [-1]*len(nums1)
        for i in range(len(nums1)):
            hashmap[nums1[i]] = i
    

        for i in range(len(nums2)):  
            while stack and stack[-1] < nums2[i]:
                popped = stack.pop()
                index = hashmap[popped]
                result[index] = nums2[i]
                
            if nums2[i] in hashmap:
                stack.append(nums2[i])
        return result
                



s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2,5]))
# s.nextGreaterElement([2,4], [1,2,3,4])
# s.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
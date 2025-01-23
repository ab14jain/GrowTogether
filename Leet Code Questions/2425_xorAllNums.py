class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:

        # contri_mp = {}
        # m = len(nums1)
        # n = len(nums2)

        # for num1 in nums1:
        #     contri_mp[num1] = (contri_mp.get(num1, 0) + n)
        
        # for num2 in nums2:
        #     contri_mp[num2] = (contri_mp.get(num2, 0) + m)

        # xor_sum = 0
        # for num, contri in contri_mp.items():
        #     if contri % 2:
        #         xor_sum ^= num

        # return xor_sum

        m = len(nums1)
        n = len(nums2)
        xor_sum = 0
        if m % 2 == 0 and n % 2 == 0:
            return 0
        
        if m&1:
            for num in nums2:
                xor_sum ^= num
       
        
        if n&1:
            for num in nums1:
                xor_sum ^= num
        

        return xor_sum
            
            

        
s=Solution()
print(s.xorAllNums([2,1,3],[10,2,5,0])) # 13
print(s.xorAllNums([1,2],[3,4])) # 0
class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        ans = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j] and (i*j) % k == 0:
        #             ans += 1

        # return ans

        freq = {}
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]].append(i)
            else:
                freq[nums[i]] = [i]
        
        
        for num in freq:
            num_freq = freq[num]            
            if len(num_freq) > 1:
                for i in range(len(num_freq)):
                    for j in range(i+1,len(num_freq)):
                        if (num_freq[i]*num_freq[j]) % k == 0:
                            ans += 1
        return ans

    

s=Solution()
print(s.countPairs([4,5,10,2,3,1],2)) # 3
print(s.countPairs([4,1,3,3],5)) # 1
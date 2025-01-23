class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        k_sums =[sum(nums[:k])]
        for i in range(k,n):
            k_sums.append(k_sums[-1]+nums[i]-nums[i-k])

        idx_count_map = {}
        def find_max_sum(idx, count):
            if count == 3 or idx > (len(nums) - k):
                return 0
            if (idx,count) in idx_count_map:
                return idx_count_map[(idx,count)]
            
            include = k_sums[idx] + find_max_sum(idx+k, count+1)
            exclude = find_max_sum(idx+1, count)

            idx_count_map[(idx,count)] = max(include, exclude)
            return idx_count_map[(idx,count)]        
        
        def get_indices():
            i = 0
            indices = []

            while i <= (len(nums) - k) and len(indices) < 3:
                include = k_sums[i] + find_max_sum(i+k, len(indices) + 1)
                exclude = find_max_sum(i+1, len(indices))

                if include >= exclude:
                    indices.append(i)
                    i += k
                else:
                    i += 1
        
            return indices
    
        return get_indices()
    
            
    
s=Solution()
print(s.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)) # [0,3,5]
print(s.maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 2)) # [0,2,4]
print(s.maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 3)) # [0,3,6]
print(s.maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 4)) # [0,4,8]

        
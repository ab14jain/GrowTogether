import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:

        # Approach 1: Using a heap - TLE
        # time complexity: O(nlogn)
        # space complexity: O(n)
        # min_heap = []
        # n = len(nums)
        # for i in range(n):
        #     heapq.heappush(min_heap, [nums[i],i])
        

        # while k > 0:            
        #     top = heapq.heappop(min_heap)
        #     top[0] *= multiplier
        #     heapq.heappush(min_heap, top)
        #     k -= 1

        # min_heap.sort(key = lambda x : x[1])
        # min_heap = [x[0] % (10**9 + 7) for x in min_heap]

        # return min_heap

        # Approach 2: Using a 

        def mod_inv(m, pow, mod):
            if pow == 0:
                return 1
            if pow % 2 == 0:
                return mod_inv(m, pow // 2, mod) ** 2 % mod
            else:
                return (m * mod_inv(m, pow - 1, mod)) % mod

        if multiplier == 1:
            return nums

        mod = 10**9 + 7
        min_heap = []
        n = len(nums)
        min_nums = float("inf")
        max_nums = float("-inf")
        for i in range(n):
            heapq.heappush(min_heap, [nums[i],i])
            min_nums = min(min_nums, nums[i])
            max_nums = max(max_nums, nums[i])

        while k > 0:
            top = heapq.heappop(min_heap)           
            min_nums = top[0]
            if min_nums*multiplier > max_nums:
                # heapq.heappush(min_heap, [(min_nums*multiplier)% mod, top[1]])
                # k -= 1
                break
            else:
                top[0] = (top[0] * multiplier) % mod
                heapq.heappush(min_heap, top)
                max_nums = max(max_nums, top[0])

            k -= 1

        if k > n:
            multiplier_power = k // n
            remainder = k % n

            for num in min_heap:
                val = mod_inv(multiplier, multiplier_power, mod)
                num[0] = (num[0] * val)%mod
            
            k = remainder

        while k > 0:
            top = heapq.heappop(min_heap)
            top[0] = (top[0] * multiplier)
            heapq.heappush(min_heap, top)
            k -= 1
        
        
        min_heap.sort(key = lambda x : x[1])
        min_heap = [x[0] % mod for x in min_heap]

        return min_heap
    

        



s = Solution()
print(s.getFinalState([66307295,441787703,589039035,322281864], 900900704, 641725)) # [664480092,763599523,886046925,47878852]
# print(s.getFinalState([100000,2000], 2, 1000000)) # [999999307,999999993]
# print(s.getFinalState([161209470], 56851412, 39846)) # [198168519]
# print(s.getFinalState([1,2,3,4,5], 300, 2)) # [2,4,6,4,5]
# print(s.getFinalState([1,2,3,4,5], 5, 3)) # [3,6,9,12,15]
# print(s.getFinalState([1,2,3,4,5], 1, 1)) # [1,2,3,4,5]
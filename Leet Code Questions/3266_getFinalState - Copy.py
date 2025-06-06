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
            # if pow == 0:
            #     return 1
            # if pow % 2 == 0:
            #     return mod_inv(m, pow // 2, mod) ** 2 % mod
            # else:
            #     return (m * mod_inv(m, pow - 1, mod)) % mod

            res = 1

            while pow:
                if pow % 2:
                    res = (res * m) % mod
                    pow -= 1
                else:
                    m = (m * m) % mod
                    pow //= 2
            
            return res

        if multiplier == 1:
            return nums

        mod = 10**9 + 7
        min_heap = []
        n = len(nums)
        min_nums = float("inf")
        max_nums = float("-inf")
        for i in range(n):
            heapq.heappush(min_heap, [nums[i]%mod,i])
            min_nums = min(min_nums, nums[i])
            max_nums = max(max_nums, nums[i])

        
        while k > 0:
            # top = heapq.heappop(min_heap)           
            min_nums = min_heap[0][0]
            if min_nums*multiplier > max_nums:
                # heapq.heappush(min_heap, [(min_nums*multiplier)% mod, top[1]])
                # k -= 1
                break
            else:
                top = heapq.heappop(min_heap)  
                top[0] = (top[0] * multiplier) % mod
                heapq.heappush(min_heap, top)
                max_nums = max(max_nums, top[0])

            k -= 1
        
        after_break_last_iteration = []

        for i in range(len(min_heap)):
            after_break_last_iteration.append(min_heap[i])

        
        for i in range(len(after_break_last_iteration)):
            val = mod_inv(multiplier, k//n, mod)% mod
            after_break_last_iteration[i][0] = (after_break_last_iteration[i][0] * val) % mod
        
        heapq.heapify(after_break_last_iteration)
        extra = k % n
        #after_brak_last_iteration.heapify()
        for i in range(extra):
            # top = heapq.heappop(after_break_last_iteration)
            # top[0] = (top[0] * multiplier) % mod
            # heapq.heappush(after_break_last_iteration, top)
            after_break_last_iteration[i][0] = (after_break_last_iteration[i][0] * multiplier) % mod

        after_break_last_iteration.sort(key = lambda x : x[1])
        after_break_last_iteration = [x[0] % mod for x in after_break_last_iteration]
        

        # if k > n:
        #     multiplier_power = k // n
        #     remainder = k % n

        #     for num in min_heap:
        #         val = mod_inv(multiplier, multiplier_power, mod)
        #         num[0] = (num[0] * val)%mod
            
        #     k = remainder

        # while k > 0:
        #     top = heapq.heappop(min_heap)
        #     top[0] = (top[0] * multiplier)
        #     heapq.heappush(min_heap, top)
        #     k -= 1
        
        
        # min_heap.sort(key = lambda x : x[1])
        # min_heap = [x[0] % mod for x in min_heap]

        return after_break_last_iteration
    

        



s = Solution()
# print(s.getFinalState([66307295,441787703,589039035,322281864], 900900704, 641725)) # [664480092,763599523,886046925,47878852]
# print(s.getFinalState([100000,2000], 2, 1000000)) # [999999307,999999993]
# print(s.getFinalState([161209470], 56851412, 39846)) # [198168519]
# print(s.getFinalState([1,2,3,4,5], 300, 2)) # [145586002,72793001,609189505,72793001,340991253]
# print(s.getFinalState([1,2,3,4,5], 5, 3)) # [3,6,9,12,15]
# print(s.getFinalState([1,2,3,4,5], 1, 1)) # [1,2,3,4,5]


# print(s.getFinalState([100000,2000,1000,23432,32423423,2342342,2342323,34223,23423,24323], 2453, 1000000))
# print(s.getFinalState([7,8,9,10,11], 246181588, 313380))
print(s.getFinalState([889458628,338743558,875422936,684907163,233489834], 246181588, 313380))


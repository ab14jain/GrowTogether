import heapq
import math
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        def find_power(num, pow):

            if pow == 0:
                return 1
            
            half = find_power(num, pow//2)
            result = half*half%1000000007
            
            if pow%2 == 1:
                result = result*num%1000000007
            
            return result
            


        def unique_prime_count(num):
            primes = set()

            for i in range(2, math.floor(math.sqrt(num))+1):
                if num%i == 0:
                    primes.add(i)
                
                while num%i == 0:
                    num /= i
            
            if num > 1:
                primes.add(int(num))

            return len(primes)

        def cal_prime_score(arr):

            score = []
            for i in range(len(arr)):
                score.append(unique_prime_count(arr[i]))
            return score
        

        def next_greater(arr):
            n = len(arr)
            indexes = [n]*n

            stack = []

            for i in range(n-1,-1,-1):

                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()

                if stack:
                    indexes[i] = stack[-1]

                stack.append(i)
            return indexes

        def prev_greater(arr):
            n = len(arr)
            indexes = [-1]*n

            stack = []

            for i in range(n):

                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()

                if stack:
                    indexes[i] = stack[-1]

                stack.append(i)
            return indexes
        
        prime_score = cal_prime_score(nums)
        next_greater_indexes = next_greater(prime_score)
        prev_greater_indexes = prev_greater(prime_score)

        
        n = len(nums)
        subarrays_count = [0]*n
        for i in range(n):
            subarrays_count[i] = (next_greater_indexes[i] - i)*(i-prev_greater_indexes[i])
        
        # print(prime_score)
        # print(next_greater_indexes)
        # print(prev_greater_indexes)
        # print(subarrays_count)

        sorted_num = []
        score = 1
        for i in range(n):
            sorted_num.append([nums[i],i])

        sorted_num.sort(reverse=True)
        # print(sorted_num)
        i = 0
        while k:            
            num, idx = sorted_num[i]
            ops = min(k, subarrays_count[idx])

            score = (score*find_power(num, ops))%1000000007

            k -= ops
            i += 1

        return score%1000000007



s=Solution()
print(s.maximumScore([8,3,9,3,8], 2))
print(s.maximumScore([19,12,14,6,10,18], 3))
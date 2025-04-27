from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        # Brute Force: 
        # Time Complexity: O(n^3) n^2 for loop and n for calculating sum
        # Space Complexity: O(n) --> to store odd sum sub array, 
        # we can use int counter to count such sub array

        # n = len(arr)
        # odd_sum = []
        # for i in range(n):
        #     for j in range(i, n):
        #         temp_sum = sum(arr[i:j+1])
        #         if temp_sum & 1 == 1:
        #             odd_sum.append(arr[i:j+1])

        # return len(odd_sum)
    
        # Optimized solution would be using prefix sum: 
        # Time Complexity: O(n^2)
        # Space Complexity: O(n) --> to store prefix sum,        

        # MOD = 1000000007
        # n = len(arr)
        # prefix_sum = [0]*n
        # prefix_sum[0] = arr[0]
        # ans = []
        # count = 0
        # for i in range(1,n):
        #     prefix_sum[i] = prefix_sum[i-1]+arr[i]

        # for i in range(n):
        #     if prefix_sum[i] & 1 == 1:
        #         count += 1

        # O + O = E
        # O + E = O
        # E + E = E
        
        # Optimized solution would be using prefix sum: 
        # Time Complexity: O(n)
        # Space Complexity: O(1) --> to store prefix sum,      
        MOD = 1000000007
        n = len(arr)
        prefix_sum = 0
        even_sum_count = 0
        odd_sum_count = 0
        total = 0
        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum & 1 == 1:                
                total += even_sum_count
                total += 1 #sub array ite self
                total = total % MOD
                odd_sum_count += 1
            else:
                total += odd_sum_count
                total = total % MOD
                even_sum_count += 1
        return total % MOD


s=Solution()
print(s.numOfSubarrays([1,3,5]))
# [1,4,9]
# [9,8,5]
print(s.numOfSubarrays([2,4,6]))
print(s.numOfSubarrays([1,2,3,4,5,6,7]))

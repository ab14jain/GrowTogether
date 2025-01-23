# https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

class Solution:
    def subarraySum(self, arr, target):
        # code here

        # n = len(arr)

        # sum_map = {}
        # curr_sum = 0
        # for i in range(n):

        #     curr_sum += arr[i]

        #     if curr_sum == target:
        #         return [1, i + 1]
            
        #     if curr_sum - target in sum_map:
        #         return [sum_map[curr_sum - target] + 1, i + 1]
            
        #     sum_map[curr_sum] = i+1
        
        # return [-1]

        n = len(arr)
        curr = 0
        start = 0
        end = 0

        for i in range(n):
            curr += arr[i]

            if curr >= target:
                end = i
                while curr > target and start < end:
                    curr -= arr[start]
                    start += 1

                if curr == target:
                    return [start + 1, end + 1]
            
        return [-1]
    

            


s=Solution()
print(s.subarraySum([1, 2, 3, 7, 5], 12)) #2
print(s.subarraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)) #1
print(s.subarraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20)) #1
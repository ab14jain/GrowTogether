class Solution:
    def countSubarrays(self, arr, k):
        # code here

        n = len(arr)
        result = 0
        prefix_sum = {}
        current_sum = 0
        for i in range(n):           
            
            current_sum += arr[i]
            if current_sum == k:
                result += 1

            if (current_sum - k) in prefix_sum:
                result += prefix_sum[current_sum - k]
            
            if current_sum in prefix_sum:
                prefix_sum[current_sum] += 1
            else:
                prefix_sum[current_sum] = 1


        return result
    

s=Solution()
print(s.countSubarrays([10, 2, -2, -20, 10], -10))
print(s.countSubarrays([1, 0, 0, 0, 1, 0, 1], 2))
print(s.countSubarrays([1, 1, 1, 1, 1], 2))
print(s.countSubarrays([1, 0, 1, 0, 1], 2))
class Solution:
    def longestPalindrome(self, arr):
        # code here
        n = len(arr)
        left = 0 
        right = n - 1
        max_len = 0
        left_sum = arr[left]
        right_sum = arr[right]
        while left < right:
            
            if left_sum == right_sum:
                left += 1
                right -= 1
                left_sum = arr[left]
                right_sum = arr[right]
                max_len += 2
            elif left_sum < right_sum:
                left += 1
                left_sum += arr[left]                
            else:
                right -= 1
                right_sum += arr[right]

        if left == right:
            max_len += 1
            
        return max_len


s=Solution()
print(s.longestPalindrome([1,5,8]))
# print(s.longestPalindrome([1,2,3]))
# print(s.longestPalindrome([1,2,1,3]))
# print(s.longestPalindrome([12,12]))
print(s.longestPalindrome([6,1,8,7,1,5]))
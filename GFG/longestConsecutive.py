#https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1

class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here

        # arr.sort()
        # n = len(arr)
        # count = 1
        # max_count = 1
        # for i in range(1,n):
        #     if arr[i] == arr[i-1]+1:
        #         count += 1
        #         max_count = max(max_count,count)
        #     elif arr[i] == arr[i-1]:
        #         continue
        #     else:
        #         count = 1

        # return max_count
        ans = 3**365
        print(ans)
        n = len(arr)
        max_arr = max(arr)
        min_arr = min(arr)
        
        result_arr = [-1]*(max_arr-min_arr+1)

        for i in range(n):
            result_arr[arr[i]-min_arr] = 1

        count = 0
        max_count = 0
        for i in range(len(result_arr)):
            if result_arr[i] == 1:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0
        
        return max_count


s=Solution()
print(s.longestConsecutive([1,1,1,1,2,2,6,1,9,4,4,4,5,5,5,3,3,3,3]))
print(s.longestConsecutive([2,6,1,9,4,5,3]))
print(s.longestConsecutive([1,9,3,10,4,20,2]))
print(s.longestConsecutive([36,41,56,35,44,33,34,92,43,32,42]))
print(s.longestConsecutive([15,24,23,12,19,11,16,18,13,14,17,21,22,20]))
print(s.longestConsecutive([1,9,3,10,4,20,2]))
print(s.longestConsecutive([15,13,12,14,16,18,17,19,20,21,22,23,24]))
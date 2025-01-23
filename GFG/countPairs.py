#https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum--150253/1

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        
        # Approach 1 - Using two loops
        # Time complexity: O(n^2)
        # Space complexity: O(1)

        # n = len(arr)
        # sum_count = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if arr[i] + arr[j] == target:
        #             sum_count += 1
        
        # return sum_count
    
        # Approach 2 - Using dictionary
        # Time complexity: O(n)
        # Space complexity: O(n)

        # freq = {}        
        # sum_count = 0
        # n = len(arr)
        # for i in range(n):
            
        #     if (target - arr[i]) in freq:
        #         sum_count += freq[target - arr[i]]
            
        #     if arr[i] in freq:
        #         freq[arr[i]] += 1
        #     else:
        #         freq[arr[i]] = 1
            
        # return sum_count


        # Approach 3 - Using two pointers in sorted array
        # Time complexity: O(nlogn)
        # Space complexity: O(1)

        arr.sort()
        n = len(arr)
        left = 0
        right = n-1
        sum_count = 0
        while left < right:
            if arr[left] + arr[right] == target:
                cnt1 = 0
                cnt2 = 0
                ele1 = arr[left]
                ele2 = arr[right]

                # Count frequency of first element of the pair
                while left <= right and arr[left] == ele1:
                    left += 1
                    cnt1 += 1

                # Count frequency of second element of the pair
                while left <= right and arr[right] == ele2:
                    right -= 1
                    cnt2 += 1

                # If both the elements are same, then count of
                # pairs = the number of ways to choose 2
                # elements among cnt1 elements
                if ele1 == ele2:
                    sum_count += (cnt1 * (cnt1 - 1)) // 2

                # If the elements are different, then count of
                # pairs = product of the count of both elements
                else:
                    sum_count += (cnt1 * cnt2)
            elif arr[left] + arr[right] < target:
                left += 1
            else:
                right -= 1
                            
        
        return sum_count


s=Solution()
print(s.countPairs([1,1,1,1],2)) #6
print(s.countPairs([1,5,7,-1,5],6)) #3
print(s.countPairs([10,12,10,15,-1],2)) #125


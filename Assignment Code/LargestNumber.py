from functools import cmp_to_key


class Solution:
    # @param A : list of integers
    # @return a strings
    def largestNumber(self, A):        
        
        def compare(f,s):
            f_str = str(f)
            s_str = str(s)

            if (int(f_str[0]) < int(s_str[0])):
                return 1
            elif (int(f_str[0]) > int(s_str[0])):
                return -1
            else:
                if int(f_str+s_str) < int(s_str+f_str):
                    return 1
                elif int(f_str+s_str) > int(s_str+f_str):
                    return -1
                else:
                    return 0


        A.sort(key=cmp_to_key(compare))
        if A[0] == 0:
            return '0'
        else:
            return ''.join(map(str, A))

# Approach : Sorting the array based on the first digit of the number
# If the first digit is same then compare the number itself

# Time complexity : O(nlogn)
# Space complexity : O(n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No
# Your code here along with comments explaining your approach
# 1. Sort the array based on the first digit of the number
# 2. If the first digit is same then compare the number itself
# 3. Return the sorted array as string
# 4. If the array is [0,0,0,0] then return '0' as the output
# 5. Else return the sorted array as string



s= Solution()
print(s.largestNumber([8,89])) #9534330
print(s.largestNumber([3, 30, 34, 5, 9])) #9534330
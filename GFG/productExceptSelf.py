# https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1
import math


class Solution:
    def productExceptSelf(self, arr):
        #code here
        # n = len(arr)    
        # prefix_prod = [1] * n
        # suffix_prod = [1] * n

        # for i in range(1, n):
        #     prefix_prod[i] = prefix_prod[i-1] * arr[i-1]
        
        # for i in range(n-2, -1, -1):
        #     suffix_prod[i] = suffix_prod[i+1] * arr[i+1]

        # res = []

        # for i in range(n):
        #     res.append(prefix_prod[i] * suffix_prod[i])
        
        # return res

        # Below algorithm is O(n) time and O(1) space and 0 should not be present in the array
        # inisde the array

        # Using log10 and pow to solve in contant time space

        # n = len(arr)
        # sum_so_far = 0
        # for i in range(n):
        #     sum_so_far += math.log10(arr[i])

        # res = []
        # for i in range(n):
        #     res.append(int(pow(10.00, (sum_so_far - math.log10(arr[i])))))

        # return res


        # Using Power 
        # We know x/y mathematically is equal to x * 1/y or x * y^-1

        n = len(arr)
        prod = 1

        for i in range(n):
            prod *= arr[i]

        res = []
        for i in range(n):
            res.append(int(prod * pow(arr[i], -1)))

        return res

s=Solution()
print(s.productExceptSelf([10, 3, 5, 6, 2])) #[180, 600, 360, 300, 900]
# print(s.productExceptSelf([12, 0])) #[20, 12]
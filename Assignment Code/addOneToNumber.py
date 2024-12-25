class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        res = []
        carry = 0
        addOne = 1
        n = len(A)
        for i in range(n-1, -1,-1):
            temp_sum = A[i] + addOne + carry
            addOne = 0
            carry = 0
            if temp_sum > 9:
                carry = temp_sum // 10
                temp_sum = temp_sum % 10
            
            res.append(temp_sum)

        if carry > 0:
            res.append(carry)
        res.reverse()
        final_res = []
        for i in range(len(res)):
            if res[i] != 0:
                final_res = res[i:]
                break
        return final_res 


s = Solution()
print(s.plusOne([1, 2, 3])) # [1, 2, 4]
print(s.plusOne([9, 9, 9])) # [1, 0, 0, 0]
print(s.plusOne([0, 0, 0])) # [0, 0, 1]
print(s.plusOne([0, 0, 9])) # [0, 1, 0]
print(s.plusOne([1,9,9,9,9,9,9])) # [1, 0, 0]
print(s.plusOne([0,3,7,6,4,0,5,5,5])) # [1, 0, 0]
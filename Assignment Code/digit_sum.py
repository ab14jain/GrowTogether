class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        digit_sum = 0
        def digitSum(N,digit_sum):         
            if N == 0:
                if digit_sum <= 9:
                    return digit_sum
                else:
                    return digitSum(digit_sum,0)
           
            digit_sum += (N%10)
            
            return digitSum(N//10,digit_sum)

            # if digit_sum == 1:
            #     return 1
            # return digit_sum

        if digitSum(A,digit_sum) == 1:
            return 1
        return 0

s=Solution()
print(s.solve(963)) # 1
# print(s.solve(2)) # 0
# print(s.solve(3)) # 0  
# print(s.solve(8355719)) # 1
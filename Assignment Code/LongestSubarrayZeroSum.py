#https://www.scaler.com/academy/mentee-dashboard/class/325378/homework/problems/27742?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        if n == 0:
            return 0
        
        sum_dict = {}
        prefix_sum = [0] * n

        max_len = 0
        for i in range(n):
            if i == 0:
                prefix_sum[i] = A[i]
            else:
                prefix_sum[i] = prefix_sum[i-1] + A[i]
        

        for i in range(n):
            if prefix_sum[i] == 0:
                max_len = max(max_len, i+1)
            if prefix_sum[i] in sum_dict:
                x = 0
                while x < n:
                    if prefix_sum[x] == prefix_sum[i]:
                        break
                    x += 1
                max_len = max(max_len, i - x)                

            sum_dict[prefix_sum[i]] = sum_dict.get(prefix_sum[i], 0) + 1
        
        return max_len
    

# You can test the code for correctness with the help of given test cases
s=Solution()
A = [1, -2, 1, 2]
print(s.solve(A)) # Output: 3
A = [3, 2, -1]
print(s.solve(A)) # Output: 0
A = [1, 2, -2, 4]
print(s.solve(A)) # Output: 2
A = [1, 2, 3]
print(s.solve(A)) # Output: 0
A = [1, 2, 3, -3]
print(s.solve(A)) # Output: 2
#https://www.scaler.com/academy/mentee-dashboard/class/325378/homework/problems/27776?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n == 0:
            return 0
        
        sum_dict = {}
        prefix_sum = [0] * n
        
        count = 0
        for i in range(n):
            if i == 0:
                prefix_sum[i] = A[i]
            else:
                prefix_sum[i] = prefix_sum[i-1] + A[i]
        

        for i in range(n):
            if prefix_sum[i] == 0:
                count += 1
            if prefix_sum[i] in sum_dict:
                count += sum_dict[prefix_sum[i]]
            sum_dict[prefix_sum[i]] = sum_dict.get(prefix_sum[i], 0) + 1
           

        return count % 1000000007
    

# You can test the code for correctness with the help of given test cases
s=Solution()
A = [1, -1, -2, 2]
print(s.solve(A)) # Output: 3
A = [-1, 2, -1]
print(s.solve(A)) # Output: 1
A = [1,2,-2,4]
print(s.solve(A)) # Output: 1
A = [1,2,3]
print(s.solve(A)) # Output: 0
A = [1,2,3,-3]
print(s.solve(A)) # Output: 1
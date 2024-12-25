#https://www.scaler.com/academy/mentee-dashboard/class/325294/homework/problems/4745/?navref=cl_pb_nv_tb
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # n = len(A)
        # sum_A = 0
        # for i in range(n):
        #     for j in range(n):
        #         sum_A += (A[i] % A[j])
        
        # return (sum_A % 1000000007)

        # To store the maximum element

        array_max = max(A) 
        # To store the frequency of each element
        cnt = [0 for i in range(array_max + 1)]    
        # Store the frequency of each element
        for i in A:
            cnt[i] += 1
    
        # To store the required answer
        ans = 0
    
        # For all valid pairs
        for i in range(1, array_max + 1):
            for j in range(1, array_max + 1):    
                # Update the count
                ans = ans + cnt[i] * cnt[j] * (i % j)
                ans = ans % 1000000007
    
        return ans


# You can test the code for correctness with the help of given test cases
s=Solution()
# A = [1, 2, 3]
# print(s.solve(A)) # Output: 5
# A = [1, 2, 3, 4]
# print(s.solve(A)) # Output: 20
# A = [1, 2, 3, 4, 5]
# print(s.solve(A)) # Output: 45
# A = [1, 2, 3, 4, 5, 6]
# print(s.solve(A)) # Output: 84
A = [17, 100, 11]
print(s.solve(A)) # Output: 61
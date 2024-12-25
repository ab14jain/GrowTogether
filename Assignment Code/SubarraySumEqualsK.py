class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):        
        count = 0
        prefix_sum = [0] * (len(A))
        prefix_sum[0] = A[0]

        sum_dict = {}
        for i in range(1, len(A)):
            prefix_sum[i] = prefix_sum[i-1] + A[i]

        for i in range(len(A)):
            
            if prefix_sum[i] == B:
                count += 1
            
            if prefix_sum[i] - B in sum_dict:
                count += sum_dict[prefix_sum[i] - B]

            sum_dict[prefix_sum[i]] = sum_dict.get(prefix_sum[i], 0) + 1
        return count
    
# # You can test the code for correctness with the help of given test cases
s=Solution()


A = [19,-10,-13,10,-13,6,7,2,18,-19,-4]
B = 19
print(s.solve(A, B)) # Output: 1

A = [-10,-12,-17,-4,1]
B = -14
print(s.solve(A, B)) # Output: 0
A = [1, 0, 1]
B = 1
print(s.solve(A, B)) # Output: 4

A = [0,0,0]
B = 0
print(s.solve(A, B)) # Output: 6
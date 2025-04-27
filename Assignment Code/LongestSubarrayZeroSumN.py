class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        n = len(A)
        prefix_sum = [0]*n
        prefix_sum[0] = A[0]
        seen_idx = {}
        seen_idx[prefix_sum[0]] = 0
        longest_arr_count = 0

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1]+A[i]

            if prefix_sum[i] in seen_idx:
                longest_arr_count = max(longest_arr_count, i-seen_idx[prefix_sum[i]])                

            if prefix_sum[i] == 0:
                longest_arr_count = max(longest_arr_count, i+1)
            
            seen_idx[prefix_sum[i]] = i+1


        return longest_arr_count
    

s=Solution()
# print(s.solve([1,-2,1,2]))
# print(s.solve([3,2,-1]))
# print(s.solve([6,5,-4,-2,1,-5,5]))
print(s.solve([9,-20,-11,-8,-4,2,-12,14,1]))
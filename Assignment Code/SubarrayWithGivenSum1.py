#https://www.scaler.com/academy/mentee-dashboard/class/325312/assignment/problems/4116?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        n = len(A)
        i = 0
        j = 0

        sub_sum = A[i]
        while j < n:
            
            if sub_sum == B:
                return A[i:j+1]
            elif sub_sum < B:
                j += 1
                if j == n:
                    break
                sub_sum += A[j]                
            else:
                sub_sum -= A[i]
                i += 1

        return [-1]
    

s=Solution()
print(s.solve([1,2,3,4,5],5))
print(s.solve([1,2,3,4,5],9))
print(s.solve([5,10,20,100,105],235))
#https://www.scaler.com/academy/mentee-dashboard/class/325312/assignment/problems/9323?navref=cl_tt_nv

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        i = 0
        j = 1
        n = len(A)
        A.sort()       
        pairs = set()
        while j < n and i < n:
            diff = A[j] - A[i]
            if diff == B and i != j:
                key = str(A[i]) + "#" + str(A[j])
                pairs.add(key)                
                i += 1
                j += 1                
            elif diff < B:
                j += 1
            else:
                i += 1
        
        return len(pairs)

s=Solution()
print(s.solve([1,5,3,4,2],3))
print(s.solve([8,12,16,4,0,20],4))
print(s.solve([1,1,1,2,2],0))
print(s.solve([1,2,3,4,5,6,6],0))
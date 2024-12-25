#https://www.scaler.com/academy/mentee-dashboard/class/325304/homework/problems/122783?navref=cl_tt_lst_nm
class Solution:
    # @param A : list of integers
    # @return an integer
    def getMax(self, A):
        maxA = A[0]
        n = len(A)
        def getM(A, i, maxA):
            if i == -1:
                return maxA
            
            if A[i] > maxA:
                maxA = A[i]

            return getM(A, i-1, maxA)
        
        return getM(A, n-1, maxA)
    

s=Solution()
print(s.getMax([1,2,3,4,5])) # 5
print(s.getMax([5,4,3,2,1])) # 5
print(s.getMax([5,4,3,2,5])) # 5

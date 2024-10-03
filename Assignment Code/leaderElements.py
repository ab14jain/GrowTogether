class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        leader_elemet = A[-1]
        res = []
        for i in range(len(A)-1, -1, -1):
            if A[i] >= leader_elemet:
                leader_elemet = A[i] 
                A[i] = 1   
                res.append(leader_elemet)

        return res

sol = Solution()
#print(sol.solve([16, 17, 4, 3, 5, 2])) # [17, 5, 2]    
print(sol.solve([5, 4])) # [4, 0]   


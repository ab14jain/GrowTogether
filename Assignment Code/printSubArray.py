class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        res = []
        for i in range(n):         
            res.append([A[i]])   
            temp_arr = []
            temp_arr.append(A[i])   
            for j in range(i+1, n):         
                temp_arr.append(A[j])  
                res.append(temp_arr[:])  
            

        return res
    

sol = Solution()
print(sol.solve([1, 2, 3])) # [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
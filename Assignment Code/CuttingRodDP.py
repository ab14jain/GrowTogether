class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        n = len(A)
        max_profit = float('-inf')
        def cut(rem):

            if rem <= 0:
                return 0            
            #profit = [0]*n
            p = 0
            for i in range(n):
                p = A[i] + cut(rem - i-1)
            
                nonlocal max_profit
                max_profit = max(max_profit, p)

            return max_profit

        cut(n)
        return max_profit

         
    
s=Solution()
print(s.solve([3,4,1,6,2]))
print(s.solve([1,5,2,5,6]))
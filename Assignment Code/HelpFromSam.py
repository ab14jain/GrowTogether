#https://www.scaler.com/academy/mentee-dashboard/class/313152/homework/problems/4531?navref=cl_tt_nv
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        take_help = 1 if A % 2 == 1 else 0
        if A == 0:
            return 0        
        else:
            while A > 0:  
                if A % 2 == 1:
                    take_help += 1
                A = A >> 2
        
        return take_help
    

# Driver code
s = Solution()
print(s.solve(5)) # 3
print(s.solve(6)) # 2
print(s.solve(7)) # 2
print(s.solve(16)) # 3
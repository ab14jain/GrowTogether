#https://www.scaler.com/academy/mentee-dashboard/class/313168/assignment/problems/35183?navref=cl_tt_nv
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        XOR_sum = 0
        for i in range(32):
            set_bit = 0
            unset_bit = 0
            for j in A:
                if j == (j | (1 << i)):
                    set_bit += 1
                else:
                    unset_bit += 1
            
            power = 1<<i
            calc = set_bit * unset_bit*power
            XOR_sum = XOR_sum + calc

        XOR_sum = XOR_sum % (10**9+7)
        
        return XOR_sum


# Driver code
s = Solution()
print(s.solve([1, 3, 5])) # 12
print(s.solve([1, 2, 3])) # 6
print(s.solve([1, 2, 3, 4, 5])) # 42
print(s.solve([1, 2, 3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])) # 1008
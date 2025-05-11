#https://www.scaler.com/academy/mentee-dashboard/class/325344/homework/problems/4669?navref=cl_tt_nv

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        min_coins = 0

        def get_min_coins(price):

            if price <= 0:
                return
            count = 0
            num = 5**count
            while num <= price:
                count += 1
                num = 5**count

            nonlocal min_coins
            min_coins += 1
            if count > 0:
                return get_min_coins(price - 5**(count-1))
            else:
                return get_min_coins(price - 1)

            
        get_min_coins(A)
        return min_coins
    
s=Solution()
print(s.solve(35))
print(s.solve(47))
print(s.solve(9))
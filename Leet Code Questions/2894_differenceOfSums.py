class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        # Approach 1 - Brute Force
        # sum_div_by_m = 0
        # sum_not_div_by_m = 0

        # for i in range(1, n+1):
        #     if i % m == 0:
        #        sum_div_by_m += i
        #     else:
        #         sum_not_div_by_m += i

        # return sum_not_div_by_m-sum_div_by_m


        t_sum = (n*(n+1))//2
        k = n//m
        m_div_sum = (k*(2*m+(k-1)*m))//2

        return t_sum - 2*m_div_sum

s=Solution()
print(s.differenceOfSums(10,3))
print(s.differenceOfSums(5,6))
print(s.differenceOfSums(5,1))


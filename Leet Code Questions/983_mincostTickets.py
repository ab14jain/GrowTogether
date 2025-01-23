class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0] * (days[-1] + 1)
        def calculate_cost(pos, last_day):
            if pos > len(days) - 1:
                return 0
            
            if last_day >= days[pos]:
                return calculate_cost(pos + 1, last_day)
            
            if dp[days[pos]]:
                return dp[days[pos]]

            d1_pass = costs[0] + calculate_cost(pos + 1, days[pos])
            d7_pass = costs[1] + calculate_cost(pos + 1, days[pos] + 6)
            d30_pass = costs[2] + calculate_cost(pos + 1, days[pos] + 29)
            
            min_cost = min(d1_pass, d7_pass, d30_pass)
            dp[days[pos]] = min_cost
            return min_cost


        d1_pass = costs[0] + calculate_cost(0, days[0])
        d7_pass = costs[1] + calculate_cost(0, days[0] + 6)
        d30_pass = costs[2] + calculate_cost(0, days[0] + 29)

        return min(d1_pass, d7_pass, d30_pass)
    

s=Solution()
print(s.mincostTickets([7,8,20,40], [6,7,13])) # 19
print(s.mincostTickets([1,4,6,7,8,20], [2,7,15])) # 11
print(s.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])) #17
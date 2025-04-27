class Solution:
    def minimumCost(self, prices):
        # code here


        remaining = 0
        n = len(prices)
        cost = 0
        for i in range(n):

            if remaining == 0:
                cost += prices[i]
                remaining = max(remaining, prices[i])
            else:
                if prices[i] <= remaining:
                    remaining -= prices[i]
                else:
                    cost += prices[i]
                    remaining = max(remaining, prices[i])

        return cost
s=Solution()
print(s.minimumCost([2,3,2]))
print(s.minimumCost([2,3,2,2]))
print(s.minimumCost([1]))

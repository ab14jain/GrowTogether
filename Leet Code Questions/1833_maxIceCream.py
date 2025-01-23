from typing import Counter


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:

        counter = Counter(costs)
        n = len(costs)
        sorted_costs = []

        counter = sorted(counter.items(), key=lambda x: x[0])

        for cost, freq in counter:
            sorted_costs.extend([cost]*freq)
        
        count = 0
        while coins > -1 and count < n:
            coins -= sorted_costs[count]
            if coins >= 0:
                count += 1

        return count


s=Solution()
print(s.maxIceCream([1,3,2,4,2], 7)) # 4
print(s.maxIceCream([10,6,8,7,7,8], 5)) # 0
print(s.maxIceCream([1,6,3,1,2,5], 20)) # 6


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        stock_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < stock_price:
                stock_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - stock_price)  

        return max_profit              
        # =========================Time complexity: O(n) - Wrong Answer===============
        # minP = prices[0]
        # index = 0
        # for i, p in enumerate(prices):
        #     if minP > p:
        #         minP = p
        #         index = i

        # if index == len(prices) - 1:
        #     return 0
        # else:
        #     maxP = prices[index + 1]
        #     for j in range(index + 1, len(prices)):
        #         if maxP < prices[j]:
        #             maxP = prices[j]
            
        #     return maxP - minP
        
        # =========================Time complexity: O(n) - Wrong Answer===============
        
        
        # =======================Time complexity: O(n^2) ---- TLE=====================
        # for i in range(0, len(prices)):
        #     currentMax = -1000000
        #     for j in range(i+1, len(prices)):                
        #         currentMax = max(currentMax, prices[j] - prices[i])
            
        #     prices[i] = currentMax

        # return max(prices)
        # =======================Time complexity: O(n^2) ---- TLE=====================

# Test
#prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
prices = [2,4,1]

solution = Solution()
print(solution.maxProfit(prices))  # 5


#https://www.geeksforgeeks.org/problems/stock-buy-and-sell2615/1
class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        # total_profit = 0
        # max_profit = 0
        # buy_price = float('inf')
        # sell_price = 0
        # n = len(prices)
        # i = 0
        # current_profit = 0
        # while i < n:
        #     if prices[i] < buy_price:
        #         buy_price = prices[i]
        #         total_profit += max_profit
        #         max_profit = 0
        #     else:
        #         # if (prices[i] - buy_price) > current_profit:
        #         #     max_profit += prices[i] - buy_price
        #         #     current_profit = 0
        #         #     buy_price = float('inf')
        #         # max_profit = max(max_profit, prices[i] - buy_price)

        #         max_profit = max(max_profit, prices[i] - buy_price)

        #     #     if sell_price > 0:
        #     #         max_profit = max(max_profit, sell_price - buy_price)
        #     #         sell_price = 0
            
        #     # if prices[i] > buy_price:
        #     #     sell_price = prices[i]            

            
            
            
        #     i += 1

        
        # return total_profit + max_profit

        n = len(prices)
        total_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
            
        return total_profit
    
s=Solution()
print(s.maximumProfit([100, 180, 260, 310, 40, 535, 695])) #5
print(s.maximumProfit([7,1,5,3,6,4])) #5
print(s.maximumProfit([7,6,4,3,1])) #0
print(s.maximumProfit([1,2])) #1
print(s.maximumProfit([2,1])) #0


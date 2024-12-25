class Solution:
    def maximumProfit(self, prices):
        # code here
        max_profit = 0
        buy_price = float('inf')
        i = 0
        n = len(prices) 
        while i < n:

            if buy_price > prices[i]:
                buy_price = prices[i]

            max_profit = max(max_profit, prices[i] - buy_price)
            i += 1
        
        return max_profit
    
s=Solution()
print(s.maximumProfit([100, 180, 260, 310, 40, 535, 695])) #655
print(s.maximumProfit([7,1,5,3,6,4])) #5
print(s.maximumProfit([7,6,4,3,1])) #0
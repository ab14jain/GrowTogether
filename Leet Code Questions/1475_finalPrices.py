class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:

        # Approach 1: Brute Force
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if prices[j] <= prices[i]:
        #             prices[i] -= prices[j]
        #             break
        
        # return prices

        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
    
        # Approach 2: Stack
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices
    
        # Time Complexity: O(n)
        # Space Complexity: O(n)

    
s= Solution()
print(s.finalPrices([8,4,6,2,3])) # [4,2,4,2,3]
print(s.finalPrices([1,2,3,4,5])) # [1,2,3,4,5]
print(s.finalPrices([10,1,1,6])) # [9,0,1,6]
        
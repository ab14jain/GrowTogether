class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0:
                    if len(flowerbed) == 1 or flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i > 0 and i < len(flowerbed) - 2:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -= 1
        
        return n <= 0
    
test = Solution()
print(test.canPlaceFlowers([1,0,0,0,1], 1)) # True
print(test.canPlaceFlowers([1,0,0,0,1], 2)) # False
print(test.canPlaceFlowers([0,0,1,0,0], 1)) # True
print(test.canPlaceFlowers([0,0,1,0,0], 2)) # True
print(test.canPlaceFlowers([0,0,0,0,0], 4)) # True

                

            
            



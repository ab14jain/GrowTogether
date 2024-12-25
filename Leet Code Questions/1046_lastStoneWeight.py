class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        
        stones.sort()
        while stones:            
            x = stones.pop()
            y = stones.pop()
            result = abs(x-y)
            if result > 0:
                stones.append(result)
            
            if n == 1:
                break
        
        if n == 0:
            return 0
        else:
            return stones[0]
    

s= Solution()

print(s.lastStoneWeight([2,7,4,1,8,1])) # 1
print(s.lastStoneWeight([2,2])) # 0
print(s.lastStoneWeight([1,3])) # 2
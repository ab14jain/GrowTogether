class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        ways = 0
        for i in range(limit+1):
            for j in range(limit+1):
                rem = n - i - j

                if rem >= 0 and rem <= limit:
                    ways += 1
                
                    print(i,j,rem)

        return ways

s=Solution()
print(s.distributeCandies(10001,20001))
# print(s.distributeCandies(5,2))
# print(s.distributeCandies(3,3))

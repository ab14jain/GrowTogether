
class Solution:
    def maximizeHealth(self, n : int, A : list[int], B : list[int], x : int, y : int) -> int:
        
        window_a = x
        window_b = y

        max_health = 0
        for i in range(n):
            health = 0
            for j in range(i, i + window_a):
                if j < n:
                    health += A[j]
            for j in range(i, i + window_b):
                if j < n:
                    health += B[j]
            max_health = max(max_health, health)
        
        return max_health
    

s = Solution()

print(s.maximizeHealth(5, [5, -1, -3, -2, 1], [-2, 1, 5, 4, 2], 2, 2)) # 2

#[5, -1, -3, -2, 1], 
#[-2, 1, 5, 4, 2]
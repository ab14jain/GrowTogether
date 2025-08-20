class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        p = [0.0]*(n+1)
        p[0] = 1

        for i in range(1, n+1):
            for j in range(1, maxPts+1):
                if (i-j)>=0 and (i-j) < k:
                    p[i] += p[i-j]*(1/maxPts)

        ans = 0

        for i in range(k, n+1):
            ans += p[i]

        return round(ans,5)

s=Solution()
print(s.new21Game(n = 21, k = 17, maxPts = 10))
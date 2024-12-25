class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0 or n == 1:
            return 0
        
        isPrimes = [True for _ in range(n)]

        isPrimes[0] = False
        isPrimes[1] = False
        
        
        i = 2
        for i in range(i, n, 1):
            if isPrimes[i]:
                x = i*i
                for j in range(x,n,i):
                   isPrimes[j] = False
        count = 0

        for i in range(2,n):
            if isPrimes[i]:
                count += 1

        return count
        


s= Solution()
print(s.countPrimes(996)) # 4
print(s.countPrimes(997)) # 4
print(s.countPrimes(998)) # 4
# print(s.countPrimes(10)) # 4
# print(s.countPrimes(0)) # 0
# print(s.countPrimes(1)) # 0
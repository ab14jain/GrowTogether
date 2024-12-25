class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:

        n = len(nums)
        primes = [True]*1000

        primes[0] = False
        primes[1] = False

        x = 2
        while x * x < 1000:
            if primes[x]:
                y = x * x
                while y < 1000:
                   primes[y] = False
                   y += x
            
            x += 1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                continue

            for p in range(2, nums[i]):
                if not primes[p]:
                    continue
                
                if (nums[i]-p) < nums[i+1]:
                    nums[i] -= p
                    break
                
            if nums[i] >= nums[i+1]:
                return False
        
        return True
    

s= Solution()
print(s.primeSubOperation([4])) # True
print(s.primeSubOperation([4,9,6,10])) # True
print(s.primeSubOperation([6,8,11,12])) # True
print(s.primeSubOperation([5,8,3])) # False
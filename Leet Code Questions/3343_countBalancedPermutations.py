class Solution:
    MOD = 10**9 + 7
    
    def mod_multiply(self, a, b):
        return (a % self.MOD) * (b % self.MOD) % self.MOD
    
    def compute_factorial(self, n):
        self.fact = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fact[i] = self.mod_multiply(self.fact[i - 1], i)
    
    def binary_exponentiation(self, a, b):
        res = 1
        while b > 0:
            if b & 1:
                res = self.mod_multiply(res, a)
            a = self.mod_multiply(a, a)
            b >>= 1
        return res
    
    def compute_inverseFactorial(self, n):
        self.inverse_fact = [1] * (n + 1)
        for i in range(n + 1):
            self.inverse_fact[i] = self.binary_exponentiation(self.fact[i], self.MOD - 2)
    
    def count_permutation(self, digit, leftover, target):
        if digit == 10:
            return self.tot_ways_to_permute if (leftover == 0 and target == 0) else 0
        if self.mem[digit][leftover][target] != -1:
            return self.mem[digit][leftover][target]
        
        include_count = min(leftover, self.freq[digit])
        if digit > 0:
            include_count = min(include_count, target // digit)
        
        ans = 0
        for i in range(include_count + 1):
            ways_for_current_digit = self.mod_multiply(self.inverse_fact[i], self.inverse_fact[self.freq[digit] - i])
            ans += ways_for_current_digit * self.count_permutation(digit + 1, leftover - i, target - digit * i)
            ans %= self.MOD
        self.mem[digit][leftover][target] = ans
        return ans
    
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        sum_digits = 0
        self.freq = [0] * 10
        for ch in num:
            digit = int(ch)
            sum_digits += digit
            self.freq[digit] += 1
        
        if sum_digits % 2 == 1:
            return 0
        
        target = sum_digits // 2
        self.compute_factorial(n)
        self.compute_inverseFactorial(n)
        
        half_len = n // 2
        self.tot_ways_to_permute = self.mod_multiply(self.fact[half_len], self.fact[n - half_len])
        
        
        max_sum = 42 * 9 
        self.mem = [[[-1] * (max_sum + 1) for _ in range(half_len + 1)] for _ in range(10)]
        
        return self.count_permutation(0, half_len, target)
        
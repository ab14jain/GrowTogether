class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:

        xor_sum = 0
        n = len(derived)
        for i in range(n):
            if i < n-1:
                xor_sum ^= derived[i] ^ derived[i+1]
            else:
                xor_sum ^= derived[i] ^ derived[0]
                
        if xor_sum == 0:
            return True
        
        return False
    

s=Solution()
print(s.doesValidArrayExist([1,1,0])) # True
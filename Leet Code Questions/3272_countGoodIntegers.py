from itertools import permutations
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        def isPalindrome(num):
            
            n = len(num)
            i = 0
            j = n-1
            
            while i <= j:
                if num[i] != num[j]:
                    return False
                
                i += 1
                j -= 1

            return True


        st = ""

        for i in range(1,n+1):
            st += str(i)
        perms = [''.join(p) for p in permutations(st)]

        count = 0
        for perm in perms:
            print(perm)
            if int(perm) % k == 0 and isPalindrome(perm):
                count += 1

        return count
        


s=Solution()
print(s.countGoodIntegers(3,5))
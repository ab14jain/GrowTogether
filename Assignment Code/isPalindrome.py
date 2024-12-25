import sys
sys.setrecursionlimit(50011)
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):        
        # print(sys.getrecursionlimit())
        def isPalindrome(A, s, e):
            if s > e:
                return 1
            
            if A[s] != A[e]:
                return 0

            return isPalindrome(A, s+1, e-1)
        
        return isPalindrome(A, 0, len(A)-1)

        # i = 0
        # j = len(A)-1

        # while i < j:
        #     if A[i] != A[j]:
        #         return 0
            
        #     i += 1
        #     j -= 1
        
        # return 1
    
# Time complexity: O(n)
s=Solution()
# print(s.solve("racecar")) # 1
# print(s.solve("racecars")) # 0
# print(s.solve("a")) # 1
# print(s.solve("ab")) # 0
# print(s.solve("aba")) # 1

#generate 5000 characters palindrome
import random
import string
import time
n = 50000
stri = ''.join(random.choices(string.ascii_lowercase, k=n))
stri = stri+ stri[::-1]
start = time.time()
print(s.solve(stri)) # 1

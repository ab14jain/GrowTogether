class Solution:
    def binary_search(self,l,m,r,num):
        guess_n = guess(num)
        if guess_n == -1:
            r = m
            m = (l + r)//2
            self.binary_search(l,m,r,m)
        elif guess_n == 1: 
            l = m
            m = (l + r)//2
            self.binary_search(l,m,r,m)
        else:
            return m

    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = (left + right)//2

        return self.binary_search(left,mid,right,6)
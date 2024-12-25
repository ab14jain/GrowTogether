class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        print(2**30)
        if num < 1:
            return False
        s = 1
        e = num
        mid = (e - s)//2
        
        while s <= e:
            mid = s + (e - s)//2
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                e = mid - 1                
            elif sq < num:
                s = mid + 1
        
        return False
            

s= Solution()
print(s.isPerfectSquare(16)) # True
print(s.isPerfectSquare(14)) # False
print(s.isPerfectSquare(1)) # True
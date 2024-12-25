#https://practice.geeksforgeeks.org/contest/gfg-weekly-184-rated-contest/problems

import math


class Solution:

    def minimumJump(self, points):
        # code here
        n = len(points)

        def is_perfect_square(n):
            if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
                return True
            else:
                return False
        
        i = 0
        j = n - 1

        while i < n:

            if is_perfect_square(points[i]):
                break
            i += 1
        
        while j > i:
            if is_perfect_square(points[j]):
                break
            j -= 1

        if i == n or i == j:
            return n - 1
        else:
            return n - j + i

s=Solution()
# points = [1,3,5,8,9,2,6,7,6,8,9]
# points = [2, 4, 16, 64, 65]
# points = [1, 2,3]
# points = [9, 41, 60, 27, 42, 69, 29, 56]
# points = [1, 4, 3, 2, 6, 7]
points = "54 14 56 61 73 57 86 68 48"
print(s.minimumJump(list(map(int,points.split(" "))))) #3
# points = [1,4,3,2,6,7]
# print(s.minimumJump(points)) #5
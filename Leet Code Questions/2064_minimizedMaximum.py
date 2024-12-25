class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        max_quantity = max(quantities)

        def canDistriibute(q, m, n):
            for i in q:
                n -= (i + m - 1) // m

                print(m,n)

            return n >= 0

        l = 1
        r = max_quantity
        m = (l+r)//2
        ans = max_quantity
        while l <= r:
            m = l + (r-l)//2

            if canDistriibute(quantities[:], m, n):
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1

        return ans
    

s= Solution()
print(s.minimizedMaximum(6, [11,6])) # 3
# print(s.minimizedMaximum(4, [1,2,3,4])) # 3
# print(s.minimizedMaximum(4, [1,2,3,4,5])) # 4
# print(s.minimizedMaximum(4, [1,2,3,4,5,6])) # 5
# print(s.minimizedMaximum(4, [1,2,3,4,5,6,7])) # 6
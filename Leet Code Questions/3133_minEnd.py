class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # last_number = x
        # for i in range(1, n):
        #     last_number = (last_number + 1) | x

        # return last_number

        left_shift = []
        curr = x
        range_x = n - 1

        for i in range(32):
            if not (curr & (1 << i)):
                left_shift.append(i)

        for i in range(32,64):
            left_shift.append(i)

        i = 0
        while range_x:
            if range_x & 1:
                curr |= 1 << left_shift[i]
            i += 1
            range_x >>= 1

        return curr

s= Solution()
print(s.minEnd(69735293, 5563569)) # [2, 5]
print(s.minEnd(2, 7)) # [2]
print(s.minEnd(3, 4)) # [2]
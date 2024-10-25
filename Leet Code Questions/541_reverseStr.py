import math


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        str_arr = list(s)        
        n = len(s)
        times = math.ceil(n / (2 * k))
        x_times = 0
        if k > n:
            str_arr.reverse()
            return "".join(str_arr)
        while x_times < times:
            l = 0 + (x_times * 2 * k)
            r = min(l + k - 1, n - 1)
            while l < r and l < n and r < n:
                temp = str_arr[l]
                str_arr[l] = str_arr[r]
                str_arr[r] = temp
                l += 1
                r -= 1
            x_times += 1

        return "".join(str_arr)
    

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the length of the input string s

s = Solution()
# print(s.reverseStr("abcdefg", 2)) # "bacdfeg"
# print(s.reverseStr("abcd", 2)) # "bacd"
# print(s.reverseStr("abc", 2)) # "bac"
# print(s.reverseStr("a", 2)) # "a"
# print(s.reverseStr("abcdefg", 8)) # "gfedcba"
# print(s.reverseStr("abcdefg", 1)) # "abcdefg"
# print(s.reverseStr("abcdefg", 7)) # "gfedcba"
# print(s.reverseStr("abcdefg", 3)) # "cbadefg"
print(s.reverseStr("abcdefghijklmnopqrstuvwxyz", 3)) # "cbadefihgjklonmpqrutsvwxzy"
print(s.reverseStr("abcdefghijklmnopqrstuvwxyzaabcd", 3)) # "cbadefihgjklonmpqrutsvwxzy"
# print(s.reverseStr("abcdefghijklmnopqrstuvwxyz", 4)) # "dcbaefghlkjimnoptsrquvwxzy"
class Solution:
    def addDigits(self, num: int) -> int:

        str_num = list(str(num))
        result = 0
        for i in str_num:
            result += int(i)

            if result > 9:
                result = int(list(str(result))[0]) + int(list(str(result))[1])
        
        return result


s = Solution()
print(s.addDigits(38))
print(s.addDigits(0))
print(s.addDigits(1234))
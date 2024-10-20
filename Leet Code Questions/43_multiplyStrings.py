class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res = []
        sum = 0       
        for i in range(len(num2) - 1, -1, -1):
            carry = 0
            res = ""      

            for j in num1[::-1]:
                temp = int(j) * int(num2[i]) + carry
                carry = temp // 10
                res += str(temp % 10)

            res = res[::-1]
            for l in range(len(num2) - 1 - i):
                res += "0"                
            sum += int(res)
            #print(res)

        return sum

s = Solution()
# print(s.multiply("123", "456")) # 56088
# write test case for large number multiplication
print(s.multiply("123456789", "987654321")) # 121932631112635269
print(s.multiply("498828660196", "840477629533")) # 419254329864656431168468
print(s.multiply("6913259244", "71103343")) # 491555843274052


                
    
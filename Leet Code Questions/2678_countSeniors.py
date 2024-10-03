class Solution:
    def countSeniors(self, details: list[str]) -> int:

        seniorCitizen = 0
        for detail in details:
            age = detail[11] + detail[12]

            if int(age) > 60:
                seniorCitizen += 1
        
        return seniorCitizen

# Test cases
s = Solution()
print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))  # 1
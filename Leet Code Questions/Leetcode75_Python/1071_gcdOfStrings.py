class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""

        if len(str1) > len(str2):
            substr = ""
            for index, i in enumerate(str2):
                substr = str2[:(index + 1)]
                tempsubstr = [substr] * (len(str2) - index)
                print(tempsubstr)
                if tempsubstr == str2:
                    print(tempsubstr)
        
        return str1.find(str2)
    

# Test cases
test = Solution()

# print(test.gcdOfStrings("ABCABC", "ABC"))
print(test.gcdOfStrings("ABABAB", "ABAB"))
# print(test.gcdOfStrings("LEET", "CODE"))
# print(test.gcdOfStrings("ABCDEF", "ABC"))
# print(test.gcdOfStrings("ABC", "ABCDEF"))

# assert test.gcdOfStrings("ABCABC", "ABC") == "ABC"
# assert test.gcdOfStrings("ABABAB", "ABAB") == "AB"
# assert test.gcdOfStrings("LEET", "CODE") == ""
# assert test.gcdOfStrings("ABCDEF", "ABC") == ""
# assert test.gcdOfStrings("ABC", "ABCDEF") == ""
# print('All tests passed')
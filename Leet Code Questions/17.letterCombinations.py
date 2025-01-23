class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        hash_map = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"            
        }

        if not digits:
            return []

        result = []  
        def backtrack(idx, path):
            if idx == len(digits):
                result.append(path)
                return
            
            for letter in hash_map[int(digits[idx])]:
                backtrack(idx+1, path+letter)

        backtrack(0, "")
        return result
    

        #           1
        #         /   \
        #        2      3
        #       / \    / 
        #      4  5   6   
        #
        #

s=Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations("234"))
print(s.letterCombinations("2345"))
print(s.letterCombinations("23456"))
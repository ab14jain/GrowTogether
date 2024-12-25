class Solution:
    def detectCapitalUse(self, word: str) -> bool: 
        n = len(word)        
        first_letter = ord(word[0])
        if first_letter >= 65 and first_letter <= 90:
            i = 1           
            has_small = False 
            has_capital = False
            while i < n:
                next_letter = ord(word[i])
                # print(word[i])               
                if next_letter >= 65 and next_letter <= 90:                   
                    i += 1
                    has_capital = True
                    if has_small:
                        return False
                    continue
                else:
                    if next_letter >= 97 and next_letter <= 122:
                        i += 1 
                        has_small = True
                        
                        if has_capital:
                            return False
                        continue
                    else: 
                        return False
                i += 1 
        else:
            i =  1
            while i < n:
                next_letter = ord(word[i])
                if not (next_letter >= 97 and next_letter <= 122)  :                  
                    return False
                i += 1
        

        return True


s = Solution()
print(s.detectCapitalUse('ERTERTERERTERTERTRHs')) # False
# print(s.detectCapitalUse('USA')) # True
# print(s.detectCapitalUse('leetcode')) # True
# print(s.detectCapitalUse('Google')) # True
# print(s.detectCapitalUse('FlaG')) # False
# print(s.detectCapitalUse('Flag')) # True
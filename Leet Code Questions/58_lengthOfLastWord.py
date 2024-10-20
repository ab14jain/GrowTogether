class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # sol 1 - using split
        # n = len(s)
        # i = 0
        # last_word_array = []
        # last_word_count = 0
        # while i < n:
        #     if s[i] != ' ':
        #         last_word_array.append(s[i])
        #     else:
        #         if len(last_word_array) > 0:
        #             #last_word = ("".join(last_word_array))
        #             last_word_count = len(last_word_array)
        #         last_word_array = []

        #     i += 1
        
        # #in case of the last word is the last word in the string
        # if len(last_word_array) > 0:
        #     last_word_count = len(last_word_array)
        # return last_word_count

        # sol 2 - better soltion traverse the string from the end
        n = len(s)
        i = n - 1
        last_word_count = 0
        while i >= 0:
            if s[i] == ' ':
                if last_word_count > 0:
                    return last_word_count
            else:
                last_word_count += 1
            i -= 1
        
        return last_word_count

s = Solution()

print(s.lengthOfLastWord("S")) # 1
print(s.lengthOfLastWord("   fly me   to   the moon  ")) # 4
print(s.lengthOfLastWord("Hello")) # 5
print(s.lengthOfLastWord("Hello World ")) # 5
print(s.lengthOfLastWord("Hello World  ")) # 5
print(s.lengthOfLastWord(" luffy is still joyboy   ")) # 5
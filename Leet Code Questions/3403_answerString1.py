class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        if numFriends == 1:
            return word
        n = len(word)
        lexi_len = n-numFriends+1
        
        # lexi_char_idx = 0
        # for i in range(1, n):
        #     if word[lexi_char_idx] < word[i]:
        #         lexi_char_idx = i
        
        # if lexi_len == 1:
        #     return word[lexi_char_idx]
        # return word[lexi_char_idx:lexi_char_idx+lexi_len]
        
        box = set()
        for i in range(n):
            sb_str = word[i:i+lexi_len]

            box.add(sb_str)

        return max(box)
    

s=Solution()
print(s.answerString("dfsfsfsdfsferweretghfngncsdf", 4))
print(s.answerString("dbca", 2))
print(s.answerString("gggg", 4))
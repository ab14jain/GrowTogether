class Solution:
    def answerString(self, word: str, numFriends: int) -> str:        
        
        if numFriends == 1:
            return word
        
        n = len(word)        
        box = set()
        sub_str_size = n - numFriends + 1
        for i in range(n):
            sub_str = word[i:i + sub_str_size]           
            box.add(sub_str)           
                
        return max(box)

        # n = len(word)
        # m = n - numFriends + 1
        # if numFriends == 1:
        #     return word

        # ans = [word[i:i + m] for i in range(n)]
        # return max(word[i:i + m] for i in range(n))
    
s=Solution()
# print(s.answerString("abacabadabacaba", 7)) # abacaba
# print(s.answerString("abacabadabacaba", 3)) # abac
# print(s.answerString("abacabadabacaba", 5)) # abacab
# print(s.answerString("abacabadabacaba", 2)) # ab
# print(s.answerString("abacabadabacaba", 1)) # a
print(s.answerString("aann", 2)) # dbc
print(s.answerString("dbca", 2)) # dbc
print(s.answerString("gggg", 4)) # g
print(s.answerString("abcd", 4)) # d
print(s.answerString("a", 1)) # d
            
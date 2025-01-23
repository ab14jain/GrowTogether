class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        n = len(s)
        freq = {}

        for i in range(n):
            if s[i] in freq:
                freq[s[i]][-1] = i
            else:
                freq[s[i]] = [i,i]

        result = 0
        for char in freq:

            start = freq[char][0]
            end = freq[char][1]
            char_set = set()
            for i in range(start+1,end):
                char_set.add(s[i])
            
            result += len(char_set)
        return result


s=Solution()
print(s.countPalindromicSubsequence("aabca")) # 3
print(s.countPalindromicSubsequence("abcabdcca")) # 10
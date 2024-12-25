class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        seen = '*'
        mapping = [[-1]*3 for _ in range(26)]
        count = 0
        for i in range(n):
            if s[i] == seen:
                count += 1
            else:
                count = 1
                seen = s[i]
                
            idx = ord(s[i])-97
            occurences = mapping[idx]
            min_val = min(occurences) 
            index_of_min = occurences.index(min_val)

            if count > min_val:
                occurences[index_of_min] = count
                mapping[idx] = occurences[:]
        
        max_len = -1
        for i in range(26):
            max_len = max(max_len, min(mapping[i]))

        return max_len

s = Solution()
print(s.maximumLength("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # 1
print(s.maximumLength("aaaa")) # 2
print(s.maximumLength("abac")) # -1
print(s.maximumLength("aa")) # -1
print(s.maximumLength("aaaaaabbbbcccccccaaaabbbcaaaabbbccc")) # 5
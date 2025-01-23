class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        
        hasVowel = []
        n = len(words)
        for i in range(n):
            first = words[i][0]
            last = words[i][-1]
            if first in "aeiou" and last in "aeiou":
                hasVowel.append(1)
            else:
                hasVowel.append(0)
        
        prefix_sum = [0] * n

        for i in range(n):
            if i == 0:
                prefix_sum[i] = hasVowel[i]
            else:
                prefix_sum[i] = prefix_sum[i - 1] + hasVowel[i]
        
        result = []

        for i in queries:
            left = i[0]
            right = i[1]
            if left == 0:
                result.append(prefix_sum[right])
            else:
                result.append(prefix_sum[right] - prefix_sum[left - 1])

        return result
    
s=Solution()

print(s.vowelStrings(["apple", "orange", "banana", "pear"], [[0, 2], [1, 3]])) # [1, 0]
print(s.vowelStrings(["apple", "orange", "banana", "pear"], [[0, 3], [1, 2]])) # [1, 1]
print(s.vowelStrings(["apple", "orange", "banana", "pear"], [[0, 0], [1, 1]])) # [1, 1]

    
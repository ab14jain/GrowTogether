class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        
        word_map = {}        
        n = len(words)
        for i in range(n):
            if words[i] in word_map:
                word_map[words[i]] += 1                
            else: 
                word_map[words[i]] = 1
        
        # for i in word_map:
        #     print(i, -word_map[i])
        
        return sorted(word_map, key=lambda x: (-word_map[x], x))[:k]  


s=Solution()
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)) # ["i", "love"]
print(s.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))


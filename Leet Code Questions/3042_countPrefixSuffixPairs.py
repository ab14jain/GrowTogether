class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:

        # Time complexity: O(n^2)*O(m) = O(n^2*m)
        # Space complexity: O(1)

        # def isPrefixAndSuffix(str1, str2):
        #     if len(str1) > len(str2):
        #         return False
        #     return str2.startswith(str1) and str2.endswith(str1)

        # count = 0
        # n = len(words)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if isPrefixAndSuffix(words[i], words[j]):
        #             count += 1
                
        # return count

        # Using Trie Data structure
        # Time complexity: O(n*m)
        # Space complexity: O(n*m)

        class TrieNode:
            def __init__(self):
                self.children = [None]*26
                self.isEnd = False
                

            def insert(root, word): 
                node = root
                for char in word:
                    idx = ord(char) - ord('a')
                    if node.children[idx] is None:
                        node.children[idx] = TrieNode()
                    node = node.children[idx]
                node.isEnd = True
            
            

        root = TrieNode()
        count = 0
        for word in words:
            TrieNode.insert(root, word)
        

        print(root.children)

        
    

s=Solution()
print(s.countPrefixSuffixPairs(["a","aba","ababa","aa"]))
print(s.countPrefixSuffixPairs(["pa","papa","ma","mama"]))
print(s.countPrefixSuffixPairs(["abab","ab"]))
print(s.countPrefixSuffixPairs(["abcd","cdef","efgh","ghab"]))
print(s.countPrefixSuffixPairs(["abcd","cdef","efgh","ghab","habc"]))
print(s.countPrefixSuffixPairs(["abcd","cdef","efgh","ghab","habc","abcd"]))
                
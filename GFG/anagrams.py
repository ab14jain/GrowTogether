#https://www.geeksforgeeks.org/problems/print-anagrams-together/1

class Solution:
    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        result = []
        sorted_map = {}
        
        for i in range(len(arr)):
            s = arr[i]           
            s = ''.join(sorted(s))
            if s not in sorted_map:
                sorted_map[s] = len(result)
                result.append([])            
            
            result[sorted_map[s]].append(arr[i])
        
        return result

# Time Complexity: O(N * M * log M), where N is the number of words and M is the maximum length of a word.
# Space Complexity: O(N * M).
# Driver code
s=Solution()
print(s.anagrams(["act","god","cat","dog","tac"]))
print(s.anagrams(["act","god","cat","dog","tac","god","god"]))
print(s.anagrams(["act","god","cat","dog","tac","god","god","dog"]))
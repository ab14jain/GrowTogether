from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        

        # result = []
        # n = len(groups)
        # for i in range(n):
        #     temp = [i]
        #     curr = groups[i]
        #     for j in range(i, n):
        #         if curr != groups[j]:
        #             temp.append(j)
        #             curr = groups[j]
            
        #     if len(result) < len(temp):
        #         result = temp[:]

        # ans = []

        # for i in result:
        #     ans.append(words[i])

        # return ans


        # def recur():

        
        # n = len(groups)
        # ans = [words[0]]
        # curr = groups[0]
        # for i in range(n):            
        #     if curr != groups[i]:
        #         ans.append(words[i])
        #         curr = groups[i]
                    
        # return ans

        

    
s=Solution()
print(s.getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1]))
print(s.getLongestSubsequence( words = ["a","b","c","d"], groups = [1,0,1,1]))
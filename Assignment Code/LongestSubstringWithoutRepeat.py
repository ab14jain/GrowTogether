class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):

            # Initialize the dictionary to store the last seen index of the character
            char_set = set()
            max_length = 0
            start = 0
            count = 0
            for i in range(len(A)):
                if A[i] not in char_set:
                    count += 1
                else:
                    while A[start] != A[i]:
                        char_set.remove(A[start])
                        start += 1
                        
                    start += 1
                    count = i - start + 1
                    max_length = max(max_length, count)

                char_set.add(A[i])
                

            return max_length


#abcabcbb

s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # Output: 3
     
class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):        
            j = 0
            res = []
            A.sort()

            n = len(A)
            isTrue = True
            tempchar = A[0][0]

            min_length = len(A[0])

            for i in range(n):
                min_length = min(min_length, len(A[i]))

            while j < min_length:
                tempchar = A[0][j]
                for i in range(n):                    
                    if tempchar != A[i][j]:
                        isTrue = False   
                        break                           

                if isTrue:   
                    res.append(tempchar)
                j += 1


            return "".join(res)


# Test cases
s = Solution()
#print(s.longestCommonPrefix(["abab", "ab", "abcd"])) # ab
# print(s.longestCommonPrefix(["abcd","abcd","efgh"])) # 
print(s.longestCommonPrefix(["abcdefgh","aefghijk","abcefgh"])) # ab

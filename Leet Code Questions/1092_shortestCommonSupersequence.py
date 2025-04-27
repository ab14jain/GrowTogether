class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        # memo = {}
        # def backtrack(i, j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]

        #     if i == len(str1):
        #         return str2[j:]

        #     if j == len(str2):
        #         return str1[i:]

        #     if str1[i] == str2[j]:
        #         return str1[i] + backtrack(i+1,j+1)

        #     result1 = str1[i] + backtrack(i+1, j)
        #     result2 = str2[j] + backtrack(i, j+1)

        #     if len(result1) < len(result2):
        #         memo[(i,j)] = result1
        #         return result1

            
        #     memo[(i,j)] = result2

        #     return result2

        # return backtrack(0, 0)

        n = len(str1)
        m = len(str2)

        prev = [str2[j:] for j in range(m)]
        prev.append("")

        for i in range(n-1,-1,-1):
            curr = [""]*m
            curr.append(str1[i:])

            for j in range(m-1,-1,-1):
                if str1[i] == str2[j]:
                    curr[j] = str1[i] + prev[j+1]
                else:
                    res1 = str1[i] + prev[j]
                    res2 = str2[j] + curr[j+1]

                    if len(res1) < len(res2):
                        curr[j] = res1
                    else:
                        curr[j] = res2
            prev = curr
        return curr[0]
s=Solution()
print(s.shortestCommonSupersequence("abac", "cab"))
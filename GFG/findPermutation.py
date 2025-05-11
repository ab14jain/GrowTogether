class Solution:
    def findPermutation(self, s):
        # Code here


        def permute(char_arr, permutations, idx, n, used, res):
            if n == idx:
                result_str = "".join(permutations)
                res.add(result_str)                
                return

            for i in range(len(used)):
                if not used[i]:
                    used[i] = True
                    permutations[idx] = char_arr[i]
                    permute(char_arr, permutations, idx+1, n, used, res)
                    used[i] = False
                    # permutations.pop()
                    #permute(char_arr, permutations, idx+1, n, used, res)

        
        n = len(s)
        used_char = [False]*n
        res = set()
        permutations = [""]*n
        permute(list(s), permutations, 0, n, used_char, res)
        return res
    

s=Solution()

print(s.findPermutation("ABC"))
print(s.findPermutation("ABSG"))
print(s.findPermutation("AAA"))
print(s.findPermutation("AAB"))
print(s.findPermutation("ABCDEFGHIJ"))
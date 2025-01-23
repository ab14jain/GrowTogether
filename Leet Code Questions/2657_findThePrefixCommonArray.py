class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        
        # n = len(A)
        # freq = [0] * (n + 1)    
        # res = [0] * n
        # count = 0
        # for i in range(n):
        #     if A[i] in freq:
        #         freq[A[i]] = freq[A[i]] + 1
        #     else:
        #         freq[A[i]] = 1
            

        #     if freq[A[i]] == 2:
        #         count += 1
            
        #     if B[i] in freq:
        #         freq[B[i]] = freq[B[i]] + 1
        #     else:
        #         freq[B[i]] = 1

        #     if freq[B[i]] == 2:
        #         count += 1

        #     res[i] = count

        # return res

        def prefix_match(A, B, size):

            count = 0
            for i in range(size+1):
                if(B.count(A[i])):
                    count += 1
            
            return count
                
        
        n = len(A)
        res = []
        setB = set()

        for i in range(0, n, 1):
            setB.add(B[i])
            res.append(prefix_match(A, B, i+1))

        return res
    
s=Solution()
print(s.findThePrefixCommonArray([2,1,2,4,2,2],[5,2,1,2,2,2])) # [2,3,3,3,3,3]
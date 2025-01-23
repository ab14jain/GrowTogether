class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        # stack = []
        # res = [0] * len(temperatures)

        # for i, t in enumerate(temperatures):
        #     while stack and t > temperatures[stack[-1]]:
        #         j = stack.pop()
        #         res[j] = i - j
        #     stack.append(i)

        # return res

        n = len(temperatures)
        stack = []
        NGR = [0]*n
        for i in range(n-1, -1, -1): 
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
               NGR[i] = stack[-1]            
            stack.append(i)  

        for i in range(n):
            if NGR[i] != 0:
                NGR[i] = NGR[i] - i

        return NGR   
    
s=Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]

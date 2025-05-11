import heapq


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        h1 = []
        h2 = []        
        n = len(A)
        

        def get_median(num):

            if len(h1) == 0 or num <= -h1[0]:
                heapq.heappush(h1, -num)
            else:
                heapq.heappush(h2, num)

            
            if len(h2) > len(h1):
                temp = heapq.heappop(h2)
                heapq.heappush(h1, -temp)

            if len(h1) - len(h2) == 2:
                temp = heapq.heappop(h1)
                heapq.heappush(h2, -temp)

            # if len(h1) > len(h2):
            #     return -h1[0]
            # else:
            #     median = (-h1[0] + h2[0])//2
            #     return median
            return -h1[0]
        
        ans = []
        for num in A:
            ans.append(get_median(num))

        return ans
    

s=Solution()
print(s.solve([59,64,10,39]))
print(s.solve([1,2,5,4,3]))
print(s.solve([5,17,100,11]))
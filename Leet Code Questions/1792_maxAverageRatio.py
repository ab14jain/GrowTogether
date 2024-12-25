import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        n = len(classes)
        maxAvg = 0
        avgDiffHeap = []
        for i in range(n):
            passed = classes[i][0]
            total = classes[i][1]
            
            avg = passed / total
            updatedAvg = (passed + 1) / (total + 1)
            diff = updatedAvg - avg
            heapq.heappush(avgDiffHeap,(-diff, i))

        while extraStudents > 0:                 
            
            bestAvg = heapq.heappop(avgDiffHeap)
            classes[bestAvg[1]][0] += 1
            classes[bestAvg[1]][1] += 1

            passed = classes[bestAvg[1]][0]
            total = classes[bestAvg[1]][1]
            avg = passed / total
            updatedAvg = (passed + 1) / (total + 1)
            diff = updatedAvg - avg
            heapq.heappush(avgDiffHeap,(-diff, bestAvg[1]))


            extraStudents -= 1

        for i in range(n):
            passed = classes[i][0]
            total = classes[i][1]
            avg = passed / total
            maxAvg += avg

        maxAvg = maxAvg/n 
        return maxAvg

s = Solution()
print(s.maxAverageRatio([[1,2],[3,5],[2,2]], 2)) # 0.78333
print(s.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4)) # 0.53485
print(s.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4)) # 0.53485
print(s.maxAverageRatio([[280,872],[108,128],[3,665],[93,972],[347,464],[443,584],[809,999],[366,398]], 77862)) # 0.0.97596

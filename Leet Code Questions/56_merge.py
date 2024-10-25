class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x : x[0])
        print(intervals)
        s1 = intervals[0][0]
        e1 = intervals[0][1]
        result = []
        for i in range(1, len(intervals)):
            s_curr = intervals[i][0]
            e_curr = intervals[i][1]
            if e1 >= s_curr and e_curr >= s1:
                e1 = max(e1, e_curr)
                s1 = min(s1, s_curr)
            else:
                result.append([s1, e1])
                s1 = s_curr
                e1 = e_curr

        result.append([s1, e1])   

        return result

# Time complexity: O(nlogn)
# Space complexity: O(1)
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))

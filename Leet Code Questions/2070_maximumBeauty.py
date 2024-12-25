class Solution:

    def binary_search(self, items, target):
        max_beauty = 0
        left = 0
        right = len(items) - 1
        mid = left + (right - left) // 2

        while left <= right:               
            if items[mid][0] > target:
                right = mid - 1
            else:
                max_beauty = max(max_beauty, items[mid][1])
                left = mid + 1        
            mid = left + (right - left) // 2  

        return max_beauty
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        
        items.sort(key = lambda x: x[0])

        if len(items) == 0:
            return -1
        p = len(items)
        q = len(queries)

        result = [0] * q
        
        max_beauty = items[0][1]
        for p in range(p):
            max_beauty = max(max_beauty, items[p][1])
            items[p][1]= max_beauty


        for i in range(q):
            target = queries[i]
            result[i] = self.binary_search(items, target)
        
        return result
                

        

        



s= Solution()
print(s.maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6])) # [2,4,5,5,6,6]
print(s.maximumBeauty([[1,2],[1,2],[1,3],[1,4]], [1])) # [4]
# print(s.maximumBeauty([[1,2],[2,3],[3,4]], [3,4])) # [1,2]  


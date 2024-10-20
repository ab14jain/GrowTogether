class Solution:
    def maximumProduct(self, n : int, arr : list[int], l : int, r : int) -> int:
         # code here
        if len(arr) == 0:
            return 0
            
        max_1 = arr[l - 1]
        min_1 = arr[l - 1]
        for i in range(l - 1, r):
            if max_1 < arr[i]:
                max_1 = arr[i]
            if min_1 > arr[i]:
                min_1 = arr[i]
        
        max_2 = -100000000000
        min_2 = arr[0]
        for i in range(len(arr)):
            if i < (l-1) or i > (r-1):
                if max_2 < arr[i]:
                    max_2 = arr[i]
                if min_2 > arr[i]:
                    min_2 = arr[i]
            
        # if max_1 < 0 and max_2 < 0:
        #     return min_1 * min_2
        # elif max_1 < 0:
        #     if min_2 < 0:
        #         return max_2 * max_1
        #     return max_1 * min_2
        # elif max_2 < 0:
        #     if min_1 < 0:
        #         return max_2 * max_1
        #     return max_2 * min_1
        # else:
        #     return max_1 * max_2

        p1 = max_1 * max_2
        p2 = min_1 * min_2
        p3 = max_1 * min_2
        p4 = min_1 * max_2

        if max_1 == min_1 or max_2 == min_2:
            return max_1 * max_2
        return max(p1, p2, p3, p4)


s = Solution()

print(s.maximumProduct(3, [2, 10, -8], 3, 3)) # -16
print(s.maximumProduct(2, [-97, -518], 1, 1)) # 50246
print(s.maximumProduct(2, [-4, 4], 2, 2)) # -16
print(s.maximumProduct(9, [-7, -1, -6, -7, 6, 8, 1, 6, -9], 5, 8)) # -1
print(s.maximumProduct(6, [0, -10, -1, 7, -1, -8], 1, 4)) # -80
print(s.maximumProduct(5, [3, 4, 7, 1, 2], 2, 4)) # 21
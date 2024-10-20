class Solution:
    def maximumSwap(self, num: int) -> int:
        
        lists = list(str(num))
        n = len(lists)
        nums = [-1] * 10

        for i in range(n):
            nums[int(lists[i])] = i
        
        
        for i in range(n):
            for j in range(9, int(lists[i]), -1):
                if nums[j] > i:
                    lists[i], lists[nums[j]] = lists[nums[j]], lists[i]
                    return int(''.join(lists))
                else:
                    continue
        
        return num


        # max_right = [0] * n
        # max_right[n-1] = n-1
        # for i in range(n-2, -1, -1):
        #     if lists[i] >= lists[max_right[i+1]]:
        #         max_right[i] = i
        #     else:
        #         max_right[i] = max_right[i+1]
        
        # for i in range(n):
        #     if lists[i] < lists[max_right[i]]:
        #         lists[i], lists[max_right[i]] = lists[max_right[i]], lists[i]
        #         break

        # print(max_right)
        # return int(''.join(lists))
        # return nums

s = Solution()
print(s.maximumSwap(0)) # 97894672
print(s.maximumSwap(27894679)) # 97894672
print(s.maximumSwap(2736)) # 7236
print(s.maximumSwap(9937)) # 9973
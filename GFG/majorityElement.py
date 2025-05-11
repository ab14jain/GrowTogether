class Solution:
    def majorityElement(self, arr):
        #code here

        maj_count = 0
        prev = arr[0]
        i = 0
        n = len(arr)
        while i < n:

            if arr[i] == prev:
                maj_count += 1
            else:
                maj_count -= 1

                if maj_count == 0:
                   prev = arr[i]
                   maj_count = 1
                    
            i += 1
        prev_count = arr.count(prev)

        if prev_count <= n//2:
            return -1
        return prev

s=Solution()
print(s.majorityElement([2, 13]))
print(s.majorityElement([2, 1, 3, 5, 1, 1, 1]))
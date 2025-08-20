class Solution:
    def rearrange(self, arr, x):
        # code here
        # temp = []

        # n = len(arr)
        # for i in range(n):
        #     temp.append([arr[i], abs(x-arr[i])])

        # temp.sort(key = lambda x : x[1])

        # ans = []

        # for i in range(n):
        #     arr[i] = temp[i][0]
        
        
        # return arr

        arr.sort(key=lambda a: abs(a-x))
        return arr

s=Solution()
print(s.rearrange([10,5,3,9,2], 7))
#https://www.geeksforgeeks.org/problems/minimize-the-heights-i/1

#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        n = len(arr)
        arr.sort()
               
        ans = arr[n-1] - arr[0]
        # print(ans)
        for i in range(1, n):
            # if arr[i] - k < 0:
            #     continue
            min_ele = min(arr[0]+k, arr[i]-k)
            # print(min_ele)
            max_ele = max(arr[n-1]-k, arr[i-1]+k)
            # print(max_ele)
            ans = min(ans, max_ele - min_ele)

        return ans
    
s=Solution()
print(s.getMinDiff(4, [-10, -2, -8, 2, 3])) #5
# print(s.getMinDiff(2, [1, 5, 8, 10])) #5
# print(s.getMinDiff(3, [3, 9, 12, 16, 20])) #11
# print(s.getMinDiff(4, [6, 1, 9, 1, 1, 7, 9, 5, 2, 10])) #5
class Solution:
    def farMin(self, arr):
        # Code Here
        #Method 1: Brute force:
        # n = len(arr)
        # ans = [-1]*n
        # for i in range(n):
        #     for j in range(i+1, n):
                
        #         if arr[i] > arr[j]:
        #             ans[i] = j

        # return ans


        #Method 2 - binary Search
        #TC - nlogn
        #SC - n
        #Optmized
        n = len(arr)
        res = [-1]*n
        suff = arr.copy()
        suff[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = min(arr[i], suff[i + 1])
        
        

        for i in range(n):

            l = i+1
            h = n-1
            ans = -1

            while l <= h:
                mid = (l+h)//2

                if suff[mid] < arr[i]:
                    ans = mid
                    l = mid + 1
                else:
                    h = mid - 1
            
            res[i] = ans

        return res

        # n = len(arr)
        # res = [-1] * n
        # stack = []  # will store indices (monotonic increasing by value)

        # for i in range(n-1, -1, -1):
        #     # Maintain increasing stack by values
        #     while stack and arr[stack[-1]] >= arr[i]:
        #         stack.pop()
            
        #     if stack:
        #         res[i] = stack[-1]   # farthest smaller index for i
        #     stack.append(i)

        # return res


s=Solution()
print(s.farMin([2,5,1,3,2]))
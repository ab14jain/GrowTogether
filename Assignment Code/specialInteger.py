#https://www.scaler.com/academy/mentee-dashboard/class/325324/homework/problems/4133?navref=cl_tt_nv
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        def isValid(arr, w, target):
            p_sum = 0
            n = len(arr)
            for i in range(w):
                p_sum += arr[i]
                if p_sum > target:
                    return False
            
            for i in range(w, n):
                p_sum = p_sum + arr[i] - arr[i - w]
                if p_sum > target:
                    return False
            
            return True


        n = len(A)
        low = 1
        # At max the answer can be the maximum element in the array
        high = n
        ans = 0
        while low <= high:
            mid = low + (high-low)//2    

            if isValid(A, mid, B):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1    

        return ans

# Time complexity: O(nlogn)
# Space complexity: O(1)

s=Solution()
print(s.solve([1,-2,3,-4,5,23,-46,78,99,102,456], 755)) # 2
print(s.solve([1, 2, 3, 4, 5], 10)) # 2
print(s.solve([5, 17, 100, 11], 130)) # 3
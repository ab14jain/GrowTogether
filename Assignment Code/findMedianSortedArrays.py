class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            t = A[:]
            A = B[:]
            B = t[:]

        m = len(A)
        n = len(B)
        total = m + n
        first_half = (total + 1)//2
        left = 0
        right = min(m,first_half)
        median = 0
        while left<=right:
            mid = (left+right)//2
            if mid > 0:
                l1 = A[mid - 1]
            else:
                l1 = float('-inf')
            if mid < m:
                r1 = A[mid]
            else:
                r1 = float('inf')

            countB = first_half - mid
            if countB > 0:
                l2 = B[countB-1]
            else:
                l2 = float('-inf')
            # l2 = B[countB-1]
            # r2 = B[countB]
            if countB < n:
                r2 = B[countB]
            else:
                r2 = float('inf')

            if l2 > r1:
                left = mid + 1
            elif l1 > r2:
                right = mid - 1
            else:
                if total % 2 == 0:
                    median = (max(l1,l2)+min(r1,r2))/2
                else:
                    median = max(l1,l2)                
        
                return median


s= Solution()
# print(s.solve([1, 3], [2])) #3
# print(s.solve([1, 4, 5], [2, 3])) #3
# print(s.solve([1, 3, 4], [2, 5, 6])) #3
# print(s.solve([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])) #5
print(s.solve([1,3,4,5,6,7,8,9,10],[2])) #3
print(s.solve([1,3,4,5,6,7,8,9,10],[])) #3
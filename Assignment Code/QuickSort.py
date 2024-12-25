class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        def partition(A, s, e):
            pivot = A[s]
            i = s+1
            j = e
            
            while i <= j:
                if A[i] < pivot:
                    i += 1
                elif A[j] > pivot:
                    j -= 1
                else:
                    A[i],A[j]=A[j],A[i]
                    i += 1
                    j -= 1

            A[s],A[j]=A[j],A[s]
            return j

        def quick_sort(A, s, e):

            if s >= e:
                return

            pivot_idx = partition(A, s, e)
            quick_sort(A, s, pivot_idx-1)
            quick_sort(A, pivot_idx+1, e)
    
        quick_sort(A, 0, len(A)-1)
        return A

s= Solution()
# print(s.solve([8,89])) #9534330
print(s.solve([3, 30, 34, 5, 9])) #9534330
#https://www.scaler.com/academy/mentee-dashboard/class/325324/homework/problems/270?navref=cl_tt_lst_nm
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
        
            n = len(A)
            if n < B:
                return -1

            low = max(A)
            high = sum(A)

            while low <= high:

                mid = low + (high - low)//2
                i = 0
                pages = 0
                students = 1
                while i < n:
                    if A[i]+ pages <= mid:
                        pages = A[i] + pages        
                    else:
                        students += 1
                        pages = A[i]
                    
                    i += 1
                

                if students > B:                    
                    low = mid + 1
                else:
                    high = mid - 1
                
            
            return low

s=Solution()
print(s.books([12, 34, 67, 90], 2)) # 113
print(s.books([12, 15, 78] , 4)) # -1
print(s.books([1,2,3,4,5] , 5)) # 5
print(s.books([1,2,3,4,5] , 4)) # 5
print(s.books([1,2,3,4,5] , 3)) # 6
print(s.books([1,2,3,4,5] , 2)) # 9

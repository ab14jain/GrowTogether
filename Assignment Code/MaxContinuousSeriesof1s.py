#https://www.scaler.com/academy/mentee-dashboard/class/325312/homework/problems/273?navref=cl_tt_nv
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def maxone(self, A, B):
		
            # n = len(A)
            # max_len = 0
            # start_idx = -1
            # end_idx = -1
            # for i in range(n):                  
            #     if (A[i] == 0 and B > 0) or A[i] == 1:                    
            #         rem_zero = B-1
            #         j = i-1
            #         k = i+1

            #         while j > -1:
            #             if A[j] == 1:
            #                 j -= 1
            #             elif A[j] == 0 and rem_zero > 0:
            #                 j -= 1
            #                 rem_zero -= 1
            #             else:
            #                 break

            #         while k < n:
            #             if A[k] == 1:
            #                 k += 1
            #             elif A[k] == 0 and rem_zero > 0:
            #                 k += 1
            #                 rem_zero -= 1
            #             else:
            #                 break                    

            #         if max_len < (k-j-1):
            #             max_len = (k-j-1)
            #             start_idx = j+1
            #             end_idx = k-1

            # ans = []
            # for i in range(start_idx, end_idx+1):
            #     ans.append(i)
            # return ans

            i = 0
            j = 0
            n = len(A)
            zero_count = 0
            window_size = 0
            ans = 0
            final_i = 0
            final_j = 0
            while j < n:   
                if A[j] == 0:
                    zero_count += 1 

                while zero_count > B:
                    if A[i] == 0:
                        zero_count -= 1

                    window_size -= 1
                    i += 1 

                if ans < window_size:
                    ans = window_size
                    final_i = i
                    final_j = j

                window_size += 1                
                j += 1
                
            ans = []
            for i in range(final_i, final_j+1):
                ans.append(i)
            return ans       

s=Solution()
print(s.maxone([0], 0))
print(s.maxone([0], 1))
print(s.maxone([1], 0))
print(s.maxone([0,1,1,1], 0))
print(s.maxone([1,1,0,1,1,0,0,1,1,1], 1))
print(s.maxone([1,1,0,1,1,0,0,1,1,1,1,1], 1))
print(s.maxone([1, 0, 0, 0, 1, 0, 1], 2))
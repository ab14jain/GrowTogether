import math
from statistics import median


class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):

            # n = len(A)
            # h_map = []
            # for i in range(n):
            #     if A[i] == 'x':
            #         h_map.append(i)

            # min_cost = float('inf')
            # for i in h_map:
            #     curr = i
            #     next_pos = curr + 1
            #     cost = 0

            #     while 
            MOD = 10000003          
            n = len(A)
            seats = []
            seats_count = 0
            for i in range(n): 
                if A[i] == 'x':
                    seats.append(i)
                    seats_count += 1

            # med = math.floor(median(seats))
            m = len(seats)
            mid = m//2
            left = mid-1
            right = mid+1
            k = 1
            res = 0
            while left >= 0:
                res += seats[mid]-k-seats[left]
                left -= 1
                k += 1
            k = 1
            while right < m:
                res += seats[right] - seats[mid] - k
                right += 1
                k += 1
            
            return res%MOD
		



s=Solution()
print(s.seats("....x..xx...x.."))
print(s.seats("....xxx"))
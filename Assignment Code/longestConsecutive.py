#https://www.scaler.com/academy/mentee-dashboard/class/325342/assignment/problems/152?navref=cl_tt_lst_nm


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):		
        
            h_map = set()
            for num in A:
                h_map.add(num)

            n = len(A)
            max_nums = 1
            for num in h_map:                
                curr_num = num
                count = 0
                if (curr_num - 1) not in h_map:
                    while curr_num in h_map:                    
                        curr_num += 1
                        count += 1     

                max_nums = max(max_nums, count)

            return max_nums
    

s=Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([2,1]))
print(s.longestConsecutive([2,1,3,0,-1,-2,-3,5,7,-4,2,4,-4,5,-3,6]))